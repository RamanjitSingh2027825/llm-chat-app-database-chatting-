# import packages
import json
import sqlite3

# databaseDescription function
def describe_database(none):
    path = "database\\databaseDescription.json"
    with open(path, "r") as file:
        return json.load(file)

# databaseTableDescription function
def describe_table(table_name):
    path = "database\\databaseTableDescription.json"
    with open(path, "r") as file:
        database_description = json.load(file)

    # Finding the specified table in the database description
    for table in database_description["Tables"]:
        if table["Table Name"] == table_name:
            return {
                "Table Name": table["Table Name"],
                "Description": table["Description"]
            }

    # Return None if the specified table is not found
    return None

# run_query_tool Function
def run_sqlite_query(query : str):
    """Takes an SQL query and returns result"""

    connection = sqlite3.connect("database\\project2.db")

    cursor = connection.cursor()
    try:
        cursor.execute(query)
        return cursor.fetchall()
    except sqlite3.OperationalError as err:
        return f"{err} : Error Occured !"