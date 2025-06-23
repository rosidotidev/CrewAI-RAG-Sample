from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from crewai.knowledge.source.pdf_knowledge_source import PDFKnowledgeSource
from typing import List

@CrewBase
class PDFKnowledgeCrew:

    agents: List[BaseAgent]
    tasks: List[Task]

    def __init__(self,pdf_paths):
        self.pdf_source = None
        self.pdf_paths=pdf_paths

    def get_knowledge_sources(self):
        if self.pdf_source is None:
            self.pdf_source = PDFKnowledgeSource(file_paths=self.pdf_paths)
        return self.pdf_source

    @agent
    def pdf_researcher(self) -> Agent:
        return Agent(
            config=self.agents_config['pdf_researcher'],  # type: ignore[index]
            verbose=True,
            knowledge_sources=[self.get_knowledge_sources()]
        )

    @agent
    def content_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config['content_analyst'],  # type: ignore[index]
            verbose=True,


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
            #knowledge_sources=[self.get_knowledge_sources()]
        )
