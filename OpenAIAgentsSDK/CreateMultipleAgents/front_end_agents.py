# frontend_agents.py
# Defines modular agents and tools for frontend architecture, design, and logic

from agents import Agent
from common import gemini_model
import highleveldesign
import lowleveldesign

# Load design tools
design_tools = [highleveldesign.hld_tool, lowleveldesign.lld_tool]

# ─────────────────────────────────────────────────────────────
# 🧠 Instruction Strings
# ─────────────────────────────────────────────────────────────

ui_logic_prompt = (
    "Implement reusable React components with clean state management and optimal rendering. "
    "Follow best practices for hooks, context, and performance. "
    "Ensure accessibility and responsiveness across devices."
)

ui_ux_prompt = (
    "Design elegant, accessible, and responsive UI using semantic HTML and modular CSS. "
    "Use pastel-themed palettes and ensure consistency across light and dark modes. "
    "Prioritize user experience and visual clarity."
)

frontend_senior_engineer_prompt = (
    "Merge UI logic and design codebases. Resolve conflicts, enforce coding standards, "
    "and optimize component structure. Ensure seamless integration and maintainability."
)

frontend_senior_handoff_description = (
    "Use this agent to combine UI logic and design code snippets into a cohesive frontend codebase. "
    "Ensure best practices and maintainability."
)

frontend_architect_prompt = (
    "Refactor frontend codebase to follow SOLID principles and scalable design patterns. "
    "Define folder structure, hide secrets (e.g., API keys), and enforce industry-standard practices. "
    "Document architecture decisions."
)

# ─────────────────────────────────────────────────────────────
# 🧰 Tool Descriptions
# ─────────────────────────────────────────────────────────────

ui_logic_tool_description = (
    "Generates React code snippets for UI logic and state management based on user requirements."
)

ui_ux_tool_description = (
    "Generates HTML/CSS code snippets for UI/UX design based on user requirements."
)

# ─────────────────────────────────────────────────────────────
# 🧠 Agent Definitions
# ─────────────────────────────────────────────────────────────

# Agent: UI Logic (React + Hooks + State)
ui_logic_agent = Agent(
    model=gemini_model,
    name="UIAgent",
    instructions=ui_logic_prompt
)

# Agent: UI/UX Design (HTML + CSS)
ui_ux_agent = Agent(
    model=gemini_model,
    name="UIViewAgent",
    instructions=ui_ux_prompt
)

# ─────────────────────────────────────────────────────────────
# 🔧 Tool Registrations
# ─────────────────────────────────────────────────────────────

ui_logic_tool = ui_logic_agent.as_tool(
    tool_name="UILogicTool",
    tool_description=ui_logic_tool_description
)

ui_ux_tool = ui_ux_agent.as_tool(
    tool_name="UIUXTool",
    tool_description=ui_ux_tool_description
)

# Merge all tools for senior engineer
ui_tools = [ui_logic_tool, ui_ux_tool, *design_tools]

# ─────────────────────────────────────────────────────────────
# 🧠 Senior Engineer Agent
# ─────────────────────────────────────────────────────────────

frontend_senior_engineer_agent = Agent(
    model=gemini_model,
    name="FrontendSeniorEngineerAgent",
    tools=ui_tools,
    instructions=frontend_senior_engineer_prompt,
    handoff_description=frontend_senior_handoff_description
)

# Handoff chain: Architect → Senior Engineer
handoff_chain = [frontend_senior_engineer_agent]

# ─────────────────────────────────────────────────────────────
# 🧠 Architect Agent (entry point)
# ─────────────────────────────────────────────────────────────

front_end_architect_agent = Agent(
    model=gemini_model,
    name="FrontendArchitectAgent",
    instructions=frontend_architect_prompt,
    handoffs=handoff_chain
)