from crewai import Task
from textwrap import dedent
import os

def generate_task_function(task_name, var_details):
    """
    Generates a Python function string for a task based on its details.
    """
    # For tasks with two variables, format the task function accordingly
    if len(var_details) == 2:
        return f'''
    def {task_name}(self, agent, {var_details[0]}, {var_details[1]}):
        return Task(
            description=dedent(
                f"""
                Perform an action as part of {task_name}
                
                {{self.__tip_section()}}
        
                Ensure to use the most recent data as possible.
        
                Utilize this variable: {{{var_details[0]}}}
                And also this variable: {{{var_details[1]}}}
                """
            ),
            agent=agent,
        )
        '''
    else:
        # For tasks without variables, format the task function differently
        return f'''
    def {task_name}(self, agent):
        return Task(
            description=dedent(
                f"""
                Take the input from the previous task and execute an operation.
                                           
                {{self.__tip_section()}}

                Ensure to perform an additional action.
                """
            ),
            agent=agent,
        )
        '''

def main():
    input_file_path = "tasks.txt"

    try:
        with open(input_file_path, "r") as file:
            task_data = file.read().strip().split("\\n\\n")  # Split by empty lines
    except FileNotFoundError:
        print("Error: tasks.txt file not found.")
        return

    generated_functions = []
    task_start_code = '''
from crewai import Task
from textwrap import dedent

# This is an example of how to define custom tasks.
# You can define as many tasks as you want.
# You can also define custom agents in agents.py

class CustomTasks:
    def __tip_section(self):
        return "If you do your BEST WORK, I'll give you a $10,000 commission!"
    '''
    generated_functions.append(task_start_code)

    for i, task_str in enumerate(task_data, 1):
        task_details = task_str.strip().split("\\n")
        task_name = f"task_{i}_name"
        var_details = [var.strip() for var in task_details[1:]]

        task_function_code = generate_task_function(task_name, var_details)
        generated_functions.append(task_function_code)

    output_file_path = "outputs/tasks.py"

    os.makedirs(os.path.dirname(output_file_path), exist_ok=True)

    with open(output_file_path, "w") as f:
        for function_code in generated_functions:
            f.write(function_code)
            f.write("\\n\\n")  # Add some space between each function

    print("\\nTask functions have been written to the output file.")

if __name__ == "__main__":
    main()
