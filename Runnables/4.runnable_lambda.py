from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import (
    RunnableLambda,
    RunnableParallel,
    RunnableSequence,
    RunnablePassthrough,
)
from dotenv import load_dotenv

load_dotenv()


def word_counter(text):
    return len(text.split())


model = ChatOpenAI()

parser = StrOutputParser()

joke_generation_template = PromptTemplate(
    name="Generate Joke Template",
    template="Tell me a joke about {topic}",
    input_variables=["topic"],
    validate_template=True,
)

joke_generation_chain = RunnableSequence(
    joke_generation_template, model, parser
)

runnable_word_counter = RunnableLambda(word_counter)

parallel_chain = RunnableParallel(
    {
        "joke": RunnablePassthrough(),
        "word_count": runnable_word_counter
    }
)

final_chain = RunnableSequence(joke_generation_chain, parallel_chain)

results = final_chain.invoke({"topic": "programming"})

print(f"Joke - {results['joke']} \n : Word Count - {results['word_count']}")
