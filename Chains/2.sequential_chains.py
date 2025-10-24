from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()


report_prompt = PromptTemplate(
    name="Generate Report",
    input_variables=["topic"],
    template="Generate a detailed report about {topic}",
    validate_template=True,
)

summary_prompt = PromptTemplate(
    name="Generate Summary of Report",
    input_variables=["text"],
    template="Generate a 5 pointer summary from the following text {text}",
    validate_template=True,
)

model = ChatOpenAI()

parser = StrOutputParser()

chain = report_prompt | model | parser | summary_prompt | model | parser

results = chain.invoke(
    {
        "topic": "Unemplyement in Pakistan",
    }
)

print(results)

# Visualize chain in terminal

chain.get_graph().draw_ascii()