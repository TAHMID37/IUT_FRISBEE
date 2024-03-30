# utils.py
from langchain_openai import ChatOpenAI
from langchain_core.documents import Document
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains.combine_documents import create_stuff_documents_chain
from dotenv import dotenv_values

config = dotenv_values(".env")
openai_api_key=config['OPENAI_API_KEY'] 

def generate_meeting_minutes(context_text,qa_system_prompt):    
    
    prompt = ChatPromptTemplate.from_messages(
            [("system", qa_system_prompt)]
        )

    llm = ChatOpenAI(
            model_name="gpt-3.5-turbo-0125",
            streaming=True,
            temperature=0.2, 
            api_key=openai_api_key
        )

    chain = create_stuff_documents_chain(llm, prompt)

 
    docs = [Document(page_content=context_text)]
    
    ans=chain.invoke({"context": docs})
    
    return ans