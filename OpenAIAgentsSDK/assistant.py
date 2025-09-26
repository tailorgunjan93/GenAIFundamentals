import os
from dotenv import load_dotenv
from agents import Agent, Runner, trace, function_tool, OpenAIChatCompletionsModel
from openai import AsyncOpenAI
import config
# Load environment variables from .env file
load_dotenv(override=True)  
# Get your API key from environment
gemini_api_key = os.getenv("GEMINI_API_KEY")
#this is first agent creation script using gemini model
model = config.GEMINI_FLASH_MODEL_NAME
url = config.GEMINI_URL_OPEN_AI
gemini_client = AsyncOpenAI(api_key=gemini_api_key, base_url=url)  
gemini_model = OpenAIChatCompletionsModel(model=model, openai_client=gemini_client)
first_agent = Agent(
    model=gemini_model, 
    name="FirstAgent",
instructions="Search on the web and find the answer to the question asked by the user.")
