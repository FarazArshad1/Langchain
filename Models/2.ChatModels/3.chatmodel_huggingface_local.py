from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
import os

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
    
# Define Location where model will be downloaded
os.environ['HF_HOME'] = 'D://huggingface_cache'

# Download the model locally & then inferece from it
llm = HuggingFacePipeline.from_model_id(
    model_id='TinyLlama/TinyLlama-1.1B-Chat-v1.0',
    task = 'text-generation',
    pipeline_kwargs=dict(
        temperature = 0.5,
        max_new_tokens = 100
    )
)

model = ChatHuggingFace(llm = llm)

def huggingface_model_invocation(prompt:str):
    try:
        result=model.invoke(prompt)
        return result
    except Exception as e:
        printError(e)
        return None

prompt = 'What is capital of Pakistan'
result = huggingface_model_invocation(prompt=prompt)

print(result)