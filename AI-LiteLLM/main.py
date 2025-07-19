import os
from litellm import completion
from dotenv import load_dotenv
import streamlit as st

# Load API Key
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

# Page Config
st.set_page_config(page_title="AI Chatbot", page_icon="🤖", layout="centered")
st.markdown("""
    <style>
        body {
            background-color: #f4f4f4;
        }
        .stChatMessage {
            padding: 0.8rem 1rem;
            border-radius: 1rem;
            margin-bottom: 0.8rem;
            width: 100%; /* FULL WIDTH */
            max-width: 100%; /* REMOVE LIMIT */
            word-wrap: break-word;
            box-sizing: border-box;
        }
        .user-message {
            background-color: #00000;
            color:#ffffff
            align-self: flex-end;
           
        }
        .assistant-message {
    background-color: #000000;
    color: #FFFFFF; /* ADD THIS */
    align-self: flex-start;
}

        .st-emotion-cache-1kyxreq {
            padding-top: 2rem;
        }
    </style>
""", unsafe_allow_html=True)

st.title("🤖 AI Chatbot")

# Initialize Session
if "messages" not in st.session_state:
    st.session_state.messages = []

# Chat Input
user_input = st.chat_input("ask your question...")

# When user sends message
if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})

    with st.spinner("Answering..."):
        response = completion(
            model="gemini/gemini-2.0-flash",
            messages=st.session_state.messages,
            api_key=api_key,
        )
        ai_reply = response['choices'][0]['message']['content']
        st.session_state.messages.append({"role": "assistant", "content": ai_reply})

# Display messages
for message in st.session_state.messages:
    if message["role"] == "user":
        with st.chat_message("user"):
            st.markdown(f"<div class='stChatMessage user-message'>{message['content']}</div>", unsafe_allow_html=True)
    else:
        with st.chat_message("assistant"):
            st.markdown(f"<div class='stChatMessage assistant-message'>{message['content']}</div>", unsafe_allow_html=True)
