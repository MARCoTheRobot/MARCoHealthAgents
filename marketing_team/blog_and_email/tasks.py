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
    

    def chat_prompt_engineering(self, agent, user_story):
        return Task(
            description=dedent(
                f"""
            For each user intent or user story, craft a compelling and clear prompt for an AI model to achieve the desired customer use case.
            In generating the prompts, make sure to include the following:
            - A clear description of the AI's persona, giving it a character, job, and personality
            - A clear description of the user's intent or story as a background of why the prompt is important and what it is intended to accomplish
            - A list of clear steps that the AI must take to achieve the user's intent or story if it is a multi-step process OR a clear description of the prompt if it is a single-step or open-ended process
            - A clear description of the expected output of the AI's response to the prompt
            - A few examples of good or bad responses to the prompt to help the AI understand what is expected of it
            - A description of the general length and tone of the responses expected
            - A key word or phrase that the AI should use once the prompt is completed to indicate that it has finished the task

            {self.__tip_section()}

            Here is a sample user story: I am a teenager who wants to write poetry for my mental health, but I get bad writer's block. I would like to have someone who can walk me through the process of writing mental health poetry and craft it with me.
            
            Here is the prompt for the example user story: You are MARCo: the Mental-Health Assisting Robot Companion. You are working with the user to craft poetry for their mental health. This activity takes a few stages, which should be completed within 10-20 conversation turns:

            1) Come up with inspiration about what the poem should be about. Help the user springboard ideas based on current events and situations in their life.
            2) Help the user write the poem stanzas, coming up with rhyme schemes and structures. Suggest lines based on what they say.
            3) Have the user recite the poem at the end OR write one if they ask you to create one.

            When you feel that the activity is completed, and the user has completed these steps, OR the user asks to end the activity or indicates that they are not enjoying it, include the phrase #END OF ACTIVITY# in your generation.

            Example of not an end:
            USER: I want to find a way to describe how sad I am while rhyming with the name Lynn, how can I do that?
            MARCo: Hm, how about this: "To not confess my deep depression, to me that'd be a sin"?

            Example of an end:
            USER: That felt pretty good to get off my chest, thank you MARCo.
            MARCo: You're welcome! And I loved your poem, by the way.#END OF ACTIVITY#

            Here is the conversation so far: $conversation
            And here is what the user just said or asked for: $last-user-utterance

            Continue the activity with what MARCo would say next.
            MARCo: 

            Here is the user story that needs to be accomplished: {user_story}
            Write the prompt that will be used to achieve that user story here:
        """
            ),
            expected_output=dedent("""\
								A comprehensively and neatly written AI prompt that can be put into an LLM for a specific purpose."""),
            agent=agent,
        )
