from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence, RunnableParallel, RunnablePassthrough

from dotenv import load_dotenv

load_dotenv()

##First lets demo runnable passthrough with a dummy text
# Just to check whether it really gives input as output or not
passthrough = RunnablePassthrough()

print("\n========================\n Dummy test run \n======================\n")
print(passthrough.invoke("this is the input"))
print("\n====================================\n")

#Now lets build the actual chain
#First get all the components
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

#Now lets build the chains

Joke_generator_chain = RunnableSequence(prompt1, model, parser)

parallel_chain = RunnableParallel(
    {
        "joke": RunnablePassthrough(),
        "explanation": RunnableSequence(prompt2, model, parser)
    }
)

final_chain = RunnableSequence(Joke_generator_chain, parallel_chain)

result = final_chain.invoke({'topic': 'AI'})

print("\n================\n")
print(result)
print("\n =======================\n")