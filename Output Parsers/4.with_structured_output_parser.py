from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain.output_parsers import StructuredOutputParser, ResponseSchema

load_dotenv()

model = ChatOpenAI()

schema = [
    ResponseSchema(name="fact-1", description="Fact 1 about a Topic"),
    ResponseSchema(name="fact-2", description="Fact 2 about a Topic"),
    ResponseSchema(name="fact-3", description="Fact 3 about a Topic"),
    ResponseSchema(name="fact-4", description="Fact 4 about a Topic"),
    ResponseSchema(name="fact-5", description="Fact 5 about a Topic"),
]

parser = StructuredOutputParser.from_response_schemas(schema)

template = PromptTemplate(
    template = 'Give 5 facts about the {topic} \n {format_instrcution}',
    input_varibales = [],
    partial_variables= {'format_instrcution' : parser.get_format_instructions()}
)


chain = template | model | parser

result = chain.invoke({'topic' : 'black hole'})

print(result)