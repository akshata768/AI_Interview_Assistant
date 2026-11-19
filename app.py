import streamlit as st
from groq import Groq
st.set_page_config(page_title = "AI_Interview_Assistant", layout = "centered")
st.title("AI_Interview_Assistant")
st.caption("practice and prepare")
st.caption("Launched by AKSHATA")
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
if st.button("Generate AI Responace", type ="primary"):
  if mode in ['Evaluate Answer', 'Improve Answer'] and (not question.strip() or not answer.strip()):
    st.warning("please enter a valid Question and Answer")
    st.stop() 
  topics = "Topic is " + topic + "Difficulty is " + level
  if mode == "Generate Question":
    task = "Generate " + str(count) + " Frequently asked Interview Question, 2 senariow."
  elif mode == "Generate Code Question":
    task = "Generate " + str(count) + " Frequently asked Interview Question on the  topic" + topic + " and given hints to slove them."
  elif mode == "Evalute Answer":
    task =  "Question : " + question + " My Answer : " + answer + "Evalute this answer."
  elif mode == "Improve Answer":
     task = "Question : " + question + " My Answer : " + answer + "Improve this answer."
     bankground = "Job role : " +role+ " Difficulty level "+level
     with st.spinner("Generating your answer ... "):
       try:
         reponse = client.chat.completions.create(
           model = ren_model,
           messages = [{"role":"sytem",
                        "content":"Act as a Senior Interviwer, both HR and Technical exper"},
                        {"role": "user",
                        "content" : background + task }],
           temprature = 0.7,
           max_tokens = 1800 )
          output = reponse.choices[0].message.content
         st.subheader("AI Response ")
         st.markdown(output)
         st.download_button("Download Response", output , file_name = "Interview_Response.txt", mime = 'text/plain')
           except E xception as e:
             st.error ("API connection was unsuccessful", e)
             st.info ("please check your API key and rate limits")
 st.caption("Powered by Streamlit.io and Github. using llm api")
    
  
  
