from crewai import Task
from textwrap import dedent


# This is an example of how to define custom tasks.
# You can define as many tasks as you want.
# You can also define custom agents in agents.py
class CustomTasks:
    def __tip_section(self):
        return "If you do your BEST WORK, I'll give you a $10,000 commission! Be thorough and professional."

    def lead_generation(self, agent, company_name, company_description, company_stage):
        return Task(
            description=dedent(
                f"""
            Collect and organize a list of 10 investment firms who are interested in early stage mental health technology startups. Pay special attention to the details of each lead, including their contact information, investment history, portfolio companies, average investment size, thesis, and any other relevant details.

            The company you are trying to find matching investors for is called {company_name}. It is a company best described as: {company_description}. It is a {company_stage} stage company.
            
            {self.__tip_section()}
        
            Make sure to use the most recent data as possible from the internet.
        """
            ),
            expected_output=dedent("""\
								A CSV list of 10 investment firms with detailed information about each firm's investment history, portfolio companies, average investment size, thesis, and contact information'"""),
            agent=agent,
        )

    def email_copywriting(self, agent, company_name, company_description, raise_target):
        return Task(
            description=dedent(
                f"""
            Take the input from a list of 10 investment firms and write a personalized email to each firm, introducing the company {company_name} and asking for a meeting to discuss a potential investment. Write a compelling subject line, personalized body with a compelling pitch for {company_name} that highlights the following:
            - the company's mission and vision, {company_description}
            - the company's traction and progress to date
            - the company's financial projections and the amount of money you are trying to raise, {raise_target}
            - a clear call to action to set up a meeting.
                                       
            {self.__tip_section()}
        """
            ),
            expected_output=dedent("""\
								A text list of 10 personalized emails, each with a compelling subject line, personalized body, and a clear call to action to set up a meeting."""),
            agent=agent,
        )
