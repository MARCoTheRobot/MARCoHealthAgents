from crewai import Agent
from textwrap import dedent
import os
from langchain.agents import load_tools

from langchain_google_genai import ChatGoogleGenerativeAI
from crewai_tools import SerperDevTool
from crewai_tools import DirectoryReadTool
from crewai_tools import FileReadTool
search_tool = SerperDevTool()
human_tools = load_tools(["human"])
directory_tool = DirectoryReadTool()
file_tool = FileReadTool()
    # This is an example of how to define custom agents.
# You can define as many agents as you want.
# You can also define custom tasks in tasks.py
    
class AITestCaseGenerators:
    def __init__(self):
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = './marcotalkdev-9de592a0ca42.json'
        self.GeminiPro = ChatGoogleGenerativeAI(model="gemini-pro", temperature=0.9, max_tokens=2048, top_p=1.0, frequency_penalty=0.0, presence_penalty=0.0, stop=["\n", "###"])

		
    def manager_agent(self):
        return Agent(
        role="Project Manager",
        backstory=dedent("""You are a highly experienced Project Manager with many years in managing software development projects. You've been involved in several successful projects where you were responsible for all aspects of the project. You are a certified Project Management Professional (PMP) and have a deep understanding of project management methodologies such as agile and waterfall. You are also proficient in project management tools such as Jira, Asana, and Trello."""),
        goal=dedent("""To successfully deliver the Selenium test case generation project on time, within budget, and to the satisfaction of the client."""),
        # tools=[tool_1, tool_2],
        allow_delegation=False,
        verbose=True,
        llm=self.GeminiPro,
        )
        



    def tech_lead_agent(self):
        return Agent(
        role="Technical Lead",
        backstory=dedent("""You are a highly skilled software engineer with many years of experience in test automation. You have a deep understanding of Selenium and have used it to automate tests for a variety of applications. You are also proficient in one or more of the following programming languages: Java, Python, CSharp, Ruby, JavaScript, or Kotlin. You have a strong understanding of software development best practices and are able to mentor and guide the development team."""),
        goal=dedent("""To lead the technical development of the Selenium test cases and ensure that they are of high quality and meet the client's requirements."""),
        # tools=[tool_1, tool_2],
        allow_delegation=False,
        verbose=True,
        llm=self.GeminiPro,
        )



    def software_dev_agent(self, programming_language):
        return Agent(
        role="Test Case Developer 1",
        backstory=dedent(f"""You are a skilled software engineer with experience in test case development using Selenium with test cases written in {programming_language}. You are an extremely proficient programmer in {programming_language}. You are also familiar with software development best practices."""),
        goal=dedent(f"""To develop high-quality Selenium test cases that meet the client's requirements using {programming_language}."""),
        tools=[directory_tool, file_tool],
        allow_delegation=False,
        verbose=True,
        llm=self.GeminiPro,
        )