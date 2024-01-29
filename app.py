# import packages
import streamlit as st
from langchain_community.callbacks import StreamlitCallbackHandler
from main import get_agent_executor

# CACHE CLEANER
import atexit, os
from cache_cleaner import delete_pycache_on_exit

# Register the function to be called on program exit
atexit.register(delete_pycache_on_exit)

st.set_page_config(page_title="professor's assignment", page_icon="assets/chat.png")

# title
st.title("🦜+ 📰 : LANGCHAIN CHATBOT")

# get api keys and then initialize the agent_executor
agent_executor = get_agent_executor()

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


with st.spinner():
    response = agent_executor.invoke({"input":prompt}, callbacks=[StreamlitCallbackHandler])

# Display assistant response in chat message container
with st.chat_message("assistant"):
    st.markdown(response["output"])
# Add assistant response to chat history
st.session_state.messages.append({"role": "assistant", "content": response})