
# Import required libraries
import dotenv  # For loading environment variables from .env file
import os  # For accessing environment variables
import config  # Custom config file for model names and endpoints
from openai import OpenAI  # OpenAI client for GenAI API

# Load environment variables from .env file (should be done before using config)
dotenv.load_dotenv(override=True)

# Get your API key from environment
gemini_api_key = os.getenv("GEMINI_API_KEY")

# Store the conversation history as a list of messages
message = []

# Function to chat with Gemini model
def chat_with_gemini(user_input):
    """
    Sends a user message to the Gemini chat model and returns the AI's response.
    Appends each user message to the conversation history.
    """
    # Add the user's message to the conversation
    message.append({"role": "user", "content": user_input})
    # Initialize the OpenAI client with your API key and endpoint
    gen_ai = OpenAI(api_key=gemini_api_key, base_url=config.GEMINI_URL_OPEN_AI)
    # Send the message to the GenAI chat model and get a response
    response = gen_ai.chat.completions.create(
        model=config.GEMINI_FLASH_MODEL_NAME,  # Use a valid model name as per your API provider
        messages=message, 
        temperature=config.Tempture,  # Controls randomness/creativity
        max_tokens=config.MAX_TOKENS  # Limits response length
    )
    # Print the AI's response to the user's message
    print("Gemini: " + response.choices[0].message.content)
    return response.choices[0].message.content

# Function to log the conversation to a file
def log_conversation(user_input, ai_response):
    """
    Logs the user input and AI response to a text file for record-keeping.
    """
    with open("conversation_log.txt", "a") as log_file:
        log_file.write(f"User: {user_input}\n")
        log_file.write(f"Gemini: {ai_response}\n\n")