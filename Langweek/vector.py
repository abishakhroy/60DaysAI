from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

# 1️⃣ Text data
texts = [
    "You will repeat ideas",
    "say similar things",
    "feel like you're boring"
]

# 2️⃣ Embedding model
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# 3️⃣ Create FAISS vector store
vectorstore = FAISS.from_texts(texts, embeddings)

# 4️⃣ Save locally
vectorstore.save_local("my_first_vector")

# 5️⃣ Create retriever
retriever = vectorstore.as_retriever(search_kwargs={"k": 2})

# 6️⃣ Query (IMPORTANT: use invoke)
query = "ideas"
results = retriever.invoke(query)

# 7️⃣ Print results
print("\n--- Results ---")
for i, doc in enumerate(results, 1):
    print(f"\nResult {i}:")
    print(doc.page_content)
  