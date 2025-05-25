import os
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.exceptions import OutputParserException

from dotenv import load_dotenv

load_dotenv()

class chain:
    def __init__(self):
        self.llm = ChatGroq(
        temperature = 0,
        groq_api_key = os.getenv("GROQ_API_KEY"),
        model_name= "llama-3.3-70b-versatile",
        )

    def extract_jobs(self, cleaned_text):
        prompt_template = PromptTemplate.from_template(
            """
            ###SCRAPED TEXT FROM THE WEBSITE:
            {page_data}
            ###INSTRUCTION:
            The scraped text is from the career's page of a website.
            Your job is to extract the job postings and return them in JSON format containing the following keys: 'role', 'experience','skills' and 'description'.
            Only return the valid JSON.
            ###VALID JSON (NO PREAMBLE):
            
            """
        )
        chain_extract = prompt_template | self.llm
        res = chain_extract.invoke(input={'page_data' : cleaned_text})
        try:
            json_parser = JsonOutputParser()
            json_res= json_parser.parse(res.content)
            # json_res = json.loads(res.content)
        
        except Exception as e:
            raise OutputParserException("Context too big. Unable to parse the jobs.")
            # raise ValueError(f"Failed to parse JSON: {e}\nResponse was:\n{res.content}")

        return json_res if isinstance(json_res, list) else [json_res]


    def write_mail(self, job,links):
        prompt_email = PromptTemplate.from_template(
            """
            ###JOB DESCRIPTION:
            {job_description}

            ###INSTRUCTION:
            You are Raj, a business development executive at Meta. Meta is a tech giant specializing in social media platforms and technologies. They have expertise in building and managing large-scale social networks, including Facebook, Instagram, Threads, Messenger, and WhatsApp. Their expertise extends to virtual and augmented reality, AI, and data analytics. 

            Your job is to write a cold email to the client regarding the job mentioned above describing the capability of fulfilling their needs.
            Also add the most relevant ones from the following links to showcase Meta's portfolio : {link_list}
            Remember you are Raj, BDE at Meta.
            Do not provide a preamble.
            ###EMAIL(NO PREAMBLE):

            """
        )
        chain_email = prompt_email | self.llm
        res = chain_email.invoke({"job_description" : str(job), "link_list":links})
        return res.content
       

if __name__ == "__main__":
    print(os.getenv("GROQ_API_KEY"))