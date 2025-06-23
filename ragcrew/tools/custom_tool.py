from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field,PrivateAttr

class PDFQueryInput(BaseModel):
    query: str

class PDFFAISSTool(BaseTool):
    name: str = "PDF_Search"
    description: str = "retrieves informations using FAISS"
    args_schema: Type[BaseModel] = PDFQueryInput

    _vector_store: any = PrivateAttr()

    def __init__(self, vector_store, **kwargs):
        super().__init__(**kwargs)
        self._vector_store = vector_store

    def _run(self, query: str):
        results = self._vector_store.similarity_search(query)
        return "\n".join([res.page_content for res in results])

    def _arun(self, query: str):
        raise NotImplementedError("PDFSearchTool non supporta esecuzione asincrona.")