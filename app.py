import streamlit as st
import os
from dotenv import load_dotenv,dotenv_values
from agents import ResearchAgent
from data_loader import DataLoader

load_dotenv()

config = dotenv_values('.env')
# print(config)

print(os.getenv('OPENAI_API_KEY'),"\n", os.getenv('AZURE_OPENAI_ENDPOINT'))

# Streamlit UI Title 
st.title("My virtual Research Assistant")


groq_api_key = os.getenv('GROQ_API_KEY')

# Check if API key is set , else stop execution
if not groq_api_key:
    st.error("Groq API Key is missing.Please set it in your environment variables")
    st.stop()


# Initialize AI agents for summarization and analysis
agents = ResearchAgent(groq_api_key)

# Initialize DataLoader for fetching research papers
data_loader = DataLoader()


# Input field for the user to enter a reasearch topic
query = st.text_input("Enter a research topic:")



