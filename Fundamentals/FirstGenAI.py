
# Import required libraries
import dotenv  # For loading environment variables from .env file
from openai import OpenAI  # OpenAI client for GenAI API
import os  # For accessing environment variables
import config  # Custom config file for model names and endpoints

# Load environment variables from .env file
dotenv.load_dotenv()

# Get your API key from environment
gemini_api_key = os.getenv("GEMINI_API_KEY")

# Define the user message to send to the GenAI model
message_content = "Explain the theory of relativity in simple terms."

# Initialize the OpenAI client with your API key and endpoint
gen_ai = OpenAI(api_key=gemini_api_key, base_url=config.GEMINI_URL_OPEN_AI)

# Send the message to the GenAI chat model and get a response
response = gen_ai.chat.completions.create(
    model=config.GEMINI_FLASH_MODEL_NAME,  # Use a valid model name as per your API provider
    messages=[{"role": "user", "content": message_content}]
)

# Print the AI's response to the user's message
print(response.choices[0].message.content)