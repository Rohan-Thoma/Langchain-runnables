from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

from langchain_core.runnables import RunnableSequence

prompt1 = PromptTemplate(
    template = "Write a joke about {topic}",
    input_variables=['topic']
)

prompt2= PromptTemplate(
    template = "Explain the following joke : {joke}",
    input_variables=['joke']
)

model = ChatOpenAI()

parser = StrOutputParser()

chain1 = RunnableSequence(prompt1, model , parser)

#This is a simple chain
print(chain1.invoke({"topic": "AI"})) 

print("\n=======================\n")

chain2= RunnableSequence(prompt1, model, parser, prompt2, model, parser)

print(chain2.invoke({'topic': 'AI'}))