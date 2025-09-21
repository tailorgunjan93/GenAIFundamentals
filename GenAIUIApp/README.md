# GenAIUIApp: Conversational GenAI Web App

![Chatbot UI Example](./chatbot_ui.png)

## Overview
GenAIUIApp is a user-friendly web application that lets you interact with a Generative AI chatbot using a modern chat interface built with Gradio. This app demonstrates best practices for building conversational AI systems, including context reten
tion, modular code, and robust error handling.

---

## ✨ Features
- **Modern Chat UI**: Clean, interactive chat interface powered by Gradio.
- **Continuous Conversation**: The AI remembers the full conversation, enabling context-aware, multi-turn dialogue.
- **Session Isolation**: Each user's chat is private and independent.
- **Modular Code**: Functions for chat, logging, and configuration are separated for clarity and maintainability.
- **Error Handling**: Graceful handling of API and input errors.
- **Conversation Logging**: All chats are saved for review and analysis.

---

## 🗂️ Folder Structure
- `main.py` — Launches the Gradio chat interface and manages conversation flow.
- `utils.py` — Contains helper functions for interacting with the GenAI API and logging.
- `config.py` — Stores model names, API endpoint, and configuration values.
- `conversation_log.txt` — Stores chat logs.
- `chatbot_ui.png` — (Add your own UI screenshot or illustration here!)

---

## 🚀 Getting Started
1. **Set up your environment:**
    - Create a `.env` file with your API key (see below).
    - Install dependencies: `pip install -r requirements.txt`
2. **Run the app:**
    - In your terminal, run: `python main.py`
3. **Chat with the AI:**
    - Type your message and press Enter. The AI will respond and remember the conversation.
    - Type `exit` in the UI to end the session.
4. **Review chat logs:**
    - All conversations are saved in `conversation_log.txt`.

---

## 🔑 Example .env File
```
GEMINI_API_KEY=your_api_key_here
```

---

## 💡 Best Practices Demonstrated
- **Separation of Concerns:** Each function and file has a clear responsibility.
- **Environment Variables:** API keys are loaded securely from a `.env` file.
- **Config Management:** All model and API settings are centralized in `config.py`.
- **Extensible Design:** Easy to add new features, such as more logging, error handling, or new chat commands.

---

## 🖼️ Adding an Image
To display the chatbot UI illustration above, add an image named `chatbot_ui.png` to this folder. You can use a screenshot of your running app or any relevant image.

---

*This project is designed for clarity, maintainability, and best practices in GenAI web applications. Happy chatting!*
