import os
from crewai import Agent, Task, Crew, Process
from langchain_google_genai import ChatGoogleGenerativeAI
from decouple import config

from textwrap import dedent
from agents import AIProjectManagerAgents
from tasks import CustomTasks
from langchain_google_genai import ChatGoogleGenerativeAI
from crewai_tools import SerperDevTool

# Install duckduckgo-search for this example:
# !pip install -U duckduckgo-search

# from langchain.tools import DuckDuckGoSearchRun

# search_tool = DuckDuckGoSearchRun()

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = './marcotalkdev-9de592a0ca42.json'
os.environ["GOOGLE_API_KEY"] = "AIzaSyDDRR5s1oS7VWA8f-g4vd7Dy4vUEjzGy5k"
os.environ["SERPER_API_KEY"] = "c60ef23e3e8de39f66bd250da3aaceb5476375ea"
# This is the main class that you will use to define your custom crew.
# You can define as many agents and tasks as you want in agents.py and tasks.py


class CustomCrew:
    def __init__(self):
        self.user_story = input(dedent("""What is the user story that you need to accomplish?"""))
        self.GeminiPro = ChatGoogleGenerativeAI(model="gemini-pro")

    def run(self):
        # Define your custom agents and tasks in agents.py and tasks.py
        agents = AIProjectManagerAgents()
        tasks = CustomTasks()


        print("Added agent")

        # Define your custom agents and tasks here
        # research_agent = agents.researcher()
        # lead_gen_agent = agents.lead_generator()
        # copywriting_agent = agents.email_copywriter()
        prompt_engineer = agents.prompt_engineer()

        # Custom tasks include agent name and variables as input
        # research_task = tasks.firm_lead_generation(
        #     research_agent,
        #     self.company_name,
        #     self.company_description,
        #     self.company_stage,
        # )

        prompt_engineer_task = tasks.chat_prompt_engineering(
            prompt_engineer,
            self.user_story
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
            agents=[prompt_engineer],
            tasks=[prompt_engineer_task],
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
    with open("output.txt", "w") as text_file:
        text_file.write(result)
