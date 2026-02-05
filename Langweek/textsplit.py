from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

# 1️⃣ Load PDF (returns list of Document objects)
loader = PyPDFLoader("Image-Prompting-Cheat-Sheet.pdf")
pdf_docs = loader.load()

print(f"Total PDF pages: {len(pdf_docs)}")

# 2️⃣ Create text splitter
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=800,      # characters per chunk
    chunk_overlap=120    # overlap between chunks
)

# 3️⃣ Split the documents
chunks = text_splitter.split_documents(pdf_docs)

print(f"Total chunks created: {len(chunks)}")

# 4️⃣ Preview first 3 chunks
for i in range(3):
    print(f"\n--- CHUNK {i+1} ---")
    print(chunks[i].page_content[:400])
    print("Metadata:", chunks[i].metadata)