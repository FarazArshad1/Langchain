"""
Read more about text splitter here
https://docs.langchain.com/oss/python/integrations/splitters/index
"""

from langchain_text_splitters import CharacterTextSplitter

with open('Document Loader/Documents/cricket.txt') as f:
    document = f.read()


text_splitter = CharacterTextSplitter(chunk_size=100, chunk_overlap = 0)
texts = text_splitter.split_text(document)

print(texts)
