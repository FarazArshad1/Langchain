from langchain_text_splitters import RecursiveCharacterTextSplitter

with open('Document Loader/Documents/cricket.txt') as f:
    document = f.read()


text_splitter = RecursiveCharacterTextSplitter(chunk_size=100, chunk_overlap = 0)
texts = text_splitter.split_text(document)

print(texts)