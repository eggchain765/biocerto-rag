import os
from langchain.chat_models import ChatOpenAI
from langchain.document_loaders import PyPDFLoader
from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains import RetrievalQA

# Config
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
DATA_PATH = "data"

# Carica documenti PDF
documents = []
for file in os.listdir(DATA_PATH):
    if file.endswith(".pdf"):
        loader = PyPDFLoader(os.path.join(DATA_PATH, file))
        documents.extend(loader.load())

# Split testo
splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
docs = splitter.split_documents(documents)

# Embedding + vector store
embedding = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)
vectorstore = Chroma.from_documents(docs, embedding)

# Retrieval + LLM
qa_chain = RetrievalQA.from_chain_type(
    llm=ChatOpenAI(temperature=0, openai_api_key=OPENAI_API_KEY),
    chain_type="stuff",
    retriever=vectorstore.as_retriever()
)

def chat():
    print("Biocerto.AI (RAG) - Digita 'exit' per uscire.")
    while True:
        query = input("Domanda: ")
        if query.lower() in ["exit", "quit"]:
            break
        risposta = qa_chain.run(query)
        print("Risposta:", risposta)

if __name__ == "__main__":
    chat()
