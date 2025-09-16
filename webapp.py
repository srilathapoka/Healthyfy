import streamlit as st
import google.generativeai as genai
import pandas as pd
import os


api=os.getenv('GOOGLE_API_KEY')
genai.configure(api_key=api)
model=genai.GenerativeModel('gemini-2.5-flash-lite')

#lets create the UI
st.title(':orange[HEALTHIFY] :blue[AI powered  personal health assistant]')
st.markdown('''##### this application will assist you to have a better and healthy life.you your health related questions and get personalized guidance.''')
tips='''Follow the steps
* Enter your details in the sidebar.
* Enter your gender,age,height(cms),weight(kgs).
* Select the number on the fitness scale(0-5).5-Fittest and 0-No fitness at all
* After filling the details write your query here and get customised response'''
st.write(tips)

#lets configure sidebar
st.sidebar.header(':red[ENTER YOUR DETAILS]')
name=st.sidebar.text_input('Enter your name')
gender=st.sidebar.selectbox('Select your gender',['Male','Female'])
age=st.sidebar.text_input('Enter your age in years')
weight=st.sidebar.text_input('Enter your weight in kgs')
height=st.sidebar.text_input('Enter you height in cms')
bmi=pd.to_numeric(weight)/(pd.to_numeric(height)/100)**2
fittness=st.sidebar.slider('Rate your fitness between 0-5',0,5,step=1)
st.sidebar.write(f'{name} Your BMI is: {round(bmi,2)} kg/m^2')

#let use genai model to get the output
user_query=st.text_input('Enter your question here')
prompt=f'''Assume you are a health expert. you are required to answer the question asked by the user.
use the fllowing details provided by the user.
name of the user is {name}
gender is {gender}
age is {age}
weight is {weight} kgs
height is {height} cms
bmi is {bmi} kg/m^2
and user rates his/her fittness as {fittness} out of 5

your output should be in the following format
* It start by giving one two line comment on the details that have been provided
* It sholud explain what the real problem is based on the query asked by the user
* What could be the possible reason for the problem.
* What are the possible solutions for he problem
* You can also mention what doctor to see (specialization) if required
* Striclty do not recommend or advise any medicine
* output should be in bullet points and use tables whereever required. 

here is the query from the user {user_query}'''


if user_query:
    response=model.generate_content(prompt)
    st.write(response.text)
