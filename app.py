import streamlit as st
from groq import Groq
st.set_page_config(page_title = "AI_Interview_Assistant", layout = "centered")
st.title("AI_Interview_Assistant")
st.caption("practice and prepare")
try:
  client = Groq(api_key = st.secrets["GROQ_API_KEY"])
except (keyError, FileNotFoundError):
  st.error("API key is missing.Add it in Advanced settings")
  st.stop()
role = st.selectbox('Job Title', ['Machine Learning Engineer', 'Senior Software Engineer', 'Devops Engineer', 'other'])
if role == "other":
  st.text_input('Enter you Job Title', 'XXXXXXX')
model = st.selectbox('Model', ['openai/gpt-oss-20b','openai/gpt-oss-120b'])
level = st.selectbox('Difficulty', ['Beginer', 'Intermediate', 'Advance'])
mode = st.radio('Activity', ['Generate Question', 'Generate Code Question', 'Evalute Answer', 'Improve Answer']) 
if mode == 'Generate Question':
  count = st.slider( "Number of Question",1,10,5)
elif mode == 'Generate code Quention':
  topic = st.slectbox('Topics',['SQL', 'DBMS', 'AIML', 'DSA', 'C++/C', 'JAVA', 'PYTHON'])
  count = st.slider("Number of Question", 1,10,5)
else:
  question = st.text_area('Enter Interview Question here')
  answer = st.text_area('Enter your answer', height = 160)
  
