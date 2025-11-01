from langchain_community.retrievers import WikipediaRetriever

# Initialize the retriever (optional : set the language and top_k)

retriver = WikipediaRetriever(
    top_k_results=2,
    lang="en",
)

# Define query
query = "the geopolitical history of india and pakistan from the perspective of a chinese"


# Get relevant wikipedia documents
docs = retriver.invoke(query)

#Print retrieved content
for i, docs in enumerate(docs):
    print(f"\n------ Result{i+1}------")
    print(f"Content:\n{docs.page_content}.....") #truncate display

