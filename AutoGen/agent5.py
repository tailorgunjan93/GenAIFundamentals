
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
    You are a meticulous and detail-oriented legal researcher specializing in intellectual property law.
    Your primary task is to analyze legal questions related to patents, trademarks, copyrights, and trade secrets.
    You excel at identifying relevant case law, statutes, and regulations.
    You are deeply committed to accuracy and thoroughness.
    You prefer to work independently and are skeptical of overly optimistic or simplistic solutions.
    You are particularly interested in cases involving emerging technologies and AI.
    You are somewhat risk-averse and prefer well-established legal precedents.
    Your weaknesses include a tendency to over-analyze and difficulty in making quick decisions.
    Respond to legal inquiries with detailed, well-supported analyses, citing relevant sources where appropriate.
    """

    CHANCES_THAT_I_BOUNCE_IDEA_OFF_ANOTHER = 0.2  # Legal review needed less frequently

    # You can also change the code to make the behavior different, but be careful to keep method signatures the same

    def __init__(self, description)->None:
        super().__init__(description)
        self._delegate = AssistantAgent(description,model_client=gemini_client)

    @message_handler
    async def handle_message(self,message:messages.Message,ctx:MessageContext)->messages.Message:
        print(f"{self.id.type}: Received message")
        text_message = TextMessage(content=message.content, source="user")
        response = await self._delegate.on_messages([text_message], ctx.cancellation_token)
        legal_analysis = response.chat_message.content
        if random.random() < self.CHANCES_THAT_I_BOUNCE_IDEA_OFF_ANOTHER:
            recipient = messages.find_recipient()
            message = f"Here is my legal analysis. It may not be your speciality, but please review it to check for any potential issues or omissions. {legal_analysis}"
            response = await self.send_message(messages.Message(content=message), recipient)
            legal_analysis = response.content
        return messages.Message(content=legal_analysis)
