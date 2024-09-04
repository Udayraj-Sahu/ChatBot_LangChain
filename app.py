#LANGCHAIN_API_KEY= "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"
#LANGCHAIN_PROJECT="CHATBOT"
#NEWS_API_KEY= "269690daf24141a295ef1ce43d8184f3"
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama


import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()



## Langsmith Tracking

os.environ['LANGCHAIN_API_KEY'] = os.getenv('LANGCHAIN_API_KEY')
os.environ['LANGCHAIN_TRACING_V2'] = "true" 

## Creating ChatBot

prompt = ChatPromptTemplate.from_messages([
    ("system","You are a helpful assisstant. Please provide response to the user."),
    ("user","Question:{question}")
])

## Streamlit framework

st.title("LangChain Demo With Ollama API")
input_text = st.text_input("Search the Topic you want")


## Open AI LLM call

llm = Ollama(model='gemma2:2b')
output_parser = StrOutputParser()

#Chain

chain = prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({'question':input_text}))