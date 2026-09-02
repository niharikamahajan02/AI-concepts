from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

st.header("Summary Tool")

llm = HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-V3-0324",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)

user_in = st.text_input("Enter prompt")

if st.button("Summarize"):
    if user_in:
        res = model.invoke(user_in)
        st.write(res.content)
    else:
        st.warning("Please enter a prompt")