from openai import OpenAI
import config

#Creaate function to initialize OpenAI client for chat taking user input
def chat_with_gemini(prompt):
    try:
        # Initialize the OpenAI client with your API key and endpoint
        gen_ai = OpenAI(api_key=config.gemini_api_key, base_url=config.GEMINI_URL_OPEN_AI)
        # Send the message to the GenAI chat model and get a response
        response = gen_ai.chat.completions.create(
            model=config.GEMINI_FLASH_MODEL_NAME,  # Use a valid model name as per your API provider
            messages=prompt
        )
        # Print the AI's response to the user's message
        print("Gemini: " + response.choices[0].message.content)
        return response.choices[0].message.content
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
#Function to log conversation
def log_conversation(user_input, ai_response):
    """
    Logs the user input and AI response to a text file for record-keeping.
    """
    with open("conversation_log.txt", "a") as log_file:
        log_file.write(f"User: {user_input}\n")
        log_file.write(f"Gemini: {ai_response}\n\n")