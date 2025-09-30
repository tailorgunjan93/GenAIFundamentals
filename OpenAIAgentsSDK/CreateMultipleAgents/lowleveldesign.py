#Importing necessary modules
from agents import Agent
from common import gemini_model
# Define Low-Level Design (LLD) Agent
lld_promt = "Break down the application into granular components and modules. Define internal logic, data flow, and interface contracts for each unit. Ensure each piece is independently testable and follows single-responsibility principles."
# Create LLD Agent
lld_agent = Agent(
    model=gemini_model, 
    name="LLDAgent",
    instructions=lld_promt)
# Create LLD Tool
lld_tool = lld_agent.as_tool(tool_name="LLDTool", tool_description="Generates low-level design documents and detailed component specifications based on user requirements.")