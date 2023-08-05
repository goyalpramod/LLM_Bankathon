from dotenv import load_dotenv, find_dotenv
import openai
import os
from PyPDF2 import PdfReader
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage, AIMessage

load_dotenv(find_dotenv())
openai.api_key = os.environ["OPENAI_API_KEY"]
# from resume_parser import resumeparse
# os.environ["OPENAI_API_KEY"] = ""
data=''
with open("transcript.txt", 'r') as transcript:
    lines=transcript.readlines()
    data="\n".join(lines)
# data=resumeparse.read_file("Samarth_resume.pdf")
# print(text)
# print(data)



chat = ChatOpenAI(temperature=0.0, model_name="gpt-3.5-turbo-16k")
jd="Mechanical Engineer intern"
system_prompt = f"""
You are an AI model that scores Answers given by candidates to a a job interview. 
Both question and it's answer given by interviewee will be provided to you in the form of a transcript. 
There may be some words spelled wrong or joined words or some other formatting issue as they been converted from speech to text, try and fix them yourself. 

The most important scoring criteria is relevance the to the job description {jd} and correctness of the answer
Maximum score of each answer can be 20
only return question number with its score. 
Output should be like: 
    Q1 <starting20 characters of question> -> 15
    Q2 <starting20 characters of question> -> 13
    Q3 <starting20 characters of question> -> 12
    .
    .
    .
    Q20 <starting20 characters of question> -> 18
    sum : <sum of all of the score>

DO not overscore or underscore. Keep it realistic. 
DO NOT alter or summarize the question while providing the output. Keep it as it was. 
IMPORTANT do not reply with "As an AI model..." under any circumstances 
"""


def func_():
    store = chat(
        [
            SystemMessage(content=system_prompt),
            HumanMessage(content=data)
        ]
    )
    return store

store = func_()
print(store.content)
