# GenAI Fundamentals Project

Welcome to the **GenAI Fundamentals** project! This repository is designed to help you learn and experiment with Generative AI (GenAI) concepts using Python and Jupyter Notebooks.

## 📚 What You'll Find Here
- **Interactive Jupyter Notebooks**: Step-by-step code examples and explanations.
- **Hands-on GenAI Demos**: Try out GenAI models and APIs directly in code.
- **Configurable API Integration**: Easily switch between different GenAI models and endpoints.
- **Best Practices**: Learn how to structure GenAI projects and manage environment variables securely.

## 🚀 Getting Started
1. **Clone the repository**
2. **Set up a Python virtual environment**
3. **Install dependencies** using `uv` or `pip`
4. **Configure your `.env` file** with your API keys and endpoints
5. **Open the Jupyter notebook** in the `Fundamentals` folder and start exploring!

## 🛠️ Key Files
- `Fundamentals/FirstGenAI.ipynb`: Main learning notebook with GenAI code examples
- `Fundamentals/FirstGenAI.py`: Python script version for quick testing
- `config.py`: Stores model names and API endpoint URLs
- `.env`: Store your API keys and secrets here (never commit this file!)

## 🔑 Environment Variables
Create a `.env` file in the root directory with the following keys:
```
GEMINI_API_KEY=your_api_key_here
GEMINI_URL_OPEN_AI=https://your-genai-endpoint.com/v1
```

## 💡 Tips
- Always load environment variables **before** importing your config module.
- Use the correct model name supported by your API provider (see their docs or use a ListModels endpoint).
- Add comments to your code to explain each step for future reference.

## 🤝 Contributing
Pull requests and suggestions are welcome! Please open an issue to discuss changes or ideas.

## 📄 License
This project is for educational purposes.

---
*Happy Learning and Creating with GenAI!*