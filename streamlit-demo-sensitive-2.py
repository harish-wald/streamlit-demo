import streamlit as st
import torch 
from transformers import AutoModelForSequenceClassification
from transformers import AutoTokenizer

st.title('Sensitive Prompt Detection - Finetuned model')

input = st.text_area('Prompt', 'Enter input prompt')

# Load the model (only executed once!)
# NOTE: Don't set ttl or max_entries in this case
@st.cache_resource
def load_model():
	  return AutoModelForSequenceClassification.from_pretrained("Harish-wald/sensitive-bert",token="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", num_labels=2)

@st.cache_resource
def load_tokenizer():
	  return AutoTokenizer.from_pretrained("bert-base-uncased")

model = load_model()

model.eval()

tokenizer = load_tokenizer()

def run_prompt():
    tokenized_input = tokenizer([input], padding="max_length", truncation=True,return_tensors='pt')
    output = model.forward(**tokenized_input)
    st.subheader('Output: ')
    label = torch.argmax(output['logits']).tolist()
    output = 'non-confidential'
    if label:
        output = 'confidential'

    st.write(output)

st.button('Run', on_click=run_prompt)

