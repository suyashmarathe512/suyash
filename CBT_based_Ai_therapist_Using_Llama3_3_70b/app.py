import streamlit as st
import requests

def generate_response(prompt, api_url="http://localhost:11434/api/generate", model="llama3.3"):
    payload = {
        "model": model,
        "prompt": prompt,
        "max_tokens": 512,
        "temperature": 0.7
    }
    try:
        response = requests.post(api_url, json=payload)
        response.raise_for_status()
        return response.json().get("text", "Error: No response text.")
    except Exception as e:
        return f"Error contacting model API: {e}"

# Streamlit App
st.set_page_config(page_title="AI Therapist Chatbot", page_icon=":brain:")
st.title("🧠 CBT AI Therapist Chatbot")

# Session state for conversation
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display conversation
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.chat_message("user").write(msg["content"])
    else:
        st.chat_message("assistant").write(msg["content"])

# User input
user_input = st.chat_input("You: ")
if user_input:
    # Add user message
    st.session_state.messages.append({"role": "user", "content": user_input})
    # Generate model response
    with st.spinner("Therapist is thinking..."):
        bot_response = generate_response(user_input)
    # Add assistant message
    st.session_state.messages.append({"role": "assistant", "content": bot_response})
    # Rerun to display
    st.experimental_rerun()
