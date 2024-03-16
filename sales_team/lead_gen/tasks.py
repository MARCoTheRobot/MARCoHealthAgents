from crewai import Task
from textwrap import dedent


# This is an example of how to define custom tasks.
# You can define as many tasks as you want.
# You can also define custom agents in agents.py
class CustomTasks:
    def __tip_section(self):
        return "If you do your BEST WORK, I'll give you a $10,000 commission! Be thorough and professional."

    def firm_lead_generation(self, agent, company_name, company_description, company_stage):
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
								A CSV list of 10 investment firms formatted with the following headers: Investment Firm Name, Notes, Website, General Email, Application Link (Optional), Location, Stages of Investment, Portfolio Companies, Average Investment Size, Thesis, Contact Information'"""),
            agent=agent,
        )
    
    def lead_generation(self, agent):
        return Task(
            description=dedent(
                f"""
            Based on a list of investors provided from the first step in the process, find the names, emails, LinkedIn profiles, and phone numbers of investors and partners at VC firms and organize them into a list.
            
            {self.__tip_section()}
        
            Make sure to use the most recent data as possible from the internet.
        """
            ),
            expected_output=dedent("""\
                                A CSV list of investor names and contact information formatted with the following headers: Name, first_name, last_name, Email, LinkedIn, Phone Number, Bio'"""),
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
