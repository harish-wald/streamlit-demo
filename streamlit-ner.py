from transformers import AutoTokenizer, AutoModelForTokenClassification
from transformers import pipeline
import streamlit as st

@st.experimental_singleton
def load_model():
    tokenizer = AutoTokenizer.from_pretrained("dslim/bert-base-NER")
    model = AutoModelForTokenClassification.from_pretrained("dslim/bert-base-NER")
    return pipeline("ner", model=model, tokenizer=tokenizer)



st.title('Named entity detection')

example = st.text_area('Prompt', 'Enter input prompt')

def run_prompt():
    nlp = load_model()
    ner_results = nlp(example)

    result_map = {}
    i =0
    j=1
    merged_list=[]
    print(ner_results)
    while j < len(ner_results):
        print(ner_results[j])
        person = ('PER' in ner_results[j]['entity'] and 'PER' in ner_results[j-1]['entity'])
        org = ('ORG' in ner_results[j]['entity'] and 'ORG' in ner_results[j-1]['entity'])
        print(person)
        print(org)
        if ner_results[j]["start"] == ner_results[j-1]["end"] and (person or org):
            j+=1
        else:
            result ={}
            result["start"]=ner_results[i]['start']
            result["end"]=ner_results[j-1]['end']
            result["word"] = example[result["start"]:result["end"]]
            person = ('PER' in ner_results[j-1]['entity'])
            org = ('ORG' in ner_results[j-1]['entity'])
            print(result)
            if person:
                result['entity']='person'
            if org:
                result['entity']='company'
            merged_list.append(result)
            i=j
            j+=1

    if j==len(ner_results):
        person = 'PER' in ner_results[j-1]['entity']
        org = 'ORG' in ner_results[j-1]['entity'] 
        result ={}
        result["start"]=ner_results[i]['start']
        result["end"]=ner_results[j-1]['end']
        result["word"] = example[result["start"]:result["end"]]
        if person:
             result['entity']='person'
        if org:
            result['entity']='company'
        merged_list.append(result)

    for result in merged_list:
        if 'entity' not in result:
            continue
        print(result)
        word = result["word"]
        print(word)
        result_map[word] = result["entity"]

    st.subheader('Output: ')
    print(result_map)
    st.write(result_map)

st.button('Run', on_click=run_prompt)


