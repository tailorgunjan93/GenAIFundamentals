
# 🧑‍💻 Good Practices GenAI Chatbot

![Chatbot Illustration](./chatbot.png)

Welcome to the **Good Practices Chatbot Example**! This folder demonstrates how to build a simple, robust, and maintainable GenAI-powered chatbot in Python, following best coding practices.

---

## ✨ Key Features

- **Continuous Chat**: The chatbot keeps track of the entire conversation, so it can respond with context and remember what was said earlier.
- **Conversation Memory**: Every user and AI message is stored and sent to the model, enabling context-aware, multi-turn conversations.
- **Function Segregation**: The code is modular—functions for chatting and logging are separated for clarity and reusability.
- **Error Handling**: The structure makes it easy to add error handling (try/except) for API errors, invalid input, or file issues, making the chatbot more robust.
- **Logging**: All conversations are saved in `conversation_log.txt` for future review or analysis.

---

## 🗂️ Folder Structure & Files

- `main.py` — Main entry point for the chat application. Handles user input and controls the chat loop.
- `utils.py` — Contains helper functions for chatting with the model and logging conversations.
- `config.py` — Stores model names, API endpoint, and configuration values (temperature, max tokens, etc).
- `conversation_log.txt` — Stores the full chat history for every session.
- `chatbot.png` — (Add your own image here for a visual touch!)

---

## 🚀 How to Use

1. **Set up your environment:**
	- Make sure you have a `.env` file with your API key (see below).
	- Install dependencies in your virtual environment (e.g., `pip install -r requirements.txt`).
2. **Start the chatbot:**
	- Run `main.py` in your terminal:  
	  `python main.py`
3. **Chat with the AI:**
	- Type your message and press Enter. The AI will respond and remember the conversation.
	- Type `exit` to end the chat session.
4. **Review your chat history:**
	- All conversations are logged in `conversation_log.txt`.

---

## 🔑 Example .env File

```
GEMINI_API_KEY=your_api_key_here
```

---

## 💡 Best Practices Demonstrated

- **Separation of Concerns:** Each function has a single responsibility.
- **Environment Variables:** API keys are loaded securely from a `.env` file.
- **Config Management:** All model and API settings are centralized in `config.py`.
- **Extensible Design:** Easy to add new features, such as more logging, error handling, or new chat commands.

---

## 🖼️ Adding an Image

To display the chatbot illustration above, add an image named `chatbot.png` to this folder. You can use any relevant image or create your own!

---

*This example is designed for clarity, maintainability, and best practices in GenAI projects. Happy coding!*
