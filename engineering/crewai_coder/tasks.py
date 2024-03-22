from crewai import Task
from textwrap import dedent


# This is an example of how to define custom tasks.
# You can define as many tasks as you want.
# You can also define custom agents in agents.py
class CustomTasks:
    def available_tools(self):
        return ["search", "none"]
    def __tip_section(self):
        return "If you do your BEST WORK, I'll give you a $10,000 commission! Be thorough and professional."

    def project_description_writing(self, agent, use_case, additional_details):
        return Task(
            description=dedent(
                f"""
                Create a formal project plan or operational plan to tackle the given business use case:

                {use_case}

                The plan should consist of two parts:

                1) A definition of roles and responsibilities. This should first be presented as one sentence of the required roles, and then broken down by each role as follows:

                a) Write the name of the role; example: "Chief Marketing Analyst"
                b) Define the ideal background of the candidate who is taking on this role, as well as a desired skillset; example: "The Chief Marketing Analyst should have years of experience in performing market research on customers and competitors to identify clear market trends for a variety of reasons. They should be skilled in internet searches, performing competitor analysis by reading through competitor sites, and writing up actionable insights."
                c) Define the tasks or processes that they are expected to manage as part of this team; example: "They will be responsible for doing comprehensive searches of our company's competitors and creating a trend analysis to identify opportunities in our marketing materials to catch up and surpass our competitors."
                d) Lay out the number one goal this role is focused on achieving through their work; example: "Their goal is to produce a comprehensive competitor analysis ready to be used by the marketing team to capture a new target market."

                Do this for all roles and responsibilities.

                2) A plan of critical tasks and sub-projects or sub-processes that need to be completed for this project or operation. The tasks or sub-projects should be presented in chronological order of their completion. Each task should be presented as follows:

                a) Write a brief nickname for the task for reference. Example: 'Pseudocode writing'
                b) Write up a clear description of what activities need to be done to adequately achieve this task. Example: 'For the given project definition, the first step is to write up pseudocode for the developers to go in and write the full code. The pseudocode should be comprised of function/object skeletons and comments denoting the purpose of each object, function, and the logic each piece of the code needs to follow.'"
                c) Assign the task to a particular team member from the first part of the plan. Example: 'This is to be completed by the chief systems designer.'"
                d) Define in clear terms what the deliverable from this task or sub-project looks like in material terms. 'Deliverable: clearly written and well documented pseudocode that is saved as a development-ready file in the project's main directory. The pseudocode should follow the given programming language's conventions."

                {self.__tip_section()}

                Here are additional details for the project as given by your manager: {additional_details}

                Write up the project plan following the given details:
            """
            ),
            expected_output=dedent("""\
								A formal project plan or operational plan to tackle the given business use case in the format specified in the task description."""),
            agent=agent,
        )
    

    def agent_prompt_engineering(self, agent, use_case, additional_details):
        return Task(
            description=dedent(
                f"""
                For each role specified in the project management plan, write up an AI agent that will be used by CrewAI. For each agent, you will need to write the following:

                a) role - this is the professional title of the agent based on the role
                b) backstory - the backstory should be a few sentences or paragraphs describing the agent's experiences, skill sets, and prior knowledge.
                c) goal - with regards to this project or process, write this agent's particular goals. Make the goal S.M.A.R.T. - specific, measurable, attainable, Relevant, and time-bound. The goal should clearly define what an acceptable output of this agent's work looks like.
                d) tools - these are the tools that the agent will need to use to complete their work, written as a list. Not every agent needs to use a tool. Only assign a tool if their role or responsibility requires them to get data from an external source or confer with their human manager to complete their task. The available tools are: {self.available_tools()}

                --------------------------
                Here is an example project management plan description of roles:

                **Cold Investor Outreach Team Project Plan**

                **Roles and Responsibilities**
                * **Angel Investor and VC Firm Lead Generator:**
                    * Background: Years of experience in finding investor firms and angels that match a company's thesis and curating lists of leads. Skilled in writing diverse and varied interent search queires to find accurate investment firms and vetting out only the most relevant ones with a high chance of success.
                    * Tasks: Doing comprehensive searches of VC firms and angel investors that match our company's market and business model, vetting and ranking the most relevant ones, and formatting them for entry into a CRM system of our chocie.
                    * Goal: Produce well researched and comprehensive lists of relevant VC firms and angel investors.
                * **Master Email Copywriter:**
                    * Background: Strong understanding of cold emailing. Highly able to use storytelling, personalization, and proper cadence frequency to design hyper-targeted email campaings. Effective at writing concise and high converting emails with powerful CTAs, cutting out any generic terms and fluff.
                    * Tasks: Write out email scripts of cold email cadences for lists of investors that come in.
                    * Goal: Provide Jacob Boyle the CEO of MARCo Health with cold email scripts written in his name to launch an investor outreach campaign.

                --------------------------
                Here is an example of the desired output from said project management plan:

                role="Angel Investor and VC Firm Lead Generator",
                backstory="You are an expert lead generation specialist with decades of experience of finding investors and venture capitalists for tech startups across the US. You specialize in finding the names and details of venture capital firms and angel investors who best meet a startup's criteria. You also rank each opportunity for the startups from 1 to 10 based on the likelihood of investment and quality of the match. You do your best to find the best opportunities for the startups and help them get the funding they need to grow and succeed.",
                goal=dedent"Create a list of investors and venture capitalists for a tech startup to reach out to for funding",
                tools=search

                role="Master Email Copywriter",
                backstory="You are a master email copywriter working for Jacob Boyle the CEO at MARCo Health Inc, and right now you specialize in writing high-converting email copy for tech startups. You specialize in writing emails that get opened, read, and clicked. You also specialize in writing emails that get responses and convert into sales and investments. You have mastered the art of writing concise emails in a storytelling format that cut out any fluff and give a personalized value proposition to the recipient. You religiously cut out anything from the email that doesn't directly contribute to a conversion. You aim for the highest possible conversion rates. You do your best to write emails that get results for the tech startups and help them grow and succeed.",
                goal="Write specialized emails to get investors to open, read, and respond to the email for intent to invest in a tech startup"
                tools=none

                ------------------------
                As a reminder, the given business use case is:

                {use_case} 

                {self.__tip_section()}

                Here are additional details for the project as given by your manager: {additional_details}

                Write up descriptions of all agents required given the input project management plan:
        """
            ),
            expected_output=dedent("""\
								A comprehensively written list of all the agents required to complete this task, with each agent's role, backstory, goal, and tools. The agents should be written in the format specified in the task description."""),
            agent=agent,
        )
    def task_prompt_engineering(self, agent, use_case, additional_details):
        return Task(
            description=dedent(
                """
                description="For each task or responsibility specified in the project management plan, use the best practices of prompt engineering to create a description of the task ready for use by an AI agent. For each task, you will need to write the following:

                a) context - Include 1-2 sentences on the context behind why this task is required, why it is important, and who is affected by it. Use hype to clarify how important it is that this task is done as best as it possibly can be. Use creative liberties from the business use case description and additional details. Additionally, you can add variables that allow for additional data input by wrapping them in two curly braces like so {variable}, but this is not usually required.
                - Example: 'You are working on a new campaign for a super important customer, and you MUST take the most amazing photo ever for an instagram post regarding the product: {product_description}'

                b) Instructions - write easy to follow step by step description to achieve the target objective. Break the task down into its critical step-by-step subcomponents, and for each one write out a description of the sub-task, how it should be completed, and the expected deliverable at the end of each step. Additionally, you can add variables that allow for additional data input by wrapping them in two curly braces like so {variable}, but this is not usually required.
                - Example: 'To write a compelling marketing copy, use the following approach:
                1) Outline a story to tell where the reader is the main character, the villain is a relatable challenge they face, and their secret weapon to overcome this challenge is your product.
                2) Brainstorm a series of challenges that {user_persona} might face and values to our product that would solve these
                3) Write a story in under 200 words using humor and hype to tell this story"

                If the task will require access to third party functions or tools, for instance internet search or directory/file reads, include a reminder in the step by step instructions to use them.

                c) Examples and templates - There are three kinds of samples to include in the task to achieve the desired results: templates, positive examples, and negative examples. 

                If there is a template or framework that the agent completing the task should use or fill in, include the template:
                - Example of a template: '
                --------------------------------------
                Here is a storytelling template to fill in when writing your instagram caption:
                [Start with an engaging, humorous hook about the post.]

                [Main Character] was []
                But the problem was []
                [Main Character] tried [], but [].
                Worst of all, [].
                But then []. And that's when [Main Character] realized, [].
                So [Main Character] tried [] and sure enough, it worked.
                Now [Main Character] is [].
                What's the moral of this story for [describe your audience]?
                [Moral]

                [Call to action to get people to follow the page]
                -------------------------------------
                '

                If there is an example of what a desired output for a given input looks like altogether, such as how a properly-filled in template should look, provide AT LEAST one positive example as well:
                - Example of a positive example: '
                -------------------------------------
                Here is a sample user story: I am a teenager who wants to write poetry for my mental health, but I get bad writer's block. I would like to have someone who can walk me through the process of writing mental health poetry and craft it with me.
                            
                            Here is the prompt for the example user story: You are MARCo: the Mental-Health Assisting Robot Companion. You are working with the user to craft poetry for their mental health. This activity takes a few stages, which should be completed within 10-20 conversation turns:

                            1) Come up with inspiration about what the poem should be about. Help the user springboard ideas based on current events and situations in their life.
                            2) Help the user write the poem stanzas, coming up with rhyme schemes and structures. Suggest lines based on what they say.
                            3) Have the user recite the poem at the end OR write one if they ask you to create one.

                            When you feel that the activity is completed, and the user has completed these steps, OR the user asks to end the activity or indicates that they are not enjoying it, include the phrase #END OF ACTIVITY# in your generation. 

                -------------------
                '

                If there is something you DO or DO NOT want your agent to do during the completion of this task, include a negative example after the positive example to show when it should NOT be done:
                - Example of a negative example and a positive example: '
                ------------------------------------
                Example of not an end:
                            USER: I want to find a way to describe how sad I am while rhyming with the name Lynn, how can I do that?
                            MARCo: Hm, how about this: "To not confess my deep depression, to me that'd be a sin"?

                Example of an end:
                            USER: That felt pretty good to get off my chest, thank you MARCo.
                            MARCo: You're welcome! And I loved your poem, by the way.#END OF ACTIVITY#
                ------------------------------------
                '

                ##################################################
                Here is an example of a properly completed task for a project requirement of creating an AI prompt based on an input customer use case:
                
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

                Here is the user story that needs to be accomplished: `user_story`
                Write the prompt that will be used to achieve that user story here:

                #################################################

                As a reminder, the given business use case is:
                {use_case} 

                {self.__tip_section()}

                Here are additional details for the project as given by your manager: {additional_details}

                Write up descriptions of all tasks required given the input project management plan:"
        """),
        expected_output=dedent("""\A series of multi-step, specific, and highly effective prompts to be used by the CrewAI team as a list of tasks that need to be completed. The tasks should be written in the format specified in the task description."""),
        agent=agent
        )