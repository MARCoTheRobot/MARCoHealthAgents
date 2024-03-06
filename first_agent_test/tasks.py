from crewai import Task
from textwrap import dedent


# This is an example of how to define custom tasks.
# You can define as many tasks as you want.
# You can also define custom agents in agents.py
class CustomTasks:
    def __tip_section(self):
        return "If you do your BEST WORK, I'll give you a $10,000 commission!"

    def story_writing(self, agent):
        return Task(
            description=dedent(
                f"""
            Write a user story for a teenager approaching the app for the first time who is in the middle of a panic attack.
            
            {self.__tip_section()}
    
           Write the story in the format of 'I'm a teenager who is all alone at school, and I need help with...'.
           Consider the details of their setting, what they're feeling, and what they need to feel better. Think also about timing and location.
        """
            ),
            expected_output=dedent("""\
								A user story following the template 'I'm a teenager who is all alone at school, and I need help with...'"""),
            agent=agent,
        )

    def project_writing(self, agent):
        return Task(
            description=dedent(
                f"""
            Take the input from the user story and write a project requirement for a software sprint.
                                       
            {self.__tip_section()}

            Write it out in sections, including the user story, acceptance criteria, and any other details that you think are important. 
            Write out a delegation plan of who needs to take on what critical tasks, and give an estimate of time to completion.
        """
            ),
            expected_output=dedent("""\
								A comprehensive project management plan with sections for each step, including a delegation plan and time estimates'"""),
            agent=agent,
        )
