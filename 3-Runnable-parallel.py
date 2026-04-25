from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence, RunnableParallel

from dotenv import load_dotenv

load_dotenv()

prompt1 = PromptTemplate(
    template = "Generate a tweet aboout {topic}",
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template = "Generate a linkedin post about {topic}",
    input_variables=['topic']
)

model = ChatOpenAI()

parser = StrOutputParser()

parallel_chain = RunnableParallel({
    'tweet': RunnableSequence(prompt1, model, parser),
    'linkedin': RunnableSequence(prompt2, model, parser)
})

result = parallel_chain.invoke({"topic": 'AI'})

#This will be the dictionary the keys as 'task' names which are 'tweet' and 'linkedin'
print(result)
print("\n========================\n")
print(result['tweet'])
print("\n========================\n")
print(result['linkedin'])