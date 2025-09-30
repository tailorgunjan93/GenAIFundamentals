#import libraries
from agents import Agent
from common import gemini_model
# Define High-Level Design (HLD) Agent
hld_promt="Outline the overall architecture of the application. Define major subsystems, their responsibilities, and how they interact. Focus on scalability, modularity, and alignment with business goals."
# Create HLD Agent
hld_agent = Agent(
    model=gemini_model, 
    name="HLDAgent",
    instructions=hld_promt)
# Create HLD Tool
hld_tool = hld_agent.as_tool(tool_name="HLDTool", tool_description="Generates high-level design documents and architecture diagrams based on user requirements.")
