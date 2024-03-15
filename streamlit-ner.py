from transformers import AutoTokenizer, AutoModelForTokenClassification
from transformers import pipeline
import streamlit as st
from gliner import GLiNER

@st.cache_resource
def load_model():
    return GLiNER.from_pretrained("urchade/gliner_largev2")


st.title('Named entity detection')

example = st.text_area('Prompt', 'Enter input prompt')

labels = ["person", "award", "date", "competitions", "teams", "company"]

def run_prompt():
    model = load_model()
    entities = model.predict_entities(example, labels)

    for entity in entities:
          st.write(entity["text"], "=>", entity["label"])

st.button('Run', on_click=run_prompt)
