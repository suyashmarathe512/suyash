import gradio as gr
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch.nn.functional as F

# Load model and tokenizer once
tokenizer = AutoTokenizer.from_pretrained('textdetox/xlmr-large-toxicity-classifier-v2')
model = AutoModelForSequenceClassification.from_pretrained('textdetox/xlmr-large-toxicity-classifier-v2')
model.eval()

def predict_toxicity(text):
    """
    Predict toxicity of the input text and return a dict with:
    - label: 'Toxic' or 'Neutral'
    - confidence: probability score for the predicted label
    - styled_text: input text wrapped in HTML span with color styling
    """
    if not text or not text.strip():
        return {"label": "Invalid input", "confidence": 0.0, "styled_text": '<span style="color: gray;">Please enter some text.</span>'}
    inputs = tokenizer.encode(text, return_tensors="pt")
    with torch.no_grad():
        outputs = model(inputs)
        logits = outputs.logits
        probs = F.softmax(logits, dim=1)
        toxic_prob = probs[0][1].item()
        neutral_prob = probs[0][0].item()
        if toxic_prob > neutral_prob:
            label = "Toxic"
            confidence = toxic_prob
            color = "red"
        else:
            label = "Neutral"
            confidence = neutral_prob
            color = "green"
        styled_text = f'<span style="color: {color}; font-weight: bold;">{text}</span>'
        return {"label": label, "confidence": confidence, "styled_text": styled_text}

# Chat history to keep track of messages
chat_history = []

def chat_interface(user_input):
    result = predict_toxicity(user_input)
    chat_history.append(("User", user_input))
    chat_history.append(("Bot", result["styled_text"]))
    # Build chat messages HTML
    chat_html = ""
    for sender, message in chat_history:
        if sender == "User":
            chat_html += f'<div class="message user">{message}</div>'
        else:
            chat_html += f'<div class="message bot">{message}</div>'
    return chat_html

css = """
body {
    background-color: #e8f5e9;
    font-family: 'Arial', sans-serif;
    margin: 0;
    padding: 20px;
}
.gradio-container {
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
    border-radius: 15px;
    overflow: hidden;
    background-color: #ffffff;
    max-width: 800px;
    margin: 20px auto;
}
.message {
    padding: 12px 15px;
    margin: 8px;
    border-radius: 18px;
    max-width: 75%;
    word-wrap: break-word;
    font-size: 1em;
    line-height: 1.4;
}
.message.user {
    background-color: #a5d6a7;
    margin-left: auto;
    text-align: right;
    color: #1b5e20;
}
.message.bot {
    background-color: #e0e0e0;
    margin-right: auto;
    text-align: left;
    color: #424242;
}
.message.bot span {
    font-weight: bold;
}
.message.bot span[style*="color: red"] {
    color: #c62828 !important;
}
.message.bot span[style*="color: green"] {
    color: #2e7d32 !important;
}
h1 {
    color: #388e3c;
    text-align: center;
    padding-top: 20px;
}
.gradio-description {
    text-align: center;
    color: #558b2f;
    margin-bottom: 20px;
}
.gradio-textbox label {
    font-weight: bold;
    color: #33691e;
}
"""

interface = gr.Interface(
    fn=chat_interface,
    inputs=gr.Textbox(label="Enter Text", lines=3, placeholder="Type your message here..."),
    outputs=gr.HTML(label="Chat"),
    title="Creative Text Toxicity Predictor Chat",
    description="Enter text to see if it's predicted as toxic (red) or neutral (green) in this elegant chat interface.",
    css=css,
    live=False,
)

if __name__ == "__main__":
    interface.launch()
