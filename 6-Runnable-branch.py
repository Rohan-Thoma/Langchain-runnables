from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel, RunnableSequence, RunnableLambda, RunnablePassthrough, RunnableBranch

from dotenv import load_dotenv
load_dotenv()

prompt1= PromptTemplate(
    template="Write a detailed report on {topic}",
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template="Summarize the following text \n {text}",
    input_variables=['text']
)

model = ChatOpenAI()

parser = StrOutputParser()

report_generation_chain = RunnableSequence(prompt1, model, parser)

#In this each condition is a tuple
branch_chain = RunnableBranch(
    (lambda x:len(x.split())>500, RunnableSequence(prompt2, model, parser)),
    RunnablePassthrough()
)

final_chain = RunnableSequence( report_generation_chain, branch_chain)

result = final_chain.invoke({"topic": "America vs Iran"})

print("\n===================\n")
print(result)
print("\n=====================\n") 