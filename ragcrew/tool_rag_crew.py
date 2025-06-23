from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from crewai_tools import PDFSearchTool
from typing import List

@CrewBase
class ToolRagCrew:

    agents: List[BaseAgent]
    tasks: List[Task]

    def __init__(self,pdf_path):
        self.pdf_tool = None
        self.pdf_path=pdf_path

    def getPDFRagTool(self):
        if self.pdf_tool is None:
            self.pdf_tool = PDFSearchTool(pdf=self.pdf_path,
                                          #chunker=dict(chunk_size=2000,chunk_overlap=50)
                                          )
        return self.pdf_tool

    @agent
    def pdf_researcher(self) -> Agent:
        return Agent(
            config=self.agents_config['pdf_researcher'],  # type: ignore[index]
            verbose=True,
            tools=[self.getPDFRagTool()],
        )

    @agent
    def content_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config['content_analyst'],  # type: ignore[index]
            verbose=True,
            tools=[self.getPDFRagTool()],
        )

    @task
    def research_task(self) -> Task:
        return Task(
            config=self.tasks_config['research_task'],  # type: ignore[index]
        )

    @task
    def content_task(self) -> Task:
        return Task(
            config=self.tasks_config['content_task'],  # type: ignore[index]
            output_file='./report.md'
        )

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )
