from langchain_openai import OpenAI
from langchain_core.prompts.loading import load_prompt

import streamlit as st

from dotenv import load_dotenv
load_dotenv()

# Load the OpenAI model

model = OpenAI()

# Streamlit app header
st.header('Research Paper Summary Tool')

paper_input = st.selectbox("Select Reaseach Paper Name",["Select...","Attetion is all  You Need",
                                                         "BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding",
                                                         "XLNet: Generalized Autoregressive Pretraining for Language Understanding",
                                                         "RoBERTa: A Robustly Optimized BERT Pretraining Approach",
                                                         "ALBERT: A Lite BERT for Self-supervised Learning of Language Representations",
                                                         "DistilBERT, a distilled version of BERT: smaller, faster, cheaper, lighter"])

style_input  = st.selectbox("Select Explanation Style",["Begineer Friendly",
                                                       "Technical",
                                                       "Code Oriented",
                                                       "Mathematical",])

length_input = st.selectbox("Select Length of Explanation",["Short","Medium","Long"])

prompt_template = load_prompt('template.json')

if st.button('Summarize'):
    chain = prompt_template | model
    
    result = chain.invoke({
        'paper_input': paper_input,
        'style_input': style_input,
        'length_input': length_input
    }) 
    
    st.write(result)
