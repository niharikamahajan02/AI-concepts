from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import PromptTemplate

load_dotenv()

st.header("Summary Tool")

llm = HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-V3-0324",
    task="text-generation"
)
i1=st.selectbox("slect option",['option1','optionh2'])
i2=st.selectbox("slect option",['option1','option2'])
model = ChatHuggingFace(llm=llm)

#make prompt template
template=PromptTemplate(
    template="""use here {i1}then here {i2}""",

    input_variables=['i1','i2']

)
#fill prompt template
prompt=template.invoke({
    'i1':i1,
    'i2':i2
})
user_in = st.text_input("Enter prompt")

if st.button("Summarize"):
    if user_in:
        res = model.invoke(prompt)
        st.write(res.content)
    else:
        st.warning("Please enter a prompt")