import os
from pathlib import Path
import streamlit as st
import requests
import joblib

# ========== CONFIG ==========
st.set_page_config(page_title="CBT AI Therapist", page_icon="🧠", layout="centered")

# ========== BASE DIRECTORY ==========
BASE_DIR = Path(__file__).parent

# ========== SIDEBAR UI & ASSETS ==========
# Load logo
logo_path = BASE_DIR / "assets" / "logo.png"
if logo_path.exists():
    st.sidebar.image(str(logo_path), width=150)

st.sidebar.markdown("### 🧠 AI CBT Therapist")
st.sidebar.markdown("#### Models in Use:")
st.sidebar.markdown("- 🧩 Fine-tuned LLaMA via Ollama")
st.sidebar.markdown("- 💬 SVC Sentiment Classifier")
st.sidebar.markdown("---")
st.sidebar.info("Feel safe to talk. This app does **not store** your data.")

# ========== LOAD SENTIMENT MODEL ==========
model_path = BASE_DIR / "sentiment_svc_model.joblib"

@st.cache_resource
def load_sentiment_model(path: Path):
    if not path.exists():
        st.error(f"❌ Sentiment model not found at {path}")
        st.stop()
    return joblib.load(path)

sentiment_model = load_sentiment_model(model_path)

# ========== SENTIMENT PREDICTION ==========
def predict_sentiment(text: str) -> str:
    """Predict the sentiment label for a given text."""
    try:
        label = sentiment_model.predict([text])[0]
    except Exception as e:
        st.error(f"⚠️ Sentiment prediction failed: {e}")
        return "Unknown"
    return label

# ========== LLaMA CBT RESPONSE ==========
def generate_cbt_response(prompt: str,
                          api_url: str = "http://localhost:11434/api/generate",
                          model: str = "llama3.3-cbt") -> str:
    """
    Generate a CBT-style response using a fine-tuned LLaMA model via local API.
    """
    payload = {
        "model": model,
        "prompt": f"You are a compassionate CBT therapist. User says:\n{prompt}\nProvide an empathetic, CBT-based therapeutic response.",
        "max_tokens": 500,
        "temperature": 0.7,
    }
    try:
        resp = requests.post(api_url, json=payload, timeout=15)
        resp.raise_for_status()
        data = resp.json()
        return data.get("response", "⚠️ No response from LLaMA API.")
    except requests.RequestException as e:
        return f"⚠️ Error contacting LLaMA API: {e}"
    except ValueError:
        return "⚠️ Invalid JSON received from LLaMA API."

# ========== SESSION STATE ==========
if "messages" not in st.session_state:
    st.session_state.messages = []

# ========== CHAT UI ==========
st.title("🧠 CBT Therapist Chatbot")
st.markdown("Start chatting with your personal AI CBT therapist. ✨")

# Display conversation
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.chat_message("user").markdown(f"🙋‍♂️ **You:** {msg['content']}")
    else:
        st.chat_message("assistant").markdown(f"🧠 **Therapist:** {msg['content']}")

# User input
user_input = st.chat_input("Share what's on your mind...")
if user_input:
    # Append and display user message
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Predict sentiment and display
    sentiment = predict_sentiment(user_input)
    st.info(f"🧭 Detected Sentiment: **{sentiment}**")

    # Generate and append therapist response
    with st.spinner("🧠 Therapist is thinking..."):
        bot_reply = generate_cbt_response(user_input)
    st.session_state.messages.append({"role": "assistant", "content": bot_reply})


