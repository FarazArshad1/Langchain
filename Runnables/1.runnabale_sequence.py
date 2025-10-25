from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableSequence
from dotenv import load_dotenv

load_dotenv()

joke_generator_prompt = PromptTemplate(
    name="Generate Joke Template",
    template="Write a joke about {topic}",
    input_variables=["topic"],
    validate_template=True,
)

joke_explainer_prompt = PromptTemplate(
    name="Explain Joke Template",
    template="Explain the following joke - {text}",
    input_variables=["text"],
    validate_template=True,
)

model = ChatOpenAI()

parser = StrOutputParser()

chain = RunnableSequence(
    joke_generator_prompt, model, parser, joke_explainer_prompt, model, parser
)

result = chain.invoke({"topic": "Cricket"})

print(result)
