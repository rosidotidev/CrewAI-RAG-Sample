import sys
import warnings
from datetime import datetime
from toolragcrew.tool_rag_crew import ToolRagCrew
from pdfknowledgecrew.pdf_knowledge_crew import PDFKnowledgeCrew
from faissragcrew.faiss_rag_crew import FAISSRagCrew
from dotenv import load_dotenv

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

def runToolRagCrew(topic='All recipes about with rice',pdf_path='./Easy_recipes.pdf'):
    """
    Run the crew.
    """
    load_dotenv()
    inputs = {
        'topic': topic,
    }
    
    try:
        ToolRagCrew(pdf_path).crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


def runPDFKnowledgeCrew(topic='All recipes about with rice',pdf_path='./Easy_recipes.pdf'):
    """
    Run the crew.
    """
    load_dotenv()
    inputs = {
        'topic': topic,
    }

    try:
        PDFKnowledgeCrew([pdf_path]).crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")

def runFAISSRagCrew(topic='All recipes about with rice',pdf_path='./Easy_recipes.pdf'):
    """
    Run the crew.
    """
    load_dotenv()
    inputs = {
        'topic': topic,
    }

    try:
        FAISSRagCrew(pdf_path).crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


if __name__ == "__main__":
    runPDFKnowledgeCrew()
