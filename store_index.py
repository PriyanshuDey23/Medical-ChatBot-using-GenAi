# Store index process

from src.helper import load_pdf_file,text_split,google_embeddings
from pinecone import Pinecone, ServerlessSpec
from langchain_pinecone import PineconeVectorStore
import os
from dotenv import load_dotenv

# Set Environment variable

load_dotenv()
# Load the api
PINECONE_API_KEY=os.environ.get('PINECONE_API_KEY')

# Load The Google Api key
GOOGLE_API_KEY = os.environ.get('GOOGLE_API_KEY')

# Extract data
extracted_data=load_pdf_file(data='Data/')

# Create Chunks
text_chunks=text_split(extracted_data)

# Embedding
embeddings=google_embeddings()

# Pinecone Initialization

# We will create and push the embedding with the help of python code

pc = Pinecone(api_key=PINECONE_API_KEY)

index_name = "medicalbot"


pc.create_index(
    name=index_name,
    dimension=768, 
    metric="cosine", 
    spec=ServerlessSpec(
        cloud="aws", 
        region="us-east-1"
    ) 
) 

# Embed each chunk and insert the embeddings into your Pinecone index.

docsearch= PineconeVectorStore.from_documents(text_chunks,embeddings,index_name=index_name)