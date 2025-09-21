#importing liberaries
import dotenv
import os
import config
from openai import OpenAI
#load env variables
dotenv.load_dotenv(override=True)
gemini_api_key = os.getenv("GEMINI_API_KEY")

#function to chat with gemini
def chat_with_gemini(user_input):
    # Prepare a user message for the GenAI chat model
    message = [{"role": "user", "content": user_input}]
    # Initialize the OpenAI client with your API key and endpoint
    gen_ai = OpenAI(api_key=gemini_api_key, base_url=config.GEMINI_URL_OPEN_AI)
    # Send the message to the GenAI chat model and get a response
    response = gen_ai.chat.completions.create(
        model=config.GEMINI_FLASH_MODEL_NAME,  # Use a valid model name as per your API provider
        messages=message
    )
    # Print the AI's response to the user's message
    print("Gemini: " + response.choices[0].message.content)

#now take user input untill user types 'exit'
while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        print("Exiting the chat. Goodbye!")
        break
    chat_with_gemini(user_input)    