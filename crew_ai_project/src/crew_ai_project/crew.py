from crewai import Agent, Crew, Process, Task,LLM
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List
from dotenv import load_dotenv
from crewai_tools import SerperDevTool
import os
load_dotenv(override=True)
gemini_model = os.getenv("MODEL")
api_key = os.getenv("GEMINI_API_KEY")
print(f"Using model: {gemini_model}")
print(f"Using API Key: {api_key}")
llm = LLM(model=gemini_model,api_key=api_key)  # Initialize the LLM once
print (llm)

@CrewBase
class CrewAiProject():
    """CrewAiProject crew"""

    agents_config = 'config/agents.yaml'
    tasks_config =  'config/tasks.yaml'
   
    @agent
    def debater(self) -> Agent:
        return Agent(config=self.agents_config['Debater'],verbose=True,tool=[SerperDevTool()])

    @agent
    def judge(self) -> Agent:
        return Agent(
            config=self.agents_config['judge'], # type: ignore[index]
            verbose=True
        )

    # To learn more about structured task outputs,
    # task dependencies, and task callbacks, check out the documentation:
    # https://docs.crewai.com/concepts/tasks#overview-of-a-task
    @task
    def propose(self) -> Task:
        return Task(
            config=self.tasks_config['propose'], # type: ignore[index]
        )

    @task
    def oppose(self) -> Task:
        return Task(
            config=self.tasks_config['oppose'], # type: ignore[index]
            
        )

    @task
    def decide(self)-> Task:
        return Task(
            config=self.tasks_config['decide'], # type: ignore[index]
            
        )
    @crew
    def crew(self) -> Crew:
        """Creates the CrewAiProject crew"""
        # To learn how to add knowledge sources to your crew, check out the documentation:
        # https://docs.crewai.com/concepts/knowledge#what-is-knowledge

        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            llm=llm,  # Use the initialized LLM
            verbose=True,
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )
