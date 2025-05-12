import streamlit as st
import requests
import joblib

# ========== CONFIG ==========
st.set_page_config(page_title="CBT AI Therapist", page_icon="🧠", layout="centered")

# ========== SIDEBAR ==========
with st.sidebar:
    st.image("assets/logo.png", width=150)
    st.markdown("### 🧠 AI CBT Therapist")
    st.markdown("#### Models in Use:")
    st.markdown("- 🧩 LLaMA 3.3 via Ollama")
    st.markdown("- 💬 SVC Sentiment Classifier")
    st.markdown("---")
    st.info("Feel safe to talk. This app does **not store** your data.")

# ========== LOAD SENTIMENT MODEL ==========
@st.cache_resource
def load_sentiment_model():
    return joblib.load("sentiment_svc_model.joblib")  # Replace with your model filename

sentiment_model = load_sentiment_model()

def predict_sentiment(text):
    return sentiment_model.predict([text])[0]

# ========== GENERATE RESPONSE FROM LLAMA ==========
def generate_response(prompt, api_url="http://localhost:11434/api/generate", model="llama3.3"):
    """
    Uses LLaMA locally (via Ollama or other local LLM server).
    """
    payload = {
        "model": model,
        "prompt": f"You are a compassionate CBT therapist. Help the user based on this message:\n\n{prompt}\n\nReply empathetically and helpfully.",
        "max_tokens": 500,
        "temperature": 0.7
    }
    try:
        response = requests.post(api_url, json=payload)
        response.raise_for_status()
        return response.json().get("response", "⚠️ Error: No response text.")
    except Exception as e:
        return f"⚠️ Error contacting LLaMA API: {e}"

# ========== SESSION STATE ==========
if "messages" not in st.session_state:
    st.session_state.messages = []

# ========== CHAT DISPLAY ==========
st.title("🧠 CBT Therapist Chatbot")
st.markdown("Start chatting with your personal AI CBT therapist. ✨")

for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.chat_message("user").markdown(f"🙋‍♂️ {msg['content']}")
    else:
        st.chat_message("assistant").markdown(f"🧠 {msg['content']}")

# ========== USER INPUT ==========
user_input = st.chat_input("Share what's on your mind...")

if user_input:
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Predict sentiment
    sentiment = predict_sentiment(user_input)
    st.info(f"🧭 Detected Sentiment: **{sentiment}**")

    # Generate CBT-style therapist reply
    with st.spinner("🧠 Therapist is thinking..."):
        bot_response = generate_response(user_input)

    # Add bot response
    st.session_state.messages.append({"role": "assistant", "content": bot_response})
