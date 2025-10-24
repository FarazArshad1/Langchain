from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableParallel

from dotenv import load_dotenv

load_dotenv()

chat_openai_model = ChatOpenAI()
chat_claude_model = ChatAnthropic(model_name="claude-3-haiku-20240307")

parser = StrOutputParser()

notes_prompt = PromptTemplate(
    name="Notes Generation Template",
    template="Generate short and simple notes from the following text \n {text}",
    input_variables=["text"],
    validate_template=True,
)

quiz_prompt = PromptTemplate(
    name="Quiz Generation Template",
    template="Generate 5 question answer from the following text \n {text}",
    input_variables=["text"],
    validate_template=True,
)

merged_prompt = PromptTemplate(
    name="Merge Notes & Quiz Generation Template",
    template="Merge the provided notes and quiz into a single document \n notes -> {notes} and quiz -> {quiz}",
    input_variables=["notes", "quiz"],
)

chain = (
    RunnableParallel(
        {
            "notes": notes_prompt | chat_openai_model | parser,
            "quiz": quiz_prompt | chat_claude_model | parser,
        }
    )
    | merged_prompt
    | chat_openai_model
    | parser
)

text = """
First, let's define the problem, just so we're all on the same page; the goal is to create code that maps a known, fixed set of strings to a predefined integer (per string), and rejects everything else. This is essentially the same as a hash table, except that since the set of strings is known ahead of time, we can do better than a normal hash table. (So no “but I heard SwissTables uses SIMD and thus cannot be beat”, please. :-) ) My use case is around a thousand strings or so, and we'll assume that a couple of minutes of build time is OK (shorter would be better, but we can probably cache somehow). If you've got millions of strings, and you don't know them compile-time (for instance because you want to use your hash table in the join phase of a database), see this survey; it's a different problem with largely different solutions.

Like Wojciech, I started splitting by length. This means that we can drop all bounds checking after this, memcmp will be optimized by the compiler to use SIMD if relevant, and so on.

But after that, he recommends using PEXT (bit extraction, from BMI2), which has two problems: First, the resulting table can get quite big if your input set isn't well-behaved. (You can do better than the greedy algorithm he suggests, but not infinitely so, and finding the optimal mask quickly is sort of annoying if you don't want to embed a SAT solver or something.) Second, I needed the code to work on Arm, where you simply don't have this instruction or anything like it available. (Also, not all x86 has it, and on older Zen, it's slow.)

So, we need some other way, short of software emulation of PEXT (which exists, but we'd like to do better), to convert a sparse set of bits into a table without any collisions. It turns out the computer chess community has needed to grapple with this for a long time (they want to convert from “I have a \ on \ and there are pieces on relevant squares \, give me an index that points to an array of squares I can move to”), and their solution is to use… well, magic. It turns out that if you do something like ((value & mask) * magic), it is very likely that the upper bits will be collision-free between your different values if you try enough different numbers for magic. We can use this too; for instance, here is code for all length-4 CSS keywords:
"""

result = chain.invoke(
    {
        "text": text,
    }
)

print(result)
