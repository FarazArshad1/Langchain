from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import TypedDict, Annotated, Optional, Literal

load_dotenv()

model = ChatOpenAI()


# Review
class Review(TypedDict):
    summary: Annotated[str, "A brief funny summary of the review"]
    sentiment: Annotated[Literal["pos","neg"], "Return sentiment of the review either neagtive, positive or neutral"]
    key_themes: Annotated[list[str],"Write down all the key themes discussed in the review"]
    pros: Annotated[Optional[list[str]],"Write down all the pros inside a list"]
    cons: Annotated[Optional[list[str]],"Write down all the cons inside a list"]

structured_output = model.with_structured_output(Review)

result = structured_output.invoke(
    """ The hardware is great, but the software feels bloated.
                                  There are too many pre-installed apps taht I can't remove. ALso, the UI looks outdated
                                  compared to other brands, Hoping for a software update to fix this"""
)


print(result)
