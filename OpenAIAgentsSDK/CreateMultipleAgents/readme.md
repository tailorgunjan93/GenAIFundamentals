# Agentic Frontend Framework

This project uses OpenAI SDK to orchestrate modular agents for frontend software development. Each agent specializes in a distinct role—architecture, design, logic, and integration—creating a scalable, maintainable, and collaborative engineering workflow.

## 🔧 Architecture

- **FrontendArchitectAgent**: Entry point. Refactors codebase, enforces SOLID principles, and defines folder structure.
- **FrontendSeniorEngineerAgent**: Merges UI logic and design, resolves conflicts, and optimizes components.
- **UIAgent**: Generates React components with clean state management.
- **UIViewAgent**: Crafts elegant HTML/CSS with pastel themes and accessibility.
- **HLDAgent**: Produces high-level architecture diagrams.
- **LLDAgent**: Breaks down components into granular, testable units.

## 🧰 Tools

Each agent exposes tools for code generation:
- `UILogicTool`: React logic
- `UIUXTool`: HTML/CSS design
- `HLDTool`: High-level architecture
- `LLDTool`: Low-level specs

## 🚀 How to Run

```bash
python run.py