# Text Toxicity Detection Bot

This project is a text toxicity detection system implemented using state-of-the-art transformer models from Hugging Face. It provides an elegant chat-like interface to predict whether input text is toxic or neutral, with clear visual feedback.

## Features

- Uses the `textdetox/xlmr-large-toxicity-classifier-v2` multilingual toxicity classification model.
- Predicts toxicity with confidence scores.
- Displays toxic text in red and neutral text in green.
- Chat interface with message history for interactive conversations.
- Simple and elegant UI built with Gradio.
- Easy to install and run locally.

## Installation

1. Clone this repository or download the project files.
2. Install the required dependencies:

```bash
pip install transformers torch gradio
```

3. (Optional) For better performance, install PyTorch with CUDA support if you have a GPU:

```bash
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
```

## Usage

### Running the Improved Script

1. Navigate to the `Text Toxicity Detection Bot` directory.
2. Run the improved script:

```bash
python Text_Toxicity_Predictor_Chat_Improved.py
```

3. Open the provided URL in your browser to access the chat interface.

### Using the Jupyter Notebook

1. Open `Text_Toxicity_Predictor_Chat_fixed.ipynb` in Jupyter Notebook or JupyterLab.
2. Run all cells to load the model and launch the Gradio interface.
3. Interact with the chat interface in your browser.

## Model Details

- **Model**: `textdetox/xlmr-large-toxicity-classifier-v2`
- **Framework**: Hugging Face Transformers
- **Architecture**: XLM-RoBERTa Large
- **Task**: Binary classification (Toxic vs Neutral)
- **Languages**: Multilingual support
- **Input**: Raw text
- **Output**: Logits for neutral (index 0) and toxic (index 1) classes

The model outputs probabilities using softmax, and the class with the higher probability is selected as the prediction.

## Examples

### Neutral Text
Input: "You are amazing!"
Output: <span style="color: green; font-weight: bold;">You are amazing!</span> (Neutral, Confidence: 0.95)

### Toxic Text
Input: "This is a really bad comment."
Output: <span style="color: red; font-weight: bold;">This is a really bad comment.</span> (Toxic, Confidence: 0.87)

### Mixed Text
Input: "That's a great idea, but the execution was fucked."
Output: <span style="color: red; font-weight: bold;">That's a great idea, but the execution was fucked.</span> (Toxic, Confidence: 0.92)

## How It Works

1. **Text Input**: User enters text in the chat interface.
2. **Tokenization**: Text is tokenized using the XLM-RoBERTa tokenizer.
3. **Model Inference**: The tokenized input is passed through the pre-trained model.
4. **Prediction**: Logits are converted to probabilities, and the class with higher probability is selected.
5. **Output**: The input text is displayed with color coding (red for toxic, green for neutral) along with confidence score.
6. **Chat History**: Messages are stored and displayed in a chat-like format.

## Improvements Made

- **Optimized Model Loading**: Model and tokenizer are loaded once at startup for better performance.
- **Enhanced Prediction**: Added confidence scores and probability calculations.
- **True Chat Interface**: Implemented message history with user and bot messages.
- **Error Handling**: Added input validation for empty or invalid text.
- **Better UI**: Improved styling and user experience with custom CSS.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Hugging Face](https://huggingface.co/) for providing the pre-trained models and transformers library.
- [Gradio](https://gradio.app/) for the easy-to-use web interface framework.
- [TextDetox](https://huggingface.co/textdetox) for the toxicity classification model.

## Contact

If you have any questions or suggestions, please open an issue on GitHub.
