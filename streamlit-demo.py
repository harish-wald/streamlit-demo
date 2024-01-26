
import streamlit as st

import openai
openai.api_key = st.secrets["OPENAI_API_KEY"]

from openai import OpenAI
client = OpenAI()


st.title('Sensitive Prompt Detection')

input = st.text_area('Prompt', 'Enter input prompt')

few_shot_prompt = """Classify following input as confidential or non-confidential. Input is confidential if it has sensitive data about a person or company or any assertions. 
    Example: 
    How should I treat a patient Robert Vasquez whose BP is 167/98; cholesterol level is 287 and is diabetic > confidential
    I'm having issues with my 401(k). Who should I contact? > confidential
    How do I apply for medical leave? > confidential
    My manager is harassing me. How should I deal with HR? > confidential
    I need to convert a Dolby Vision XML from 24 to 25 fps. What's the command? > non-confidential
    What is coca colas stock symbol? > non-confidential
    Where is Intel's headquarters based? > non-confidential
    """

few_shot_prompt = few_shot_prompt + input + ' >'


def run_prompt():
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a privacy expert skilled in detecting data leaks"},
            {"role": "user", "content": few_shot_prompt}
            ]
            )
    st.subheader('Output: ')
    st.write(completion.choices[0].message.content)
st.button('Run', on_click=run_prompt)


