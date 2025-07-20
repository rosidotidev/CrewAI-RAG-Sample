# CrewAI-RAG-Sample
This project uses CrewAI to demonstrate various RAG strategies for LLMs. It compares PDF analysis using native tools (PDFSearchTool, CrewAI Knowledge) and a custom FAISS tool. It's a practical guide to implementing RAG with autonomous agents for enhanced accuracy.

This project aims to show how easy it is to set up different **Retrieval-Augmented Generation (RAG)** strategies using the **CrewAI** framework. You'll see examples of how to:

* **Use CrewAI's built-in `Knowledge` feature** to give agents general information.

* **Employ a dedicated `PDFSearchTool`** for specific searches within PDF documents.

* **Integrate a custom RAG tool** that uses FAISS for advanced, personalized retrieval.

This sample helps you understand the flexibility and power of CrewAI when building intelligent agent systems that need to access external data.

## Getting Started

Follow these simple steps to get the project up and running on your local machine.

### 1. Clone the Repository

First, clone this GitHub repository to your local system:

git clone https://github.com/rosidotidev/CrewAI-RAG-Sample.git
cd CrewAI-RAG-Sample


### 2. Install Dependencies

Next, install all the necessary libraries. We recommend using `pipenv` for environment management.

You'll find the exact commands in the `setup.txt` file located in the project's root directory. For your convenience, here are the common commands you'll likely need to run:

pipenv install crewai crewai_tools python-dotenv langchain langchain-openai faiss-cpu pdfplumber openai


**Note:** If you don't have `pipenv` installed, you can get it by running `pip install pipenv`.

### 3. Set Up Your Environment Variables

Create a file named `.env` in the root of your project directory. Inside this file, add your OpenAI API key. This key is crucial for the Large Language Models (LLMs) to work correctly.

OPENAI_API_KEY="your_openai_api_key_here"


## How to Run

After completing the setup, you can run the main script ('main.py') to see the different RAG strategies in action. Just follow the specific instructions provided within the project's code files for each example.
