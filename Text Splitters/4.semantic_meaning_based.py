"""
Semantic Chunker is a lightweight Python package for semantically-aware chunking and clustering of text.
It’s designed to support retrieval-augmented generation (RAG), LLM pipelines,
and knowledge processing workflows by intelligently grouping related ideas.

Traditional chunking methods for LLM pipelines often rely on fixed-size windows or naive text boundaries,
which can fragment meaning, split up related ideas, or fail to capture contextual coherence.
This leads to inefficient retrieval, diluted embeddings, and suboptimal responses in RAG systems.
Semantic Chunker addresses this by analyzing the
meaning of each chunk — using sentence embeddings and clustering — to merge semantically similar chunks into more coherent units.
The result is smarter preprocessing: fewer, denser, and more relevant chunks t
that enhance both the performance and interpretability of your downstream models.


Learn more here: https://github.com/rango-ramesh/advanced-chunker

"""

from semantic_chunker.core import SemanticChunker

chunks = [
    {"text": "Artificial intelligence is a growing field."},
    {"text": "Machine learning is a subset of AI."},
    {"text": "Photosynthesis occurs in plants."},
    {"text": "Deep learning uses neural networks."},
    {"text": "Plants convert sunlight into energy."},
]

chunker = SemanticChunker(max_tokens=512)
merged_chunks = chunker.chunk(chunks)

for i, merged in enumerate(merged_chunks):
    print(f"Chunk {i}:")
    print(merged["text"])
    print()
