import warnings
from ragcrew.tool_rag_crew import ToolRagCrew
from ragcrew.pdf_knowledge_crew import PDFKnowledgeCrew
from ragcrew.faiss_rag_crew import FAISSRagCrew
from dotenv import load_dotenv

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

def runToolRagCrew(topic='All recipes with rice',pdf_path='./knowledge/Easy_recipes.pdf'):
    """
    Run the crew.
    """
    load_dotenv()
    inputs = {
        'topic': topic,
    }
    
    try:
        output=ToolRagCrew(pdf_path).crew().kickoff(inputs=inputs)
        print(output.token_usage)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


def runPDFKnowledgeCrew(topic='All recipes with rice',pdf_path='./Easy_recipes.pdf'):
    """
    Run the crew.
    """
    load_dotenv()
    inputs = {
        'topic': topic,
    }

    try:
        output=PDFKnowledgeCrew([pdf_path]).crew().kickoff(inputs=inputs)
        print(output.token_usage)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")

def runFAISSRagCrew(topic='All recipes with rice',pdf_path='./knowledge/Easy_recipes.pdf'):
    inputs = {
        'topic': topic,
    }
    output=FAISSRagCrew(pdf_path).crew().kickoff(inputs=inputs)
    print(output.token_usage)



if __name__ == "__main__":
    load_dotenv()
    #runFAISSRagCrew(topic='Recipes where rice is the main ingredient')
    #runFAISSRagCrew()
    #runToolRagCrew(topic='Recipes where rice is the main ingredient')
    runToolRagCrew()
    #runPDFKnowledgeCrew(topic='Recipes where rice is the main ingredient')
    #runPDFKnowledgeCrew()
