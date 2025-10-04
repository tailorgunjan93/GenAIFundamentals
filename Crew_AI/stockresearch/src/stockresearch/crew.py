from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from crewai_tools import SerperDevTool
from typing import List
from pydantic import BaseModel, Field
from .tools.push_tool import PushNotificationTool
from crewai.memory import LongTermMemory, ShortTermMemory, EntityMemory
from crewai.memory.storage.rag_storage import RAGStorage
from crewai.memory.storage.ltm_sqlite_storage import LTMSQLiteStorage
from dotenv import load_dotenv
import os

load_dotenv(override=True)
gemini_api_key = os.getenv("GEMINI_API_KEY")
# If you want to run a snippet of code before or after the crew starts,
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators

class TrendingCompany(BaseModel):
    name: str = Field(description="Name of the company")
    ticker: str = Field( description="Ticker symbol of the company")
    reason: str = Field( description="Reason why the company is trending")

class TrendingCompaniesList(BaseModel):
    companies: List[TrendingCompany] = Field(description="List of trending companies")

class TrendingCompanyResearch(BaseModel):
    name: str = Field(description="Name of the company")
    market_position: str = Field( description="Market position of the company")
    future_outlook: str = Field( description="Future outlook of the company")
    investment_potential: str = Field( description="Investment potential of the company")
    latest_news: str = Field( description="Latest news about the company")
    latest_news_date: str = Field( description="Date of the latest news about the company")

class TrendingCompanyResearchList(BaseModel):
    research: List[TrendingCompanyResearch] = Field(description="List of research on trending companies")

@CrewBase
class Stockresearch():
    """Stockresearch crew"""

    agents_config = 'config/agents.yaml'
    tasks_config =  'config/tasks.yaml'


    @agent
    def trending_company_finder(self) -> Agent:
        return Agent(
            config=self.agents_config['trending_company_finder'], 
            verbose=True,tools=[SerperDevTool()]
        )

    @agent
    def financial_researcher(self) -> Agent:
        return Agent(
            config=self.agents_config['financial_researcher'], 
            verbose=True,tools=[SerperDevTool()]
        )
    
    @agent
    def stock_picker(self) -> Agent:
        return Agent(
            config=self.agents_config['stock_picker'], # type: ignore[index]
            verbose=True,
            tools=[PushNotificationTool()]
        )

    @task
    def find_trending_companies(self) -> Task:
        return Task(
            config=self.tasks_config['find_trending_companies'], # type: ignore[index]
            output_pydantic=TrendingCompaniesList
        )
    @task
    def research_trending_companies(self) -> Task:
        return Task(
            config=self.tasks_config['research_trending_companies'], # type: ignore[index]
            output_pydantic=TrendingCompanyResearchList
        )   
    @task
    def pick_best_company(self) -> Task:
        return Task(
            config=self.tasks_config['pick_best_company'], # type: ignore[index]
        )
    @crew
    def crew(self) -> Crew:
        """Creates the Stockresearch crew"""
        manager = Agent(
            config=self.agents_config['manager'], # type: ignore[index] 
            verbose=True,
            allow_delegation=True
        )

       

        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.hierarchical,
            verbose=True,
            manager_agent=manager,
            memory=True,
            # Long-term memory for persistent storage across sessions
            long_term_memory = LongTermMemory(
                storage=LTMSQLiteStorage(
                    db_path="./memory/long_term_memory_storage.db"
                )
             ),
            #Below code used when we choose paid api not free api 
            # # Short-term memory for current context using RAG
            # short_term_memory = ShortTermMemory(
            #     storage = RAGStorage(
            #             embedder_config={
            #                 "provider": 'google-generativeai',
            #                 "config": {
            #                     "model_name": 'models/embedding-001',
            #                     "api_key": gemini_api_key
            #                 }
            #             },
                        
            #             type="short_term",
            #             path="./memory/"
            #         )
            #     ),            # Entity memory for tracking key information about entities
            # entity_memory = EntityMemory(
            #     storage=RAGStorage(
            #         embedder_config={
            #             "provider": 'google-generativeai',
            #             "config": {
            #                 "model_name": 'models/embedding-001',
            #                 "api_key": gemini_api_key
            #             }
            #         },
                
            #         type="entity_storage",
            #         path="./memory/"
            #     )
            # ),
        )
