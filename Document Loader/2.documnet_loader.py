from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader("Document Loader/Documents/Terms of Use.pdf")

docs = loader.load()

print(len(docs))
print(docs[0].page_content)
print(docs[0].metadata)
