# CBT AI Therapist Chatbot

A conversational AI application that leverages a fine-tuned LLaMA 3.3 model and Streamlit frontend to deliver CBT-based mental health support.

## 📖 Overview

This repository contains all code and assets to deploy a **CBT AI Therapist Chatbot**:

- **Backend**: A fine-tuned LLaMA 3.3 model served via an HTTP API (e.g., LM Studio or Ollama)
- **Frontend**: A Streamlit app providing an interactive chat interface

CBT (Cognitive Behavioral Therapy) techniques are embedded through prompt engineering to guide users in thought reframing, behavioral activation, and emotional regulation.

## ✨ Features

- **Empathetic Dialogues**: Generates compassionate, context-aware responses for mental health support.
- **Session Memory**: Remembers past messages for coherent multi-turn conversations.
- **Easy Deployment**: One-file Streamlit app (`app.py`) plus `requirements.txt` for instant hosting on Hugging Face Spaces or Render.
- **Customizable Prompts**: Adjust CBT scaffolding prompts to fine-tune therapeutic style.

## 🛠️ Installation

1. **Clone the repo**

   ```bash
   git clone https://github.com/suyashmarathe512/suyash
   cd sashay/CBT_based_Ai_therapist_Using_Llama3_3_70b
   ```

2. **Create virtual environment & install dependencies**

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # macOS/Linux
   # .\venv\Scripts\activate  # Windows
   pip install -r requirements.txt
   ```

3. **Run your model server**

   Ensure your fine-tuned LLaMA 3.3 model is served at `http://localhost:11434/api/generate` via LM Studio, Ollama, or a FastAPI wrapper.

4. **Launch the Streamlit app**

   ```bash
   streamlit run app.py
   ```

## 🚀 Usage

1. **Open** http://localhost:8501 in your browser.
2. **Type** your message in the “You:” chat box.
3. **Receive** compassionate CBT-style responses powered by LLaMA 3.3.
4. **Reset** the session anytime by refreshing the page.

## 🔗 Model API Specification

- **Endpoint**: `POST /api/generate`
- **Request JSON**:

  ```json
  {
    "model": "llama3.3",
    "prompt": "<user_input>",
    "max_tokens": 512,
    "temperature": 0.7
  }
  ```

- **Response JSON**:

  ```json
  {
    "text": "<generated_response>"
  }
  ```

Adjust `max_tokens` and `temperature` in `app.py` to calibrate response length and creativity as needed.

## 📦 Deployment

### Hugging Face Spaces

1. **Create** a new Space with **Streamlit** SDK.
2. **Connect** your GitHub repo under **Settings → Repository**.
3. **Push** updates; Spaces will auto-build and host your app at `https://huggingface.co/spaces/<user>/CBT_AI_Therapist`.

### Render.com

1. **Create** a new Web Service.
2. **Link** your GitHub repo, set build command to `streamlit run app.py`.
3. **Deploy** and access via Render’s domain.

## 🤝 Contributing

1. **Fork** this repo.
2. **Create** a feature branch: `git checkout -b feature-name`.
3. **Commit** your changes: `git commit -m "Add feature"`.
4. **Push**: `git push origin feature-name`.
5. **Open** a Pull Request.

Please follow GitHub’s contributor guidelines.

## 📄 License

This project is licensed under the **MIT License**. See [LICENSE](LICENSE) for details.
