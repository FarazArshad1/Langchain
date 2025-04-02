from langchain_huggingface import HuggingFaceEmbeddings

embedding = HuggingFaceEmbeddings(model_name='senetence-transformers/all-MiniLM-L6-v2')

text = 'Islambad is Capital of India'

vector = embedding.embed_query(text)

print(str(vector))