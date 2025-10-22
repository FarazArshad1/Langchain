from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from pydantic import BaseModel, Field
from typing import TypedDict, Optional, Literal
import pprint

load_dotenv()

model = ChatOpenAI()


# Schema

json_schema = {
    "title": "Review",
    "type": "object",
    "properties": {
        "key_themes": {
            "type": "array",
            "items": {"type": "string"},
            "description": "Write down all the key themes discussed in the review in a list",
        },
        "summary": {"type": "string", "description": "A brief summary of the review"},
        "sentiment": {
            "type": "string",
            "enum": ["pos", "neg"],
            "description": "Return sentiment of the review either negative, positive or neutral",
        },
        "pros": {
            "type": ["array", "null"],
            "items": {"type": "string"},
            "description": "Write down all the pros inside a list",
        },
        "cons": {
            "type": ["array", "null"],
            "items": {"type": "string"},
            "description": "Write down all the cons inside a list",
        },
        "name": {
            "type": ["string", "null"],
            "description": "Write the name of the reviewer",
        },
    },
    "required": ["key_themes", "summary", "sentiment"],
}

structured_output = model.with_structured_output(json_schema)

result = structured_output.invoke(
    """ The hardware is great, but the software feels bloated.
                                  There are too many pre-installed apps taht I can't remove. ALso, the UI looks outdated
                                  compared to other brands, Hoping for a software update to fix this"""
)


print(result)