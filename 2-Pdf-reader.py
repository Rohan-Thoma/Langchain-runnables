from langchain_classic.document_loaders import TextLoader
from langchain_classic.text_splitter import RecursiveCharacterTextSplitter
from langchain_classic.embeddings import OpenAIEmbeddings
from langchain_classic.vectorstores import FAISS
from langchain_classic.llms import OpenAI 

#laod the document
loader = TextLoader("docs.txt")
documents = loader.load()

#split the text in to smaller chunks
text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
docs = text_splitter.split_documents(documents)

# Convert text into embddings and store in FAISS
vector_store = FAISS.from_documents(docs, OpenAIEmbeddings())

#Create a retriever (fectches relevant documents)
retriever = vector_store.as_retriever()

# manually retrive relevent documents
query = "What are the key takeaways from the document?"
retrived_docs = retriever._get_relevant_documents(query)

# Combine retrieved text into a single prompt
retrieved_text = "\n".join([doc.page_content for doc in retrived_docs])

# initialize the llM
llm = OpenAI(model_name='gpt-4', temperateure = 0.7)

#Manually pass the retriever text in to LLM
prompt = f"Based on the following text, answer the question: {query}\n\n {retrieved_text}"
answer = llm.predict(prompt)

#print the answer
print('Answer: ', answer)