# import packages
import streamlit as st
from langchain_community.callbacks import StreamlitCallbackHandler
from main import get_agent_executor
from dotenv import load_dotenv
import os

load_dotenv()

# CACHE CLEANER
import atexit, os
from cache_cleaner import delete_pycache_on_exit

# Register the function to be called on program exit
atexit.register(delete_pycache_on_exit)

st.set_page_config(page_title="professor's assignment", page_icon="assets/chat.png")

# title
st.title("🦜+ 📰 : LANGCHAIN CHATBOT")

# get api keys and then initialize the agent_executor
def process_uploaded_file(uploaded_file):
    content = uploaded_file.read().decode("utf-8")
    with open(".env", "w") as env_file:
        env_file.write(content)
    st.success("File uploaded successfully.")

dot_env_file = st.sidebar.file_uploader(
    label="Upload .env file containing AZURE API and AZURE ENDPOINT",
    type=['.txt']
)

if not dot_env_file:
    st.info("Please upload .env file to continue.")
    st.stop()
else:
    process_uploaded_file(dot_env_file)

api_key = os.getenv("AZURE_OPENAI_API_KEY")
azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
agent_executor = get_agent_executor(api_key=api_key, azure_endpoint=azure_endpoint)

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []


# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        if message["role"]=="assistant":
            st.markdown(message["content"]["output"])
        else:
            st.markdown(message["content"])

# React to user input
prompt = st.chat_input("Ask me anything . . .")
if prompt:
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

try:
    with st.spinner():
        response = agent_executor.invoke({"input":prompt}, callbacks=[StreamlitCallbackHandler])
except:
    st.error("Please check you API KEY and AZURE ENDPOINT")
    st.stop()
# Display assistant response in chat message container
with st.chat_message("assistant"):
    st.markdown(response["output"])
# Add assistant response to chat history
st.session_state.messages.append({"role": "assistant", "content": response})