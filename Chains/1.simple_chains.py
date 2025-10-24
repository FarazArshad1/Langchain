from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()


prompt = PromptTemplate(
    name="First Prompt",
    input_variables=["topic"],
    # output_parser=StrOutputParser(),
    template="Generate 5 interesting facts about {topic}",
)

parser = StrOutputParser()
model = ChatOpenAI()

chain = prompt | model | parser

result = chain.invoke(
    {
        "topic": "cricket",
    }
)


print(result)

# We can visualize the chain using the get_graph() method
chain.get_graph().draw_ascii()