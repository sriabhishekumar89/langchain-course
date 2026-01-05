from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate   
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama


load_dotenv()

def main():
    print("Hello from langchain-course!")
    information="""abhishek srivastava, based in Bengaluru, KA, IN, is currently a Senior Project Manager at ZF LIFETEC. abhishek srivastava brings experience from previous roles at ZF Group. abhishek srivastava holds a 2019 - 2020 PG in data science @ International Institute of Information Technology Bangalore. With a robust skill set that includes AutoCAD, CATIA, PTC Creo, Mechanical Engineering, SolidWorks and more. abhishek srivastava has 3 emails on RocketReach."""
    summary_template = """Summarize the following information{information} about a person in a concise manner:
    1. A Short Summary
    2. Two interesting facts about him 
    """
    summary_prompt_template= PromptTemplate(input_variables=["information"],template=summary_template
    )
    llm = ChatOpenAI(temperature=0,model="gpt-5.2")
    #llm=ChatOllama(temperature=0,model="gemma3:270m")
    chain=summary_prompt_template | llm
    response = chain.invoke(input={"information": information})
    print(response.content)


if __name__ == "__main__":
    main()
