from langchain_huggingface import HuggingFaceEndpoint
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

st.header('summary tool')

user_in=st.text_input('enter prompt')

if st.button('summarize'):
    st.text('text random')

    