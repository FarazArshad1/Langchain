from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader, TextLoader

loader = DirectoryLoader(
    path="Document Loader/Documents",
    glob="*.pdf",
    loader_cls=PyPDFLoader,
)

docs = loader.load()

print(len(docs))

print(docs[0].page_content)
print(docs[0].metadata)
