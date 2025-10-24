from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import (
    RunnableBranch,
    RunnableLambda,
)
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import Literal

from dotenv import load_dotenv

load_dotenv()


class Feedback(BaseModel):

    sentiment: Literal["Positive", "Negative"] = Field(
        description="Sentiment of Feedback"
    )


model = ChatOpenAI()

parser = StrOutputParser()
pydantic_feedback_parser = PydanticOutputParser(pydantic_object=Feedback)

sentiment_classification_prompt = PromptTemplate(
    name="Sentiment Classification Prompt",
    template="Classify the sentiment of the following feedback text into positive or neagtive\n {feedback} \n {format_instruction}",
    input_variables=["feedback"],
    validate_template=True,
    partial_variables={
        "format_instruction": pydantic_feedback_parser.get_format_instructions()
    },
)

classifier_chain = sentiment_classification_prompt | model | pydantic_feedback_parser

positive_resposne_prompt = PromptTemplate(
    name="Positive Response Prompt",
    template="Write an approprite resposne to this positive feedback \n {feedback}",
    input_variables=["feedback"],
    validate_template=True,
)

negative_resposne_prompt = PromptTemplate(
    name="Positive Response Prompt",
    template="Write an approprite resposne to this negative feedback \n {feedback}",
    input_variables=["feedback"],
    validate_template=True,
)


branch_chain = RunnableBranch(
    (lambda x:x.sentiment == "Positive", positive_resposne_prompt | model | parser),
    (lambda x:x.sentiment == "Negative", negative_resposne_prompt | model | parser),
    RunnableLambda(lambda x: "could not find sentiment"),
)

chain = classifier_chain | branch_chain

result = chain.invoke({"feedback": "Not a good phone"})
print(result)
