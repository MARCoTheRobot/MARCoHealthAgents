from crewai import Agent
from textwrap import dedent
import os

from langchain_google_genai import ChatGoogleGenerativeAI
from crewai_tools import SerperDevTool
search_tool = SerperDevTool()



# This is an example of how to define custom agents.
# You can define as many agents as you want.
# You can also define custom tasks in tasks.py
class AIProjectManagerAgents:
    def __init__(self):
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = './marcotalkdev-9de592a0ca42.json'
        os.environ["GOOGLE_API_KEY"] = "AIzaSyDDRR5s1oS7VWA8f-g4vd7Dy4vUEjzGy5k"
        os.environ["SERPER_API_KEY"] = "c60ef23e3e8de39f66bd250da3aaceb5476375ea"
        self.GeminiPro = ChatGoogleGenerativeAI(model="gemini-pro", temperature=0.9, max_tokens=1040, top_p=1.0, frequency_penalty=0.0, presence_penalty=0.0, stop=["\n", "###"])

    def project_researcher(self):
        print("Researcher Init")
        return Agent(
            role="Senior User Experience Researcher",
            backstory=dedent(f"""You are an expert lead generation specialist with decades of experience of finding investors and venture capitalists for tech startups across the US. 
            You specialize in finding the names and details of venture capital firms and angel investors who best meet a startup's criteria. You also rank each opportunity for the startups from 1 to 10 based on the likelihood of investment and quality of the match. 
            You do your best to find the best opportunities for the startups and help them get the funding they need to grow and succeed."""),
            goal=dedent(f"""Create a list of investors and venture capitalists for a tech startup to reach out to for funding"""),
            tools=[search_tool],
            allow_delegation=False,
            verbose=True,
            llm=self.GeminiPro,
        )

    # The prompt engineer agent is intended to work on creating prompts for the AI to generate content.
    def prompt_engineer(self):
        print("Prompt Engineer Init")
        return Agent(
            role="Senior Prompt Engineer",
            backstory=dedent(
                f"""
            You are a senior prompt engineer with years of experience in creating prompts for AI models. 
            You specialize in creating prompts that are clear, concise, and effective in generating the desired content.
            You focus on using the best practices in prompt engineering with a focus on creating prompts that give the AI personality and follow directions effectively."""),
            goal=dedent(f"""Generate a set of prompts for an AI model to achieve the desired customer use case"""),
            # tools=[tool_1, tool_2],
            allow_delegation=False,
            verbose=True,
            llm=self.GeminiPro,
        )
