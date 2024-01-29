
import streamlit as st

import openai
openai.api_key = st.secrets["OPENAI_API_KEY"]

from openai import OpenAI
client = OpenAI()


st.title('Sensitive Prompt Detection')

input = st.text_area('Prompt', 'Enter input prompt')

few_shot_prompt = """Classify following input as confidential or non-confidential. Input is confidential if it has sensitive data or non public knowledge about a person or company. 
    Example: 
    "How should I treat a patient Robert Vasquez whose BP is 167/98; cholesterol level is 287 and is diabetic" > "confidential"
    "I'm having issues with my 401(k). Who should I contact?" > "confidential"
    "How do I apply for medical leave?" > "confidential"
    "My manager is harassing me. How should I deal with HR?" > "confidential"
    "I need to convert a Dolby Vision XML from 24 to 25 fps. What's the command?" > "non-confidential"
    "What is coca colas stock symbol?" > "non-confidential"
    "Where is Intel's headquarters based?" > "non-confidential"
    "Help me write a press release for the new Dolby Atmos launch planned for March" > "confidential"
    "Help me write a press release for the new colgate whitening toothpaste launch planned for September. It has unique anticavity, antigingivitis, antisensitivity toothpaste formula helps interfere with the harmful effects of plaque bacteria associated with gingivitis for healthy gums" > "confidential"
    "i have frequent headaches. what should i do." > "non-confidential"
    "Is it okay for me to attack Diet Coke in an ad campaign?" > "non-confidential"
    "is apple ceo gay" > "non-confidential"
    "is my boss elon musk married" > "non-confidential"
    """

few_shot_prompt = few_shot_prompt + '\n"'+ input + '" >'


def run_prompt():
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo-1106",
        messages=[
            {"role": "system", "content": ""},
            {"role": "user", "content": few_shot_prompt}
            ]
            )
    st.subheader('Output: ')
    st.write(completion.choices[0].message.content)
st.button('Run', on_click=run_prompt)


