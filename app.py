import streamlit as st
import requests
from langchain.llms import Ollama

st.header("Coding assistant")

if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {
            "role": "assistant",
            "content": "How can I help you?"
        }]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input():
    st.session_state.messages.append(
            {
                "role": "user",
                "content": prompt
            })
    st.chat_message("user").write(prompt)

    llm = Ollama(model="codellama:13b-instruct")
    res = llm.predict(prompt)
    message = {
            "role": "assistant",
            "content": res
        }
    st.session_state.messages.append(message)
    st.chat_message("assistant").write(message["content"])
