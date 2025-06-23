from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
import pdfplumber
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from openai import OpenAI
from typing import List
from langchain_openai import OpenAIEmbeddings  # 👈 nuovo import
from ragcrew.tools.custom_tool import PDFFAISSTool


@CrewBase
class FAISSRagCrew:

    agents: List[BaseAgent]
    tasks: List[Task]

    def __init__(self,pdf_path):
        self.pdf_path=pdf_path
        self.vector_store= None
        self.client=OpenAI()
        self.search_tool=None

    def get_openai_embedding(self,text):
        response = self.client.embeddings.create(
            input=text,
            model="text-embedding-3-small"
        )
        return response.data[0].embedding

    def load_pdf(self):
        with pdfplumber.open(self.pdf_path) as pdf:
            return " ".join(page.extract_text() for page in pdf.pages)

    def prepare_rag(self,pdf_text):
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=2000,
            chunk_overlap=200
        )
        chunks = text_splitter.split_text(pdf_text)
        return FAISS.from_texts(chunks, OpenAIEmbeddings())

    def initFAISS(self):
        pdf_text = self.load_pdf()
        self.vector_store = self.prepare_rag(pdf_text)
        self.search_tool = PDFFAISSTool(self.vector_store)

    @agent
    def pdf_researcher(self) -> Agent:
        self.initFAISS()
        return Agent(
            config=self.agents_config['pdf_researcher'],  # type: ignore[index]
            verbose=True,
            tools=[self.search_tool]
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

        )
