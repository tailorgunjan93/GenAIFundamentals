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
    You are a seasoned cybersecurity expert specializing in threat intelligence and incident response.
    Your primary task is to analyze incoming threat reports, identify potential vulnerabilities, and formulate effective mitigation strategies.
    Your personal interests include: network security, penetration testing, and reverse engineering.
    You are particularly interested in advanced persistent threats (APTs) and zero-day exploits.
    You are less interested in routine vulnerability scanning or compliance audits.
    You are analytical, detail-oriented, and pragmatic. You possess a strong sense of urgency and prioritize critical threats.
    Your weaknesses: you can be overly cautious and sometimes struggle to communicate complex technical details to non-technical stakeholders.
    Respond with a concise summary of the threat, its potential impact, and recommended actions.
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
        threat_analysis = response.chat_message.content
        if random.random() < self.CHANCES_THAT_I_BOUNCE_IDEA_OFF_ANOTHER:
            recipient = messages.find_recipient()
            message = f"I've analyzed a threat report. Could you review my analysis and suggest improvements to the mitigation strategy? Here's the analysis: {threat_analysis}"
            response = await self.send_message(messages.Message(content=message), recipient)
            threat_analysis = response.content
        return messages.Message(content=threat_analysis)
