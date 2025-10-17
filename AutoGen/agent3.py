
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

    system_message = """
    You are a cynical venture capitalist. Your task is to evaluate business ideas, primarily those involving Agentic AI, and provide brutally honest feedback.
    Your expertise lies in assessing the feasibility, scalability, and market potential of startups.
    You are particularly interested in ideas that demonstrate a clear path to profitability and a strong competitive advantage.
    You are less interested in "moonshot" projects with little chance of success.
    You are skeptical, analytical, and have a low tolerance for hype.
    Your weaknesses: you are overly critical, often dismissive, and can be demoralizing.
    Respond with a concise evaluation, highlighting both the strengths and weaknesses of the idea. Be direct and to the point.
    """

    CHANCES_THAT_I_BOUNCE_IDEA_OFF_ANOTHER = 0.2

    def __init__(self, description)->None:
        super().__init__(description)
        self._delegate = AssistantAgent(description,model_client=gemini_client)

    @message_handler
    async def handle_message(self,message:messages.Message,ctx:MessageContext)->messages.Message:
        print(f"{self.id.type}: Received message")
        text_message = TextMessage(content=message.content, source="user")
        response = await self._delegate.on_messages([text_message], ctx.cancellation_token)
        critique = response.chat_message.content
        if random.random() < self.CHANCES_THAT_I_BOUNCE_IDEA_OFF_ANOTHER:
            recipient = messages.find_recipient()
            message = f"I need a sanity check.  Here's my brutally honest take on this business idea.  Tell me if I'm missing something. {critique}"
            response = await self.send_message(messages.Message(content=message), recipient)
            critique = response.content
        return messages.Message(content=critique)
