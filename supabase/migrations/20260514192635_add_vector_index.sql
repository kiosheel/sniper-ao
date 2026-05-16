create index on chunks 
using hnsw (embedding vector_cosine_ops)
with (m = 16, ef_construction = 64);