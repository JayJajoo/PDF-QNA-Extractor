import streamlit as st
from PyPDF2 import PdfReader
from dotenv import load_dotenv
import os
import time
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from langchain.llms import HuggingFaceEndpoint
from HTMLTemplates import html_sender, html_bot

load_dotenv()

HUGGINGFACEHUB_API_TOKEN = os.getenv("HUGGINGFACEHUB_API_TOKEN")

def get_text(pdfs):
    text = ""
    for pdf in pdfs:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text


def get_chunks(text):
    splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len,
        is_separator_regex=False
    )
    return splitter.split_text(text)


def get_vectorStore(chunks):
    model_name = "hkunlp/instructor-xl"
    embedding_model = HuggingFaceEmbeddings(model_name=model_name)
    time_start = time.time()
    vector_store = FAISS.from_texts(texts=chunks, embedding=embedding_model)
    time_end = time.time()
    st.write(f"Time Taken: {time_end - time_start:.2f}s")
    return vector_store



def get_conversation(vector_store):
    
    memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
    
    llm = HuggingFaceEndpoint(
        repo_id="mistralai/Mistral-Nemo-Instruct-2407",
        task="text-generation",
        huggingfacehub_api_token=HUGGINGFACEHUB_API_TOKEN
    )

    conversation_chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=vector_store.as_retriever(),
        memory=memory
    )

    return conversation_chain


def handleUserInput(question):
    if st.session_state.conversation is not None:
        response = st.session_state.conversation({"question": question})
        return response["chat_history"]  
    else:
        st.write("No conversation state initialized.")

def render_message(message, sender="user"):
    if sender == "user":
        html = html_sender.replace("{{MESSAGE}}", str(message))
    else:
        html = html_bot.replace("{{MESSAGE}}", str(message))
    
    st.markdown(html, unsafe_allow_html=True)


def main():
    os.environ["TRANSFORMERS_CACHE"] = os.getenv("TRANSFORMERS_CACHE")  # Get from .env

    st.set_page_config(page_title="QNA Bot", page_icon=":books:")
    st.header("Chat")

    if "conversation" not in st.session_state:
        st.session_state.conversation = None

    user_question = st.text_area(label="Ask a question")
    if user_question:
        chats = handleUserInput(user_question)
        chats = chats[::-1]
        for i in range(0,len(chats),2):
            chats[i],chats[i+1] = chats[i+1],chats[i]

        for chat in chats:
            if chat.type == "human":
                render_message(chat.content, sender="user")
            else:
                render_message(chat.content, sender="bot")

    with st.sidebar:
        st.subheader("Your Documents")
        pdfs = st.file_uploader("Upload PDF's here and click process.", accept_multiple_files=True, type=["pdf", "docx", "doc"])
        if st.button("Process"):
            with st.spinner("Loading"):
                text = get_text(pdfs)
                text_chunks = get_chunks(text)
                vector_store = get_vectorStore(text_chunks)
                st.session_state.conversation = get_conversation(vector_store=vector_store)


if __name__ == "__main__":
    main()
