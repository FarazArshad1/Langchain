from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableSequence, RunnableParallel
from dotenv import load_dotenv

load_dotenv()

tweet_generator_prompt = PromptTemplate(
    name="Generate Tweet Template",
    template="Write a tweet about {topic}",
    input_variables=["topic"],
    validate_template=True,
)

linkedin_post_generator_prompt = PromptTemplate(
    name="Generate linkedin Template",
    template="Write a linkedin about {topic}",
    input_variables=["topic"],
    validate_template=True,
)

model = ChatOpenAI()
parser = StrOutputParser()

parallel_Chain = RunnableParallel(
    {
        "tweet": RunnableSequence(tweet_generator_prompt, model, parser),
        "linkedin_post": RunnableSequence(
            linkedin_post_generator_prompt, model, parser
        ),
    }
)

posts = parallel_Chain.invoke(
    {"topic": "I passed AWS Solutions Architect Associate Exam"}
)


print(posts)
