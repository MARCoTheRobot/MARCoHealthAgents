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

# Install duckduckgo-search for this example:
# !pip install -U duckduckgo-search

# from langchain.tools import DuckDuckGoSearchRun

# search_tool = DuckDuckGoSearchRun()

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = './marcotalkdev-9de592a0ca42.json'
# os.environ["GOOGLE_API_KEY"] = os.get
# os.environ["SERPER_API_KEY"] = "4bea7bd2d55f035a29de22f73f6e3e8e289c406e"
# This is the main class that you will use to define your custom crew.
# You can define as many agents and tasks as you want in agents.py and tasks.py


class CustomCrew:
    def __init__(self):
        self.use_case = input(dedent("""What is the project or operation that this team needs to tackle?"""))
        self.additional_details = input(dedent("""What are the additional details for the project or process that would be useful to the team?"""))
        # self.GeminiPro = ChatGoogleGenerativeAI(model="gemini-pro")
        self.GeminiPro = ChatGoogleGenerativeAI(model="gemini-pro", temperature=1, max_tokens=2048, top_p=1.0, frequency_penalty=0.0, presence_penalty=0.0, stop=["\n", "###"])

    def run(self):
        # Define your custom agents and tasks in agents.py and tasks.py
        agents = AIProjectManagerAgents()
        tasks = CustomTasks()


        print("Added agent")

        # Define your custom agents and tasks here

        # First is the project manager, who will be writing up the detailed project description based on the user input
        project_manager = agents.project_manger()

        # Second agent is the prompt engineer focused on developing AI agents for the project
        agent_engineer = agents.agent_prompt_engineer()

        # Third agent is the task engineer
        task_engineer = agents.task_prompt_engineer()

        # Custom tasks include agent name and variables as input


        project_manager_task = tasks.project_description_writing(
            project_manager,
            self.use_case,
            self.additional_details
        )

        agent_engineer_task = tasks.agent_prompt_engineering(
            agent_engineer,
            self.use_case,
            self.additional_details
        )

        task_engineer_task = tasks.task_prompt_engineering(
            task_engineer,
            self.use_case,
            self.additional_details
        )

        # lead_gen_task = tasks.lead_generation(
        #     research_agent
        # )

        # copywriting_task = tasks.email_copywriting(
        #     copywriting_agent,
        #     self.company_name,
        #     self.company_description,
        #     self.raise_target,
        # )
        

        # Define your custom crew here
        crew = Crew(
            agents=[project_manager, agent_engineer, task_engineer],
            tasks=[project_manager_task, agent_engineer_task, task_engineer_task],
            verbose=True,
        )

        result = crew.kickoff()
        return result


# This is the main function that you will use to run your custom crew.
if __name__ == "__main__":
    print("## Welcome to Crew AI Template")
    print("-------------------------------")
    


    custom_crew = CustomCrew()
    result = custom_crew.run()
    print("\n\n########################")
    print("## Here is you custom crew run result:")
    print("########################\n")
    print(result)

    # Now save the result to a file
    with open("tasks.txt", "w") as text_file:
        text_file.write(result)
