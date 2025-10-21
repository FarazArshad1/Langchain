from langchain_openai import OpenAI
from dotenv import load_dotenv
import streamlit as st

from langchain_core.prompts.loading import load_prompt

model = OpenAI()

st.header('Research Tool')

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

# Template for the prompt

template = load_prompt('template.json')

# Fill the placeholders in the template with user inputs
prompt = template.invoke({
    "paper_input": paper_input,
    "style_input": style_input,
    "length_input": length_input
})

if st.button('Summarize'):
    result = model.invoke(prompt)
    st.write(result)