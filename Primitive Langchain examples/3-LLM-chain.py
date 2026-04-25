from langchain_classic.llms import OpenAI
from langchain_classic.chains import LLMChain
from langchain_classic.prompts import PromptTemplate
from dotenv import load_dotenv
load_dotenv()


#Laod the LLM
llm = OpenAI(model_name='gpt-4', temperature=0.7)

#create a prompt template
prompt = PromptTemplate(
    input_variables=['topic'],
    template="Suggest a catchy lbog title about {topic}"
) 

#create an LLMChain  
chain = LLMChain(llm=llm, prompt=prompt)

# Run the chain with a specific topic
topic = input("Enter a topic")
output = chain.rub(topic)

print("Generated Blog title:", output)