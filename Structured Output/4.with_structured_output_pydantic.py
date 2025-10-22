from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from pydantic import BaseModel, Field
from typing import TypedDict, Optional, Literal
import pprint

load_dotenv()

model = ChatOpenAI()


# Review
class Review(BaseModel):
    summary: str = Field(description="A brief funny summary of the review")
    sentiment: Literal["pos", "neg"] = Field(
        description="Return sentiment of the review either neagtive, positive or neutral"
    )
    key_themes: list[str] = Field(
        description="Write down all the key themes discussed in the review"
    )
    pros: Optional[list[str]] = Field(
        description="Write down all the pros inside a list"
    )
    cons: Optional[list[str]] = Field(
        description="Write down all the cons inside a list"
    )


structured_output = model.with_structured_output(Review)

result = structured_output.invoke(
    """ The hardware is great, but the software feels bloated.
                                  There are too many pre-installed apps taht I can't remove. ALso, the UI looks outdated
                                  compared to other brands, Hoping for a software update to fix this"""
)



