import os
from dotenv import load_dotenv
from crewai import Agent, Task, Crew, Process
from langchain_google_genai import ChatGoogleGenerativeAI
from decouple import config

from textwrap import dedent
from agents import AIProjectManagerAgents
from tasks import CustomTasks
from langchain_google_genai import ChatGoogleGenerativeAI
from crewai_tools import SerperDevTool
load_dotenv()

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = './marcotalkdev-9de592a0ca42.json'

class CustomCrew:
    def __init__(self):
        self.use_case = input(dedent("""What is the project or operation that this team needs to tackle?"""))
        self.additional_details = input(dedent("""What are the additional details for the project or process that would be useful to the team?"""))
        self.GeminiPro = ChatGoogleGenerativeAI(model="gemini-pro", temperature=1, max_tokens=2048, top_p=1.0, frequency_penalty=0.0, presence_penalty=0.0, stop=["\n", "###"])

    def run(self):
        print("AGENTS START")
        agents = AIProjectManagerAgents()

        print("TASKS START")
        tasks = CustomTasks()

        print("Added agent")


        project_manager = agents.project_manger()
        print("AGENT ENGINEER")
        agent_engineer = agents.agent_prompt_engineer()
        print("TASK ENGINEER")
        task_engineer = agents.task_prompt_engineer()

        print("DESCRIPTION WRITING")
        project_manager_task = tasks.project_description_writing(
            project_manager,
            self.use_case,
            self.additional_details
        )

        print("AGENT PROMPT ENGINEERING")
        agent_engineer_task = tasks.agent_prompt_engineering(
            agent_engineer,
            self.use_case,
            self.additional_details
        )

        print("TASK PROMPT ENGINEERING")
        task_engineer_task = tasks.task_prompt_engineering(
            task_engineer,
            self.use_case,
            self.additional_details
        )

        print("CREW CREW CREW")
        crew = Crew(
            agents=[project_manager, agent_engineer, task_engineer],
            tasks=[project_manager_task, agent_engineer_task, task_engineer_task],
            verbose=True,
        )

        print("KICKOFF")
        result = crew.kickoff()

        with open("tasks.txt", "w") as text_file:
            text_file.write(result)

         # Extract relevant information from agent_engineer
        agent_engineer_output = f"Role: {agent_engineer.role}\nBackstory: {agent_engineer.backstory}\nGoal: {agent_engineer.goal}\nTools: {agent_engineer.tools}\n"

        # Now save the output related to the agent_engineer to a file
        with open("agent_engineer_output.txt", "w") as text_file:
            text_file.write(agent_engineer_output)


if __name__ == "__main__":
    print("## Welcome to Crew AI Template")
    print("-------------------------------")
    
    custom_crew = CustomCrew()
    custom_crew.run()
