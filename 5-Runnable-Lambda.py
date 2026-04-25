from langchain_core.runnables import RunnableLambda

#function to count the number of words
def word_counter(text):
    return len(list(text.split()))

#now we will convert this in to a runnable 
runnable_word_counter = RunnableLambda(word_counter)


print("\n================\n Dummy run \n=================\n")
#Lets see if its returns the number of words
print(runnable_word_counter.invoke("there are five words here"))
print("\n=======================\n")


#Now, lets build the application 

from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel, RunnableSequence, RunnableLambda, RunnablePassthrough

from dotenv import load_dotenv
load_dotenv()

model = ChatOpenAI()

prompt = PromptTemplate(
    template = "Write a joke about {topic}",
    input_variables=['topic']
)

parser = StrOutputParser()

joke_generator_chain = RunnableSequence(prompt, model, parser)

parallel_chain = RunnableParallel({
    'joke': RunnablePassthrough(),
    'number of words': runnable_word_counter
})

final_chain = RunnableSequence(joke_generator_chain, parallel_chain)

result = final_chain.invoke({"topic": "AI"})

print("\n=========Final Output===============\n")
print(result)
print("\n====================================\n")