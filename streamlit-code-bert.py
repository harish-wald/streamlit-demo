import streamlit as st
from transformers import pipeline
import torch 
from transformers import AutoModelForSequenceClassification
from transformers import AutoTokenizer

st.title('Code Prompt Detection - Finetuned model')

input = st.text_area('Prompt', 'Enter input prompt')

# Load the model (only executed once!)
# NOTE: Don't set ttl or max_entries in this case
@st.cache_resource
def load_model():
	  return AutoModelForSequenceClassification.from_pretrained("Harish-wald/code-bert",token="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", num_labels=2)

@st.cache_resource
def load_tokenizer():
	  return AutoTokenizer.from_pretrained("Harish-wald/code-bert")

model = load_model()

model.eval()

tokenizer = load_tokenizer()

def run_prompt():
    tokenized_input = tokenizer([input], padding="max_length", truncation=True,return_tensors='pt')
    output = model.forward(**tokenized_input)
    st.subheader('Output: ')
    label = torch.argmax(output['logits']).tolist()
    output = 'no-code'
    if label:
        output = 'code'

    st.write(output)

st.button('Run', on_click=run_prompt)

