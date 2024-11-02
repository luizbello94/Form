
import logging
import os
from twilio.rest import Client
from decouple import config
from langchain_openai import ChatOpenAI  
from langchain_openai import OpenAIEmbeddings  
from langchain_community.document_loaders import UnstructuredWordDocumentLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.prompts import PromptTemplate
from langchain_community.vectorstores import FAISS
from langchain.prompts import SystemMessagePromptTemplate, HumanMessagePromptTemplate, ChatPromptTemplate
from langchain.chains import RetrievalQA

# Configuración de Twilio
account_sid = config("TWILIO_ACCOUNT_SID")
auth_token = config("TWILIO_AUTH_TOKEN")
client = Client(account_sid, auth_token)
twilio_number = config("TWILIO_NUMBER")


# Configuración del logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


# Envío de mensajes vía Twilio Messaging API
def send_message(to_number, body_text):
    try:
        message = client.messages.create(
            from_=f"whatsapp:{twilio_number}",
            body=body_text,
            to=f"whatsapp:{to_number}",
        )
        logger.info(f"Mensaje enviado a {to_number}: {message.body}")
    except Exception as e:
        logger.error(f"Error enviando mensaje a {to_number}: {e}")



# def save_response_log(phone_number, description, response, start_date):
#     data = {
#         "Phone_number": phone_number,
#         "Description": description,
#         "Response": response,
#         "Start_Date": start_date,
#     }
#     logger.info(f"Datos enviados a Airtable tabla de response log {data}")
#     try:
#         record = table_log.create(data)
#         logger.info(f"Registro creado en tabla response log , datos: {record}")
#     except Exception as e:
#         logger.info(f"Error al crear el registro en airtable {e}")
#         raise




# Setup logger
logger = logging.getLogger(__name__)

def setup_langchain():
    # Step 1: Configure embeddings for the QA system
    embeddings = OpenAIEmbeddings(
        openai_api_key=config("OPENAI_API_KEY")
    )  
    
    # Step 2: Define the prompt template with specific instructions
    prompt_template = """
    **Role:**
    You are an advanced programming assistant, highly knowledgeable in software development and data science. You are aware of the user's background in full-stack development, including experience with Python, JavaScript, C#, Django, React, and Node.js, as well as data science and machine learning. Your goal is to provide precise, relevant, and efficient guidance that aligns with the user's expertise level.

    **Response Format:**
    - Directly address the user's question or problem with clear, step-by-step guidance.
    - Offer code examples when necessary, focusing on clarity and best practices.
    - If there are multiple solutions, briefly mention alternative approaches and their advantages.

    **Scope:**
    - Focus on programming topics, including full-stack development, data science, machine learning, API integration, and database management.
    - Provide detailed explanations or references if requested, especially for complex or advanced topics.

    **Parameters:**
    - Use only the information provided in the context.
    - If the requested information is not available, kindly indicate that you do not have that information.
    - Limit responses to a maximum of 800 characters when brevity is requested; otherwise, provide comprehensive answers.

    **Purpose:**
    Assist the user in solving complex programming challenges, refining code, understanding algorithms, or implementing new technologies effectively.

    **Objective:**
    Empower the user to reach solutions efficiently while expanding their knowledge in programming and development.

    ---

    **Context:**
    {context}

    **Question:**
    {question}

    **Response:**
    """

    # Step 3: Define the prompt template for LangChain
    PROMPT = PromptTemplate(
        template=prompt_template, input_variables=["context", "question"]
    )

    # Step 4: Configure the language model
    llm = ChatOpenAI(
        model_name="gpt-4o-mini",  # Switch to "gpt-3.5-turbo" if GPT-4 is unavailable
        temperature=0,
        max_tokens=600,
        openai_api_key=config("OPENAI_API_KEY"),
    )

    # Step 5: Create the question-answering chain with retrieval
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        chain_type_kwargs={"prompt": PROMPT},  
    )
    return qa_chain

# Initialize the QA chain
qa_chain = setup_langchain()

# Function to handle user queries
def responder_consulta(consulta):
    try:
        # Generate a response for the given query
        resultado = qa_chain({"query": consulta})
        respuesta = resultado["result"]
        return respuesta
    except Exception as e:
        logger.error(f"Error al generar respuesta con LangChain: {e}")
        return "Lo siento, ocurrió un error al procesar su solicitud."



# Función para responder a las consultas informativas
def responder_consulta(consulta):
    try:
        resultado = qa_chain({"query": consulta})
        respuesta = resultado["result"]
        return respuesta
    except Exception as e:
        logger.error(f"Error al generar respuesta con LangChain: {e}")
        return "Lo siento, ocurrió un error al procesar su solicitud."

