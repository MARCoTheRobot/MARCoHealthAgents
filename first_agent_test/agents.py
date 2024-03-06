from crewai import Agent
from textwrap import dedent
import os

from langchain_google_genai import ChatGoogleGenerativeAI



# This is an example of how to define custom agents.
# You can define as many agents as you want.
# You can also define custom tasks in tasks.py
class CustomAgents:
    def __init__(self):
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = './marcotalkdev-9de592a0ca42.json'
        os.environ["GOOGLE_API_KEY"] = "AIzaSyDDRR5s1oS7VWA8f-g4vd7Dy4vUEjzGy5k"
        self.GeminiPro = ChatGoogleGenerativeAI(model="gemini-pro")

    def story_writer(self):
        print("story_writer")
        return Agent(
            role="User story write",
            backstory=dedent(f"""You are a gen Z user story writer at a leading technology company that develops mental health apps to support teenagers and young adults who feel anxious, depressed, and lonely. You specialize in empathizing with what teenagers want to do when they need help with their mental health. You do your best to write user stories and consider what really matters to these teens."""),
            goal=dedent(f"""Create user stories for a software project"""),
            # tools=[tool_1, tool_2],
            allow_delegation=False,
            verbose=True,
            llm=self.GeminiPro,
        )

    def project_manager(self):
        print("project_manager")
        return Agent(
            role="Senior Project Manager",
            backstory=dedent(f"""You are a senior project manager and SCRUM master at a leading technology company that develops mental health apps to support teenagers and young adults who feel anxious, depressed, and lonely. You specialize in managing software projects and leading software sprints. You do your best to prepare project requirements and project plans for software sprints. You have high attention to detail when preparing project requirements and project plans for software sprints. You also have a knack for finding hidden bugs and security vulnerabilities."""),
            goal=dedent(f"""Prepare project requirements and project plans for software sprints"""),
            # tools=[tool_1, tool_2],
            allow_delegation=False,
            verbose=True,
            llm=self.GeminiPro,
        )
