from random import choice


# Fake implementation of Langchain LLM class which takes prompt and gives output back
class FakeLLM:

    def __init__(self):
        print("LLM Created")

    def predict(self, prompt):
        response_list = [
            "Lahore is capital of Pakistan",
            "PSL is cricket league",
            "AI stands for Artificial Intelligence",
        ]

        return {"response": choice(response_list)}


class FakePromptTemplate:

    def __init__(self, name, template, input_variables):
        self.name = name
        self.template = template
        self.input_variables = input_variables

    def format(self, **kwargs):
        return self.template.format(**kwargs)


class FakeLLMChain:

    def __init__(self, llm, prompt):
        self.llm = llm
        self.prompt = prompt

    def run(self, input_dict):
        final_prompt = self.prompt.format(**input_dict)
        result = self.llm.predict((final_prompt))
        return result["response"]


if __name__ == "__main__":
    
    llm = FakeLLM()
    
    template = FakePromptTemplate(
        name="Fake PromptTemplate class",
        template="Write a {length} poem about {topic}",
        input_variables=["length","topic"],
    )

    llm_chain = FakeLLMChain(llm, template)
    
    result = llm_chain.run({
        "length" : "short",
        "topic" : "Pakistan"
    })

    print(result)
