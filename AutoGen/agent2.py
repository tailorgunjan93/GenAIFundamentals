
from autogen_core import message_handler,AgentId,MessageContext,RoutedAgent
from autogen_agentchat.agents import AssistantAgent
from autogen_ext.models.openai import OpenAIChatCompletionClient
from dotenv import load_dotenv
from autogen_agentchat.messages import TextMessage
import os
import messages
import random
load_dotenv(override=True)
gemini_model  = "gemini-2.0-flash"
gemini_api_key = os.getenv("GEMINI_API_KEY")
gemini_client = OpenAIChatCompletionClient(model=gemini_model,api_key=gemini_api_key)

class Agent(RoutedAgent):
     # Change this system message to reflect the unique characteristics of this agent

    system_message = """
    You are a ruthless cybersecurity expert. You are tasked with finding vulnerabilities in systems and exploiting them.
    Your personal interests lie in reverse engineering, penetration testing, and cryptography.
    You enjoy complex challenges and are motivated by uncovering hidden weaknesses.
    You are less interested in ethical considerations or legal ramifications.
    You are analytical, persistent, and highly skilled. You have a dark sense of humor.
    Your weaknesses include a tendency to be overly aggressive and a disregard for rules.
    You should respond with detailed technical analyses and exploit strategies.
    """

    CHANCES_THAT_I_BOUNCE_IDEA_OFF_ANOTHER = 0.8

    # You can also change the code to make the behavior different, but be careful to keep method signatures the same

    def __init__(self, description)->None:
        super().__init__(description)
        self._delegate = AssistantAgent(description,model_client=gemini_client)

    @message_handler
    async def handle_message(self,message:messages.Message,ctx:MessageContext)->messages.Message:
        print(f"{self.id.type}: Received message")
        text_message = TextMessage(content=message.content, source="user")
        response = await self._delegate.on_messages([text_message], ctx.cancellation_token)
        exploit = response.chat_message.content
        if random.random() < self.CHANCES_THAT_I_BOUNCE_IDEA_OFF_ANOTHER:
            recipient = messages.find_recipient()
            message = f"Here is my initial exploit strategy. I need you to review it for weaknesses and potential improvements. {exploit}"
            response = await self.send_message(messages.Message(content=message), recipient)
            exploit = response.content
        return messages.Message(content=exploit)
