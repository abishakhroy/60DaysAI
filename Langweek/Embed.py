from langchain_openai import OpenAIEmbeddings

openai_embed = OpenAIEmbeddings(openai_api_key="Key here")

textembed = "Hey Abi, You are a champ"
embeded = openai_embed.embed_query(textembed)

print(embeded[:5])
