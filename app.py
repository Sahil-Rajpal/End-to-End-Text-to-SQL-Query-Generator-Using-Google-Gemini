from dotenv import load_dotenv
load_dotenv() # laod all the envoirnment variables
import streamlit as st

import os
import sqlite3
import google.generativeai as genai


# configure api key

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# function to load google gemini model and provide sql query as response

def get_gemini_response(question,prompt):
    # model=genai.GenerativeModel(model_name='gemini-1.0-pro')
    model = genai.GenerativeModel('models/gemini-1.5-flash')

    response=model.generate_content([prompt[0],question])
    return response.text


## function to retrieve query from sql database

def read_sql_query(sql,db):
    conn=sqlite3.connect(db)
    cur=conn.cursor()
    cur.execute(sql)
    rows=cur.fetchall()
    conn.commit()
    conn.close()
    for row in rows:
        print(row)
    return rows



## Define Your Prompt
prompt=[
    """
    You are an expert in converting English questions to SQL query!
    The SQL database has the name STUDENT and has the following columns - NAME, CLASS, 
    SECTION and MARKS \n\nFor example,\nExample 1 - How many entries of records are present?, 
    the SQL command will be something like this SELECT COUNT(*) FROM STUDENT ;
    \nExample 2 - Tell me all the students studying in Data science class?, 
    the SQL command will be something like this SELECT * FROM STUDENT 
    where CLASS="Data science"; 
    also the sql code should not have ``` in beginning or end and sql word in output

    """


]



## Streamlit App

st.set_page_config(page_title="I can Retrieve Any SQL query")
st.header("Gemini App To Retrieve SQL Data")

question=st.text_input("Input: ",key="input")

submit=st.button("Ask the question")

# if submit is clicked
if submit:
    response=get_gemini_response(question,prompt)
    print(response)
    data=read_sql_query(response,"student.db")
    st.subheader("The Response is")
    for row in data:
        print(row)
        st.header(row)








# import google.generativeai as genai
# import os
# from dotenv import load_dotenv

# load_dotenv()
# genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# # TEMPORARY: List available models to test access
# models = genai.list_models()
# for model in models:
#     print(f"Model name: {model.name}")
#     print(f"  Description: {model.description}")
#     print(f"  Supported generation methods: {model.supported_generation_methods}")
#     print()