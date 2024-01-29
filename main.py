# import packages
from langchain_openai.chat_models.azure import AzureChatOpenAI
from langchain.prompts import ChatPromptTemplate
from tools.sql import describe_database_tool, describe_table_tool, run_query_tool
from langchain_core.prompts import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    MessagesPlaceholder
)
from langchain.memory import ConversationBufferMemory
from langchain.schema import SystemMessage
from langchain.agents import create_openai_functions_agent, AgentExecutor
from dotenv import load_dotenv

# create get_agent_executor function
def get_agent_executor():
    llm = AzureChatOpenAI(
        openai_api_version = "2023-09-01-preview",
        azure_deployment= "gpt-35-turbo-16k",
        model_name="gpt-35-turbo-16k",
    )

    # tool
    tools = [describe_table_tool, run_query_tool]

    # prompt
    system_message = SystemMessage(
        content=f'''You are an AI with access to 'describe_table_tool' for exploring SQLite database structures and 'run_query_tool' for executing queries. Your task is to formulate an SQLite query based on the information obtained from exploring specific tables. The relevant tables for this scenario are 'Marks,' 'Professors,' 'Subjects,' 'ProfessorSubjects,' and 'WeeklySchedule.'

    Follow these steps in your plan:
    1. Break down the problem into step-by-step solving:

    Then follow this Algorithm in the same way:
    1. Utilize 'describe_table_tool' to retrieve detailed information about the 'Marks' table. Understand its column names, data types, and potential relationships.
    2. Explore the 'Professors' table using 'describe_table_tool.' Gather information about its structure, including column names, data types, and any foreign key relationships.
    3. Investigate the 'Subjects' table using 'describe_table_tool' to understand its columns, data types, and potential connections with other tables.
    4. Examine the 'ProfessorSubjects' table with 'describe_table_tool,' focusing on its columns, data types, and foreign key relationships.
    5. Lastly, explore the 'WeeklySchedule' table using 'describe_table_tool.' Understand its structure, including column names, data types, and potential relationships.

    Based on the insights obtained from exploring these tables, formulate a syntactically correct SQLite query.
    6. Use 'run_query_tool' to execute the formulated query.

    Ensure each step in the solution aligns with the details obtained from 'describe_table_tool' and the formulated query.

    Your final output should include both the SQLite query and the results obtained from executing the query using 'run_query_tool.' Provide a clear and concise explanation of how the information gathered influenced the construction of your query and how the complex problem was broken down and solved step-by-step.
    '''
    )

    human_message_prompt = HumanMessagePromptTemplate.from_template(
        template="{input}"
    )

    prompt = ChatPromptTemplate(
        messages=[
            system_message,
            MessagesPlaceholder(variable_name="chat_history"),
            human_message_prompt,
            MessagesPlaceholder(variable_name="agent_scratchpad")
        ]
    )

    # create memory
    memory = ConversationBufferMemory(memory_key="chat_history",return_messages=True)

    # create agent
    agent = create_openai_functions_agent(
        llm=llm,
        tools=tools,
        prompt=prompt
    )

    # create agent executor
    agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True, memory=memory)

    return agent_executor