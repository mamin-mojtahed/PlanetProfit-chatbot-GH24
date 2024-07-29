from langchain_community.document_loaders import PyPDFLoader
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from langchain_openai import ChatOpenAI
import streamlit as st

def ask(info_input: str) -> str:
    apikey = st.secrets["OPENAI_API_KEY"]

    pdf_file_path = 'Climate_Sustainability_Programs.pdf'
    loader = PyPDFLoader(pdf_file_path)
    pages = loader.load_and_split()

    # print(pages[0])

    embeddings = OpenAIEmbeddings(api_key = st.secrets["OPENAI_API_KEY"])
    vectorstore = FAISS.from_documents(pages, embedding=embeddings)

    llm = ChatOpenAI(model= "gpt-3.5-turbo", temperature = 0.7, api_key=apikey)

    memory = ConversationBufferMemory(memory_key='chat_history', return_messages=True)

    conversation_chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        chain_type="stuff",
        retriever=vectorstore.as_retriever(),
        memory=memory
    )

    personal_info = info_input

    query = f"You are a program reccomendation assistant designed to help citizens of the Kitchener City find out what climat and sustainability programs they are eligible for and how much they can benefit from these programs. You have been provided a list of all of the programs available including eligibility requirements and a description of each initiative. Your task is to provide me with a list of the top 5 programs best suited to me and how I can use these to initiatives to save money. Here are some details about me: {personal_info}."
    result = conversation_chain({"question": query})
    answer = result["answer"]

    print(answer)

    # Chatbot
    # Define a function to generate responses
    def get_response(input_text):
        # Simple echo bot
        return f"Echo: {input_text}"
    
    return answer
