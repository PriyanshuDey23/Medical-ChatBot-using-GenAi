from flask import Flask , render_template ,jsonify ,request
from src.helper import google_embeddings
from pinecone import Pinecone, ServerlessSpec
from langchain_pinecone import PineconeVectorStore
from langchain_google_genai import GoogleGenerativeAIEmbeddings # Embedding Model
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from src.prompt import *
import os


app = Flask(__name__)

# Set Environment variable

load_dotenv()
# Load the api
PINECONE_API_KEY=os.environ.get('PINECONE_API_KEY')

# Load The Google Api key
GOOGLE_API_KEY = os.environ.get('GOOGLE_API_KEY')

# Embedding
embeddings=google_embeddings()

# Load Existing index from Database

from langchain_pinecone import PineconeVectorStore

index_name = "medicalbot"

docsearch = PineconeVectorStore.from_existing_index(
    index_name=index_name,
    embedding=embeddings
)


# Retriver 
retriever = docsearch.as_retriever(search_type="similarity", search_kwargs={"k":3}) # For showing 3 results

# Initialize the LLm
llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro-002",temperature=0.3, max_tokens=500)

# Prompt from src\prompt.py
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system_prompt),
        ("human", "{input}"),
    ]
)


question_answer_chain = create_stuff_documents_chain(llm, prompt)
rag_chain = create_retrieval_chain(retriever, question_answer_chain)

# Default Route (interface)
@app.route("/")
def index():
    return render_template('chat.html')

# Chat Operation
@app.route("/get", methods=["GET", "POST"])
def chat():
    msg = request.form["msg"] # Message
    input = msg
    print(input)
    response = rag_chain.invoke({"input": msg}) # Give to rag chain
    print("Response : ", response["answer"])
    return str(response["answer"]) # Print




if __name__ == '__main__':
    app.run(host="0.0.0.0", port= 8080, debug= True)