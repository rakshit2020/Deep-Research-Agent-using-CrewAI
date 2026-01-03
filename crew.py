from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import SerperDevTool, FirecrawlScrapeWebsiteTool
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List
from dotenv import load_dotenv
from crewai.llm import LLM
import os

load_dotenv()


@CrewBase
class DeepResearchCrew:
    """Deep Research Crew using NVIDIA NIM via LiteLLM"""

    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    agents: List[BaseAgent]
    tasks: List[Task]

    def __init__(self):
        self.search_tool = SerperDevTool(
            api_key=os.getenv("SERPER_API_KEY"),
            n_results=10
        )
        self.scrape_tool = FirecrawlScrapeWebsiteTool(
            api_key=os.getenv("FIRECRAWL_API_KEY")
        )
        self.llm = LLM(
            model="nvidia_nim/mistralai/devstral-2-123b-instruct-2512",
            api_key=os.getenv("NVIDIA_API_KEY"),
            temperature=0.7,
            max_tokens=8192
        )

    # ---------------- Agents ----------------

    @agent
    def research_manager(self) -> Agent:
        return Agent(
            config=self.agents_config["research_manager"],
            verbose=True,
            llm=self.llm
        )

    @agent
    def deep_researcher(self) -> Agent:
        return Agent(
            config=self.agents_config["deep_researcher"],
            verbose=True,
            tools=[self.search_tool, self.scrape_tool],
            llm=self.llm
        )

    @agent
    def technical_writer(self) -> Agent:
        return Agent(
            config=self.agents_config["technical_writer"],
            verbose=True,
            llm=self.llm
        )

    # ---------------- Tasks ----------------

    @task
    def clarify_requirements_task(self) -> Task:
        return Task(
            config=self.tasks_config["clarify_requirements_task"],
            human_input=True
        )

    @task
    def research_plan_task(self) -> Task:
        return Task(
            config=self.tasks_config["research_plan_task"]
        )

    @task
    def conduct_research_task(self) -> Task:
        return Task(
            config=self.tasks_config["conduct_research_task"],
            tools=[self.search_tool, self.scrape_tool]
        )

    @task
    def write_report_task(self) -> Task:
        return Task(
            config=self.tasks_config["write_report_task"],
            output_file="output/research_report.md"
        )

    # ---------------- Crew ----------------

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
            cache=True,
            max_rpm=10,
            tracing=True
        )




if __name__ == "__main__":
    # Example usage for testing
    crew = DeepResearchCrew()
    topic = input("Enter the topic: ")
    result = crew.crew().kickoff(
        inputs={"topic": topic}
    )
    print(result)
