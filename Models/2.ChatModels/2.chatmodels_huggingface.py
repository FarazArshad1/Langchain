from typing import *

from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()

def printError(e):
    import sys
    error_type = type(e).__name__  
    line_number = sys.exc_info()[-1].tb_lineno
    if e.args:
        error_name = e.args[0]
    else:
        error_name = "No additional information available"
    error_msg = f"Error Type: {error_type}\nError Name: {error_name}\nLine where error occurred: {line_number}"
    print(error_msg)

llm = HuggingFaceEndpoint(
    repo_id='TinyLlama/TinyLlama-1.1B-Chat-v1.0',
    task='text-generation',
)

model = ChatHuggingFace(llm=llm)

def huggingface_model_invocation(prompt:str):
    try:
        result=model.invoke(prompt)
        return result
    except Exception as e:
        printError(e)
        return None

prompt = 'what is deep Learning'
hugging_face_result = huggingface_model_invocation(prompt=prompt)
print(hugging_face_result)