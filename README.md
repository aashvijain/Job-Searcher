# Job Searcher

> **Note:** This project is still a work in progress and will be enhanced in the future.

This is a Python application that uses OpenAI embeddings and vector search to help you search through job listings using natural language queries.

## Features
- Loads job listings from a text file (`job_listings.txt`).
- Splits the listings into manageable chunks for vector search.
- Uses OpenAI embeddings and Chroma vector database for semantic search.
- Enter a query and get relevant job listings printed to the console.

## Requirements
- Python 3.8+
- [langchain](https://python.langchain.com/)
- [langchain-openai](https://python.langchain.com/docs/integrations/llms/openai)
- [langchain-chroma](https://python.langchain.com/docs/integrations/vectorstores/chroma)
- [python-dotenv](https://pypi.org/project/python-dotenv/)

## Setup
1. **Clone the repository**
2. **Install dependencies:**
   ```bash
   pip install langchain langchain-openai langchain-chroma python-dotenv
   ```
3. **Create a `.env` file** in the project root with your OpenAI API key:
   ```env
   OPENAI_API_KEY=your_openai_api_key_here
   ```
4. **Add your job listings** to a file named `job_listings.txt` in the project root.
5. **Run the app:**
   ```bash
   python job_searcher.py
   ```

## Usage
- When prompted, enter your search query (e.g., "remote data analyst jobs in healthcare").
- The app will print out the most relevant job listings.

