# **Overview**

The Cold Email Generator is an AI-powered tool that helps job seekers craft personalized cold emails tailored to any job posting URL. It intelligently analyzes job descriptions, matches them with relevant portfolio projects stored in a vector database, and generates compelling cold emails to express interest in the role.

## 🚀 **How It Works**
1. **Input:** The user enters the URL of the job posting they’re interested in.
2. **Job Parsing:** Meta’s Llama 3.3-70B model processes the job URL to extract relevant details in structured JSON format.
3. **Portfolio Matching:** Based on the extracted job description, relevant portfolio links are retrieved from a ChromaDB vector database.   
4. **Email Generation:** The model then generates a personalized cold email, incorporating the matched portfolio links to highlight the user’s qualifications.

## 🧠 **Under the Hood**

**LLM-Powered Extraction:** Llama 3.3-70B (served via GROQ cloud) interprets and summarizes job descriptions.

**LangChain:** Used to orchestrate the LLM workflows and connect to the vector database.

**Vector Search:** Portfolio projects are stored in ChromaDB and retrieved based on semantic relevance to the job posting.

**Frontend:** A Streamlit interface provides a clean and intuitive user experience.

## ⚙️ **Tech Stack**

**LLM:** Meta's Llama 3.3-70B (via GROQ cloud)

**Framework:** LangChain

**Frontend:** Streamlit

**Database:** ChromaDB (for vector search)

**Hosting/Serving:** GROQ API (no local model setup required)

## 🛠️ **Setup Instructions**

1. Get your API key from GROQ Console and add it to the .env file as GROQ_API_KEY.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
3. Run the streamlit app:
   ```bash
   streamlit run app.py

## Example
**Input URL:** https://company.com/careers/software-engineer

↳ **Extracted Role:** Software Engineer

↳ **Skills:** Python, APIs, ML

↳ **Matching Portfolio:** Portfolio project links from vector DB

↳ **Output:** Personalized cold email generated with context

## 💡 Challenges & Solutions
| Challenge                         | Solution                                    |
| --------------------------------- | ------------------------------------------- |
| LangChain compatibility issues    | Used stable, community-supported versions   |
| Large model resource requirements | Offloaded to GROQ Cloud                     |
| System stability                  | Optimized LangChain and Streamlit workflows |


