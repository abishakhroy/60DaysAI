from langchain_community.document_loaders import TextLoader
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.document_loaders import WebBaseLoader
from langchain_community.document_loaders import ArxivLoader
from langchain_community.document_loaders import WikipediaLoader


#Text file loader

test = TextLoader("Notes.txt")
text_docs = test.load()

print("---- TEXT FILE CONTENT ----")
print(text_docs[0].page_content)


#pdf file loader
test2 = PyPDFLoader("Image-Prompting-Cheat-Sheet.pdf")
test2.load()

#Web content loader
test3 = WebBaseLoader(web_path="https://www.geeksforgeeks.org/web-tech/web-technology/")
test3.load()

#Reserach paper loader
test4 = ArxivLoader(query = "1706.03762")
text_docs4 = test4.load()

#print("---- FILE CONTENT ----")
#print(text_docs4[0].page_content)

#Wikipedia Loader
test5 = WikipediaLoader(query="Vijay",load_max_docs=2)
test5.load()
