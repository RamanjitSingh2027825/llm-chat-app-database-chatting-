# import packages
import sqlite3
from langchain.tools import Tool
from pydantic.v1 import BaseModel
from typing import List
from tools.functions import describe_database,describe_table,run_sqlite_query

# database connection
connection = sqlite3.connect("database\\project2.db")

# Tool : describe_database_tool
describe_database_tool = Tool.from_function(
    name="describe_database",
    description='''Retrieves and summarizes the structure and details of a database 
    based on a JSON representation. Useful when exploring the database 
    schema.''',
    func=describe_database
)

# Tool : describe_table_tool
class DescribeTableArgsSchema(BaseModel):
    table_name: str

describe_table_tool = Tool.from_function(
    name="describe_table",
    description='''Retrieves and summarizes the structure and details of a specific table 
    in a database based on its name and a JSON representation. 
    Useful when exploring or documenting individual table schemas.
    ''',
    func=describe_table,
    args_schema=DescribeTableArgsSchema
)

# Tool : run_query_tool
class RunQueryArgsSchema(BaseModel):
    query : str

# create run_query_tool
run_query_tool = Tool.from_function(
    name="run_sqlite_query",
    description="useful when running a sqlite query",
    func=run_sqlite_query,
    args_schema=RunQueryArgsSchema
)