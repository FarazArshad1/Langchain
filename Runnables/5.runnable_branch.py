from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import (
    RunnableParallel,
    RunnableSequence,
    RunnableBranch,
    RunnablePassthrough,
)
from dotenv import load_dotenv

load_dotenv()

report_generation_prompt = PromptTemplate(
    name="Report Generation Prompt",
    template="Write a detailed report on {topic}",
    input_variables=["topic"],
    validate_template=True,
)

report_summarization_prompt = PromptTemplate(
    name="Report Summarization Prompt",
    template="Summarize the follwowing text -{text}",
    input_variables=["text"],
    validate_template=True,
)

model = ChatOpenAI()

parser = StrOutputParser()

report_generation_chain = RunnableSequence(report_generation_prompt, model, parser)

report_summarization_chain = RunnableSequence(
    report_summarization_prompt, model, parser
)


# Check if size of text is more then 500 characters then generate a summary of that text, else leave it as it is and passthrough
branch_chain = RunnableBranch(
    (lambda x: len(x.split()) > 500, report_summarization_chain),
    RunnablePassthrough()
)

final_Chain = RunnableSequence(report_generation_chain, branch_chain)

result = final_Chain.invoke(
    {
        "topic" : "Nigga History"
    }
)

print(result)




