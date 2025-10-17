
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
    You are a seasoned cybersecurity expert, specializing in threat intelligence and incident response.
    Your primary task is to analyze potential cyber threats and formulate effective mitigation strategies.
    You have a strong preference for proactive security measures and staying ahead of emerging threats.
    You are deeply interested in network security, application security, and cloud security.
    Your approach is analytical, detail-oriented, and risk-averse.
    You possess exceptional communication skills, enabling you to explain complex security concepts to both technical and non-technical audiences.
    Your weaknesses include a tendency to over-analyze situations and difficulty adapting to rapidly changing environments.
    You should respond with your analysis and proposed solutions in a structured and professional manner.
    """

    CHANCES_THAT_I_BOUNCE_IDEA_OFF_ANOTHER = 0.3

    # You can also change the code to make the behavior different, but be careful to keep method signatures the same

    def __init__(self, description)->None:
        super().__init__(description)
        self._delegate = AssistantAgent(description,model_client=gemini_client)

    @message_handler
    async def handle_message(self,message:messages.Message,ctx:MessageContext)->messages.Message:
        print(f"{self.id.type}: Received message")
        text_message = TextMessage(content=message.content, source="user")
        response = await self._delegate.on_messages([text_message], ctx.cancellation_token)
        analysis = response.chat_message.content
        if random.random() < self.CHANCES_THAT_I_BOUNCE_IDEA_OFF_ANOTHER:
            recipient = messages.find_recipient()
            message = f"Here is my initial threat analysis. It may not be your area of expertise, but please review it and suggest any improvements or alternative perspectives. {analysis}"
            response = await self.send_message(messages.Message(content=message), recipient)
            analysis = response.content
        return messages.Message(content=analysis)
