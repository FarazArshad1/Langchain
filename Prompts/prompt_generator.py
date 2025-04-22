from langchain_core.prompts.prompt import PromptTemplate

template = PromptTemplate(
    template = """Please summarize the research paper titled "{paper_input}" with the following specifications:
    Explanation Style: {style_input}
    Length of Explanation: {length_input}
    
    1. Mathematical Details:
        - Include any relevant mathematical equations or concepts if present in paper.
        - Explain the mathematical concepts using simple, intuctive code snippets where
        applicable.
    2. Analogies:
        - Provide analogies to help understand the concepts.
    
    If Cerain concepts are not present in the paper, respond with: "Insufficient Information available" instead pf guessing.
    Ensure the summary is clear, concise, and easy to understand for someone with a basic understanding of the topic and aligned with the provided style and length.
    """,
    
    input_variables = ["paper_input", "style_input", "length_input"],
    validate_template=True,
)

template.save('template.json')