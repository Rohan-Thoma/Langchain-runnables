#Here we are looking at traditonal way of working with langchain
from langchain_classic.llms import OpenAI
from langchain_classic.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

#Initialize the LLM
llm = OpenAI(model_name= 'gpt-4', temperature=0.7)

#Create a Prompt template
prompt = PromptTemplate(
    template='suggest a catchy blog title about {topic}',
    input_variables=['topic']
)

#Define the input
topic = input('Enter a topic for the blog : ')

#Format the prompt manually using prompt template
formatted_prompt = prompt.format(topic=topic)

# Call the LLM directly
blog_title = llm.predict(formatted_prompt)

# Print the output
print("Generated Blog Title : ", blog_title)
