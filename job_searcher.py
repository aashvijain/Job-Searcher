from dotenv import load_dotenv
import os
from langchain_openai import OpenAIEmbeddings
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma



load_dotenv()  # Loads variables from .env into environment
openai_api_key = os.getenv("OPENAI_API_KEY")
llm = OpenAIEmbeddings(api_key=openai_api_key)
print(f"OpenAI API Key: {openai_api_key}")

document = TextLoader ("job_listings.txt").load()
text_splitter = RecursiveCharacterTextSplitter(chunk_size=200, chunk_overlap=10)
chunks = text_splitter.split_documents(document)

db = Chroma.from_documents(chunks, llm)
retriever = db.as_retriever()

llm = OpenAIEmbeddings(api_key=openai_api_key)

text = input("Enter the query: ")

docs = retriever.invoke(text)
for doc in docs:
    print(doc.page_content)
