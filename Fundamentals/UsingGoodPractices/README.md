# Good Practices Chatbot Example

This folder demonstrates a simple GenAI-powered chatbot implemented with good coding practices in mind.

## Features
- **Continuous Chat**: The chatbot maintains a conversation history, so it can remember previous messages in the session.
- **Conversation Memory**: All user and AI messages are stored and passed to the model, allowing for context-aware responses.
- **Function Segregation**: Code is organized into separate functions for chatting with the model and logging conversations, making it modular and easy to maintain.
- **Error Handling**: (Recommended) You can easily add try/except blocks to handle API errors, invalid input, or file issues for a more robust experience.

## How It Works
- Run `main.py` to start the chat.
- Type your message and press Enter. The AI will respond and remember the conversation.
- Type `exit` to end the chat.
- All conversations are logged in `conversation_log.txt` for future reference.

## Files
- `main.py`: Main entry point for the chat application.
- `utils.py`: Contains functions for chatting with the model and logging conversations.
- `config.py`: Stores model names, API endpoint, and configuration values.

## Getting Started
1. Ensure your `.env` file is set up with your API key.
2. Install dependencies in your virtual environment.
3. Run `main.py` to start chatting!

---
*This example is designed for clarity, maintainability, and best practices in GenAI projects.*
