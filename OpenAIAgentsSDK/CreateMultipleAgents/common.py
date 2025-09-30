# common.py
# Initializes the Gemini model using OpenAI SDK with environment variables

import os
from dotenv import load_dotenv
from agents import Agent, OpenAIChatCompletionsModel
from openai import AsyncOpenAI
import config

# Load environment variables from .env file
load_dotenv(override=True)

# Retrieve Gemini API key and endpoint
gemini_api_key = os.getenv("GEMINI_API_KEY")
url = config.GEMINI_URL_OPEN_AI
model = config.GEMINI_FLASH_MODEL_NAME

# Initialize OpenAI client and Gemini model
gemini_client = AsyncOpenAI(api_key=gemini_api_key, base_url=url)
gemini_model = OpenAIChatCompletionsModel(model=model, openai_client=gemini_client)