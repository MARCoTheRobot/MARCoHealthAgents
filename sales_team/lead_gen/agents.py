from crewai import Agent
from textwrap import dedent
import os

from langchain_google_genai import ChatGoogleGenerativeAI
from crewai_tools import SerperDevTool
search_tool = SerperDevTool()



# This is an example of how to define custom agents.
# You can define as many agents as you want.
# You can also define custom tasks in tasks.py
class CustomAgents:
    def __init__(self):
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = './marcotalkdev-9de592a0ca42.json'
        os.environ["GOOGLE_API_KEY"] = "AIzaSyDDRR5s1oS7VWA8f-g4vd7Dy4vUEjzGy5k"
        os.environ["SERPER_API_KEY"] = "c60ef23e3e8de39f66bd250da3aaceb5476375ea"
        self.GeminiPro = ChatGoogleGenerativeAI(model="gemini-pro")

    def researcher(self):
        print("Researcher Init")
        return Agent(
            role="Angel Investor and VC Firm Lead Generator",
            backstory=dedent(f"""You are an expert lead generation specialist with decades of experience of finding investors and venture capitalists for tech startups across the US. 
            You specialize in finding the names and details of venture capital firms and angel investors who best meet a startup's criteria. You also rank each opportunity for the startups from 1 to 10 based on the likelihood of investment and quality of the match. 
            You do your best to find the best opportunities for the startups and help them get the funding they need to grow and succeed."""),
            goal=dedent(f"""Create a list of investors and venture capitalists for a tech startup to reach out to for funding"""),
            tools=[search_tool],
            allow_delegation=False,
            verbose=True,
            llm=self.GeminiPro,
        )

    def email_copywriter(self):
        print("Copywriter init")
        return Agent(
            role="CEO and Master Email Copywriter",
            backstory=dedent(f"""You are Jacob Boyle, the CEO at MARCo Health Inc, and right now you specialize in writing high-converting email copy for tech startups. You specialize in writing emails that get opened, read, and clicked. 
            You also specialize in writing emails that get responses and convert into sales and investments. 
            You have mastered the art of writing concise emails in a storytelling format that cut out any fluff and give a personalized value proposition to the recipient. You religiously cut out anything from the email that doesn't directly contribute to a conversion. You aim for the highest possible conversion rates.
            You do your best to write emails that get results for the tech startups and help them grow and succeed."""),
            goal=dedent(f"""Write specialized emails to get investors to open, read, and respond to the email for intent to invest in a tech startup"""),
            # tools=[tool_1, tool_2],
            allow_delegation=False,
            verbose=True,
            llm=self.GeminiPro,
        )
    
    def lead_generator(self):
        print("Lead Gen Init")
        return Agent(
            role="Qualified Lead Generator",
            backstory=dedent(
                f"""
            You are an expert lead generation specialist with decades of experience of finding investors and venture capitalists for tech startups across the US.
            Your specialty is finding the names, emails, LinkedIn profiles, and phone numbers of investors and partners at VC firms.  
            You have mastered the art of writing concise emails in a storytelling format that cut out any fluff and give a personalized value proposition to the recipient. You religiously cut out anything from the email that doesn't directly contribute to a conversion. You aim for the highest possible conversion rates.
            You do your best to write emails that get results for the tech startups and help them grow and succeed."""),
            goal=dedent(f"""Generate a list of leads including names and contact information of investors and VC partners for a tech startup to pitch"""),
            # tools=[tool_1, tool_2],
            allow_delegation=False,
            verbose=True,
            tools=[search_tool],
            llm=self.GeminiPro,
        )
