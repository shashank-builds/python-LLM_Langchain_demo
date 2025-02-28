import streamlit
import os
from dotenv import load_dotenv,dotenv_values
from agents import ResearchAgent
from data_loader import DataLoader

load_dotenv()

config = dotenv_values('.env')
# print(config)

print(os.getenv('OPENAI_API_KEY'),"\n", os.getenv('AZURE_OPENAI_ENDPOINT'))

