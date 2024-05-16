from crewai import Task
from textwrap import dedent


# This is an example of how to define custom tasks.
# You can define as many tasks as you want.
# You can also define custom agents in agents.py
class TestTasks:
    def available_tools(self):
        return ["search", "none"]
    def __tip_section(self):
        return "If you do your BEST WORK, I'll give you a $10,000 commission! Be thorough and professional."

    def test_requirement_writeup(self, agent, use_case, additional_details):
        return Task(
            description=dedent(
                f"""
                **Task 1: Gather and Analyze Project Requirements**

                **Context:**

                To ensure the successful execution of the Selenium test case generation project, it is crucial to gather and thoroughly analyze the project requirements. This task is of utmost importance as it lays the foundation for the entire project and helps define its scope, objectives, and deliverables.

                **Instructions:**

                1. **Conduct stakeholder interviews:** This task is already completed. The stakeholder interviews revealed that the use case you are developing for is as follows: {use_case} {additional_details}

                2. **Review project documentation:** Carefully examine all relevant project documentation, such as the project charter, scope statement, requirements document, and user stories, to supplement the information obtained from stakeholder interviews.

                3. **Analyze and prioritize requirements:** Consolidate the requirements gathered from stakeholders and project documentation. Categorize and prioritize them based on their importance, urgency, and potential impact on the project's success.

                4. **Develop a requirements traceability matrix (RTM):** Create an RTM to establish a direct link between the project requirements and the test cases that will be developed. This matrix ensures that each requirement is accounted for and tested.

                5. **Present requirements to team:** Present the analyzed and prioritized requirements to the project team to ensure a shared understanding of the project's objectives and deliverables. Secure team buy-in and address any questions or concerns.

                **Examples and Templates:**

                * **Example of Requirements Traceability Matrix:**

                | Requirement ID | Requirement Description | Test Case ID | Test Case Description | Status |
                |---|---|---|---|---|
                | REQ-01 | User should be able to create a new account | TC-01 | Verify user can successfully create an account | Pass |
                | REQ-02 | System should generate a welcome email after account creation | TC-02 | Verify welcome email is sent upon account creation | Fail |

                {self.__tip_section()}

                Write up a detailed test requirement writeup for the given business use case:
            """
            ),
            expected_output=dedent("""\
								A requirement matrix that includes all the requirements gathered from stakeholders and project documentation, categorized, prioritized, and presented to the project team. The matrix should establish a clear link between the project requirements and the test cases that will be developed."""), # @Prabhat: This is the expected output that the AI-generated response should match.
            agent=agent,
            output_file="outputs/requirement_matrix.md" # @Prabhat: If you just need to quickly save an output after a task is completed, you can use this parameter to specify the file path where the output should be saved.
        )
    

    def test_writeup(self, agent, language, code_directory):
        return Task(
            description=dedent(
                f"""
                **Task 2: Design and Develop Selenium Test Cases**

                **Context:**

                The development of high-quality Selenium test cases is essential to ensure the effectiveness of the testing process. This task involves designing, coding, and executing test cases using the Selenium framework.

                **Instructions:**

                1. **Design test cases:** Design test cases that cover various scenarios and conditions to thoroughly test the software functionality. Consider different user roles, inputs, and possible outcomes. Use the information provided by the last agent to create the test cases.

                2. **Develop Selenium code:** Implement the test cases using the Selenium framework. Use the {language} programming languages and techniques to create robust and maintainable code. Reference the project documentation and source code found in the {code_directory} directory and all subdirectories for creating your test cases.

                The output should be the code with appropriate comments that can be directly imported for execution in the Selenium framework.
        """
            ),
            expected_output=dedent("""\
								A comprehensively written list of all the agents required to complete this task, with each agent's role, backstory, goal, and tools. The agents should be written in the format specified in the task description."""),
            agent=agent,
            output_file="outputs/test_cases.txt"
        )
    
    # def task_prompt_engineering(self, agent, use_case, additional_details):
    #     return Task(
    #         description=dedent(
    #             """
    #             description="For each task or responsibility specified in the project management plan, use the best practices of prompt engineering to create a description of the task ready for use by an AI agent. For each task, you will need to write the following:

    #             a) context - Include 1-2 sentences on the context behind why this task is required, why it is important, and who is affected by it. Use hype to clarify how important it is that this task is done as best as it possibly can be. Use creative liberties from the business use case description and additional details. Additionally, you can add variables that allow for additional data input by wrapping them in two curly braces like so {variable}, but this is not usually required.
    #             - Example: 'You are working on a new campaign for a super important customer, and you MUST take the most amazing photo ever for an instagram post regarding the product: {product_description}'

    #             b) Instructions - write easy to follow step by step description to achieve the target objective. Break the task down into its critical step-by-step subcomponents, and for each one write out a description of the sub-task, how it should be completed, and the expected deliverable at the end of each step. Additionally, you can add variables that allow for additional data input by wrapping them in two curly braces like so {variable}, but this is not usually required.
    #             - Example: 'To write a compelling marketing copy, use the following approach:
    #             1) Outline a story to tell where the reader is the main character, the villain is a relatable challenge they face, and their secret weapon to overcome this challenge is your product.
    #             2) Brainstorm a series of challenges that {user_persona} might face and values to our product that would solve these
    #             3) Write a story in under 200 words using humor and hype to tell this story"

    #             If the task will require access to third party functions or tools, for instance internet search or directory/file reads, include a reminder in the step by step instructions to use them.

    #             c) Examples and templates - There are three kinds of samples to include in the task to achieve the desired results: templates, positive examples, and negative examples. 

    #             If there is a template or framework that the agent completing the task should use or fill in, include the template:
    #             - Example of a template: '
    #             --------------------------------------
    #             Here is a storytelling template to fill in when writing your instagram caption:
    #             [Start with an engaging, humorous hook about the post.]

    #             [Main Character] was []
    #             But the problem was []
    #             [Main Character] tried [], but [].
    #             Worst of all, [].
    #             But then []. And that's when [Main Character] realized, [].
    #             So [Main Character] tried [] and sure enough, it worked.
    #             Now [Main Character] is [].
    #             What's the moral of this story for [describe your audience]?
    #             [Moral]

    #             [Call to action to get people to follow the page]
    #             -------------------------------------
    #             '

    #             If there is an example of what a desired output for a given input looks like altogether, such as how a properly-filled in template should look, provide AT LEAST one positive example as well:
    #             - Example of a positive example: '
    #             -------------------------------------
    #             Here is a sample user story: I am a teenager who wants to write poetry for my mental health, but I get bad writer's block. I would like to have someone who can walk me through the process of writing mental health poetry and craft it with me.
                            
    #                         Here is the prompt for the example user story: You are MARCo: the Mental-Health Assisting Robot Companion. You are working with the user to craft poetry for their mental health. This activity takes a few stages, which should be completed within 10-20 conversation turns:

    #                         1) Come up with inspiration about what the poem should be about. Help the user springboard ideas based on current events and situations in their life.
    #                         2) Help the user write the poem stanzas, coming up with rhyme schemes and structures. Suggest lines based on what they say.
    #                         3) Have the user recite the poem at the end OR write one if they ask you to create one.

    #                         When you feel that the activity is completed, and the user has completed these steps, OR the user asks to end the activity or indicates that they are not enjoying it, include the phrase #END OF ACTIVITY# in your generation. 

    #             -------------------
    #             '

    #             If there is something you DO or DO NOT want your agent to do during the completion of this task, include a negative example after the positive example to show when it should NOT be done:
    #             - Example of a negative example and a positive example: '
    #             ------------------------------------
    #             Example of not an end:
    #                         USER: I want to find a way to describe how sad I am while rhyming with the name Lynn, how can I do that?
    #                         MARCo: Hm, how about this: "To not confess my deep depression, to me that'd be a sin"?

    #             Example of an end:
    #                         USER: That felt pretty good to get off my chest, thank you MARCo.
    #                         MARCo: You're welcome! And I loved your poem, by the way.#END OF ACTIVITY#
    #             ------------------------------------
    #             '

    #             ##################################################
    #             Here is an example of a properly completed task for a project requirement of creating an AI prompt based on an input customer use case:
                
    #             For each user intent or user story, craft a compelling and clear prompt for an AI model to achieve the desired customer use case.
    #             In generating the prompts, make sure to include the following:
    #             - A clear description of the AI's persona, giving it a character, job, and personality
    #             - A clear description of the user's intent or story as a background of why the prompt is important and what it is intended to accomplish
    #             - A list of clear steps that the AI must take to achieve the user's intent or story if it is a multi-step process OR a clear description of the prompt if it is a single-step or open-ended process
    #             - A clear description of the expected output of the AI's response to the prompt
    #             - A few examples of good or bad responses to the prompt to help the AI understand what is expected of it
    #             - A description of the general length and tone of the responses expected
    #             - A key word or phrase that the AI should use once the prompt is completed to indicate that it has finished the task

    #             {self.__tip_section()}

    #             Here is a sample user story: I am a teenager who wants to write poetry for my mental health, but I get bad writer's block. I would like to have someone who can walk me through the process of writing mental health poetry and craft it with me.
                
    #             Here is the prompt for the example user story: You are MARCo: the Mental-Health Assisting Robot Companion. You are working with the user to craft poetry for their mental health. This activity takes a few stages, which should be completed within 10-20 conversation turns:

    #             1) Come up with inspiration about what the poem should be about. Help the user springboard ideas based on current events and situations in their life.
    #             2) Help the user write the poem stanzas, coming up with rhyme schemes and structures. Suggest lines based on what they say.
    #             3) Have the user recite the poem at the end OR write one if they ask you to create one.

    #             When you feel that the activity is completed, and the user has completed these steps, OR the user asks to end the activity or indicates that they are not enjoying it, include the phrase #END OF ACTIVITY# in your generation.

    #             Example of not an end:
    #             USER: I want to find a way to describe how sad I am while rhyming with the name Lynn, how can I do that?
    #             MARCo: Hm, how about this: "To not confess my deep depression, to me that'd be a sin"?

    #             Example of an end:
    #             USER: That felt pretty good to get off my chest, thank you MARCo.
    #             MARCo: You're welcome! And I loved your poem, by the way.#END OF ACTIVITY#

    #             Here is the conversation so far: $conversation
    #             And here is what the user just said or asked for: $last-user-utterance

    #             Continue the activity with what MARCo would say next.
    #             MARCo: 

    #             Here is the user story that needs to be accomplished: `user_story`
    #             Write the prompt that will be used to achieve that user story here:

    #             #################################################

    #             As a reminder, the given business use case is:
    #             {use_case} 

    #             {self.__tip_section()}

    #             Here are additional details for the project as given by your manager: {additional_details}

    #             Write up descriptions of all tasks required given the input project management plan:"
    #     """),
    #     expected_output=dedent("""\A series of multi-step, specific, and highly effective prompts to be used by the CrewAI team as a list of tasks that need to be completed. The tasks should be written in the format specified in the task description."""),
    #     agent=agent
    #     )
    # def generate_agent_function(self, agent_name, role, backstory, goal, llm_model):
    #     """
    #     Generate Python code for creating an agent function based on the provided description.
    #     """
    #     agent_function_template = f"""
    #     \tdef {agent_name}(self):
    #     \t\treturn Agent(
    #             role="{role}",
    #             backstory=dedent(\"\"\"{backstory}\"\"\"),
    #             goal=dedent(\"\"\"{goal}\"\"\"),
    #             # tools=[tool_1, tool_2],
    #             allow_delegation=False,
    #             verbose=True,
    #             llm=self.OpenAIGPT35,
    #         \t)
    #     """
    #     return agent_function_template

    # def agent_generation_callback(self, agent_data_raw):
        # Convert agent_data_raw to a string
        agent_data = agent_data_raw.raw_output.strip().split("\n\n")  # Split by empty lines

        generated_functions = []
        # @Prabhat - We should have some flexibility to change between different AI models. Especially considering, internally, we are only using Gemini at this time. Or at least set that as the default but import the others in case.
        agent_start_code = f"""from crewai import Agent\nfrom textwrap import dedent\nfrom langchain_community.llms import OpenAI\nfrom langchain_community.llms import Ollama\nfrom langchain_openai import ChatOpenAI
    # This is an example of how to define custom agents.\n# You can define as many agents as you want.\n# You can also define custom tasks in tasks.py
    \nclass CustomAgents:\n\tdef __init__(self):\n\t\tself.OpenAIGPT35 = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.7)\n\t\tself.OpenAIGPT4 = ChatOpenAI(model_name="gpt-4", temperature=0.7)\n\t\tself.Ollama = Ollama(model="openhermes") 
            """
        generated_functions.append(agent_start_code)

        for i, agent_str in enumerate(agent_data, 1):
            agent_info = agent_str.strip().split("\n")
            agent_name = f"agent_{i}_name"
            role = agent_info[0].split("=")[1].strip().strip('",')
            backstory = agent_info[1].split("=")[1].strip().strip('",')
            goal = agent_info[2].split("=")[1].strip().strip('",')
            tools = agent_info[3].split("=")[1].strip()

            agent_function_code = self.generate_agent_function(agent_name, role, backstory, goal, tools)
            generated_functions.append(agent_function_code)

        output_file_path = "outputs/agents.py"

        lines_written = 0
        with open(output_file_path, "w") as f:
            for function_code in generated_functions:
                f.write(function_code)
                f.write("\n\n")  # Add some space between each function
                lines_written += function_code.count("\n")
                if lines_written >= 15:
                    f.write("\n")  # Add an extra line after every 15 lines
                    lines_written = 0

        print("\nAgent functions have been written to the output file.")