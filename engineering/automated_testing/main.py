import os
from dotenv import load_dotenv
from crewai import Agent, Task, Crew, Process
from langchain_google_genai import ChatGoogleGenerativeAI
from decouple import config

from textwrap import dedent
from agents import AITestCaseGenerators
from tasks import TestTasks
from langchain_google_genai import ChatGoogleGenerativeAI
from crewai_tools import SerperDevTool
load_dotenv()

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = './marcotalkdev-9de592a0ca42.json'

class CustomCrew:
    def __init__(self):
        self.language = input(dedent("""What is the primary programming language that the team will be using for tests? It should either be Python, Java, CSharp, Ruby, JavaScript, or Kotlin."""))
        self.software = input(dedent("""Enter the full path of the source code directory that these tests will need to reference. If you know the location of the files that contain the test cases, please enter the full path of the specific subdirectory that contains these files.""")) 
        self.use_case = input(dedent("""What are the user stories and requirements that need to be tested?"""))
        self.additional_details = input(dedent("""What are the additional details for the project or process that would be useful to the team?"""))
        self.GeminiPro = ChatGoogleGenerativeAI(model="gemini-pro", temperature=1, max_tokens=2048, top_p=1.0, frequency_penalty=0.0, presence_penalty=0.0, stop=["\n", "###"])

    def run(self):
        print("AGENTS START")
        agents = AITestCaseGenerators()

        print("TASKS START")
        tasks = TestTasks()

        print("Added agent")


        
        print("PROJECT MANAGER")
        project_manager = agents.manager_agent()
        print("SW ENGINEER")
        test_engineer = agents.software_dev_agent(self.language)

        print("DESCRIPTION WRITING")
        project_manager_task = tasks.test_requirement_writeup(
            project_manager,
            self.use_case,
            self.additional_details
        )

        print("TEST WRITING")
        task_engineer_task = tasks.test_writeup(
            test_engineer,
            self.use_case,
            self.additional_details
        )

        print("CREW CREW CREW")
        crew = Crew(
            agents=[project_manager, test_engineer],
            tasks=[project_manager_task, task_engineer_task],
            verbose=True,
        )

        print("KICKOFF")
        result = crew.kickoff()

        with open("tasks.txt", "w") as text_file:
            text_file.write(result)

         # Extract relevant information from agent_engineer
        # agent_engineer_output = f"Role: {agent_engineer.role}\nBackstory: {agent_engineer.backstory}\nGoal: {agent_engineer.goal}\nTools: {agent_engineer.tools}\n"

        # # Now save the output related to the agent_engineer to a file
        # with open("agent_engineer_output.txt", "w") as text_file:
        #     text_file.write(agent_engineer_output)


if __name__ == "__main__":
    print("## Welcome to Crew AI Template")
    print("-------------------------------")
    
    custom_crew = CustomCrew()
    custom_crew.run()
