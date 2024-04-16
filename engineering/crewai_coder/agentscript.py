from textwrap import dedent

def generate_agent_function(agent_name, role, backstory, goal, llm_model):
    """
    Generate Python code for creating an agent function based on the provided description.
    """
    agent_function_template = f"""
\tdef {agent_name}(self):
\t\treturn Agent(
        role="{role}",
        backstory=dedent(\"\"\"{backstory}\"\"\"),
        goal=dedent(\"\"\"{goal}\"\"\"),
        # tools=[tool_1, tool_2],
        allow_delegation=False,
        verbose=True,
        llm=self.OpenAIGPT35,
    \t)
"""
    return agent_function_template

def main():
    input_file_path = "agent_engineer_output.txt"  # Assuming the file is in the same directory as the script

    try:
        with open(input_file_path, "r") as f:
            agent_data = f.read().strip().split("\n\n")  # Split by empty lines
    except FileNotFoundError:
        print("Error: Agents.txt file not found.")
        return

    generated_functions = []
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

        agent_function_code = generate_agent_function(agent_name, role, backstory, goal, tools)
        generated_functions.append(agent_function_code)

    output_file_path = "agentworkingfinal.py"

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

if __name__ == "__main__":
    main()
