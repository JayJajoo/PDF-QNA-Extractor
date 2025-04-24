# 📚 PDF QA Answer Extractor using LLMs (LangChain + Streamlit)

This project is an intelligent Question-Answering (QA) system that allows users to upload PDF documents and ask natural language questions based on the content. It leverages **LangChain**, **FAISS**, **Hugging Face LLMs**, and **Streamlit** to build an interactive, retrieval-augmented chatbot.

## 🚀 Features

- Upload multiple PDF files
- Extract text from documents
- Split text into manageable chunks
- Generate embeddings using HuggingFace's `instructor-xl` model
- Perform similarity search using FAISS
- Answer user questions using an LLM (`mistralai/Mistral-Nemo-Instruct-2407`)
- Store conversation context with memory
- Clean and responsive UI using Streamlit
- Styled chat interface using custom HTML templates

---

## 🧠 Tech Stack

- **Frontend**: Streamlit
- **Backend**: Python, LangChain
- **Embeddings**: `hkunlp/instructor-xl` via Hugging Face
- **LLM**: `mistralai/Mistral-Nemo-Instruct-2407`
- **Vector Store**: FAISS
- **Document Parsing**: PyPDF2
- **Environment Management**: `python-dotenv`

---

## 📦 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/pdf-qa-bot.git
cd pdf-qa-bot
