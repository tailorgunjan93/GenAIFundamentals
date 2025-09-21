import os
import dotenv
# Load environment variables from .env file
dotenv.load_dotenv(override=True)
# Get your API key from environment
gemini_api_key = os.getenv("GEMINI_API_KEY")

# Model name for Gemini Turbo (used for advanced chat completions)
GEMINI_TURBO_MODEL_NAME = "gemini-1.5-turbo"

# Model name for Gemini Flash (used for fast, lightweight chat completions)
GEMINI_FLASH_MODEL_NAME = "gemini-2.0-flash"

# Base URL for the Gemini OpenAI-compatible API endpoint
GEMINI_URL_OPEN_AI = "https://generativelanguage.googleapis.com/v1beta/openai/"

# Temperature controls randomness/creativity of responses (0 = deterministic, 1 = more random)
Tempture = 0.5

# Maximum number of tokens (words/pieces) in the AI's response
MAX_TOKENS = 200