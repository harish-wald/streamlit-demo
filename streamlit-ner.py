from transformers import AutoTokenizer, AutoModelForTokenClassification
from transformers import pipeline
import streamlit as st

@st.cache_resource
def load_model():
    tokenizer = AutoTokenizer.from_pretrained("dslim/bert-base-NER")
    model = AutoModelForTokenClassification.from_pretrained("dslim/bert-base-NER")
    return pipeline("ner", model=model, tokenizer=tokenizer)



st.title('Named entity detection')

example = st.text_area('Prompt', 'Enter input prompt')

def run_prompt():
    nlp = load_model()
    ner_results = nlp(example)
    result_list = []
    for result in ner_results:
        result_list+=[result["word"]]
    st.subheader('Output: ')
    print(ner_results)
    st.write(result_list)

st.button('Run', on_click=run_prompt)


