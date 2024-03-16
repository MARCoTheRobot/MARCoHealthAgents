import os
from crewai import Agent, Task, Crew, Process
from langchain_google_genai import ChatGoogleGenerativeAI
from decouple import config

from textwrap import dedent
from agents import CustomAgents
from tasks import CustomTasks
from langchain_google_genai import ChatGoogleGenerativeAI

# Install duckduckgo-search for this example:
# !pip install -U duckduckgo-search

# from langchain.tools import DuckDuckGoSearchRun

# search_tool = DuckDuckGoSearchRun()

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = './marcotalkdev-9de592a0ca42.json'
os.environ["GOOGLE_API_KEY"] = "AIzaSyDDRR5s1oS7VWA8f-g4vd7Dy4vUEjzGy5k"

# This is the main class that you will use to define your custom crew.
# You can define as many agents and tasks as you want in agents.py and tasks.py


class CustomCrew:
    def __init__(self, var1, var2):
        self.var1 = var1
        self.var2 = var2
        self.GeminiPro = ChatGoogleGenerativeAI(model="gemini-pro")

    def __tip_section(self):
        return "If you do your BEST WORK, I'll give you a $10,000 commission!"

    def run(self):
        # Define your custom agents and tasks in agents.py and tasks.py
        agents = CustomAgents()
        tasks = CustomTasks()

        agent_1 = Agent(
            role="User story write",
            backstory=dedent(f"""You are a gen Z user story writer at a leading technology company that develops mental health apps to support teenagers and young adults who feel anxious, depressed, and lonely. You specialize in empathizing with what teenagers want to do when they need help with their mental health. You do your best to write user stories and consider what really matters to these teens."""),
            goal=dedent(f"""Create user stories for a software project"""),
            # tools=[tool_1, tool_2],
            allow_delegation=False,
            verbose=True,
            llm=self.GeminiPro,
        )

        print("Added agent")

        # Define your custom agents and tasks here
        custom_agent_1 = agents.story_writer()
        custom_agent_2 = agents.project_manager()

        # Custom tasks include agent name and variables as input
        custom_task_1 = tasks.story_writing(
            custom_agent_1,
        )

        # custom_task_1 = Task(
        #     description=dedent(
        #         f"""
        #     Write a user story for a teenager approaching the app for the first time who is in the middle of a panic attack.
            
        #     {self.__tip_section()}
    
        #    Write the story in the format of 'I'm a teenager who is in the middle of a panic attack and I need help with...'.
        #    Consider the details of their setting, what they're feeling, and what they need to feel better. Think also about timing and location.
        # """
        #     ),
        #     agent=custom_agent_1,
        # )

        custom_task_2 = tasks.project_writing(
            custom_agent_2,
        )
        # custom_task_2 = Task(
        #     description=dedent(
        #         f"""
        #     Take the input from the user story and write a project requirement for a software sprint.
                                       
        #     {self.__tip_section()}

        #     Write it out in sections, including the user story, acceptance criteria, and any other details that you think are important. 
        #     Write out a delegation plan of who needs to take on what critical tasks, and give an estimate of time to completion.
        # """
        #     ),
        #     agent=custom_agent_2,
        # )
        

        # Define your custom crew here
        crew = Crew(
            agents=[custom_agent_1, custom_agent_2],
            tasks=[custom_task_1, custom_task_2],
            verbose=True,
        )

        result = crew.kickoff()
        return result


# This is the main function that you will use to run your custom crew.
if __name__ == "__main__":
    print("## Welcome to Crew AI Template")
    print("-------------------------------")
    var1 = input(dedent("""Enter variable 1: """))
    var2 = input(dedent("""Enter variable 2: """))

    custom_crew = CustomCrew(var1, var2)
    result = custom_crew.run()
    print("\n\n########################")
    print("## Here is you custom crew run result:")
    print("########################\n")
    print(result)
