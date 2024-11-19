import os
import openai
from openai import AzureOpenAI
 
# Set up the environment variables or defaults
endpoint = os.getenv("ENDPOINT_URL", "https://GenAI-OpenAI-Andromeda.openai.azure.com/openai/deployments/gpt-4o/chat/completions?api-version=2024-02-15-preview/")
deployment = os.getenv("DEPLOYMENT_NAME", "gpt-4o")
search_endpoint = os.getenv("SEARCH_ENDPOINT", "https://teamandromeda.search.windows.net/")
search_key = os.getenv("SEARCH_KEY", "mNlQqg4hc1qrQxgYQO85xDn0kTqFY8YaPmFOnII3t8AzSeDPensR")
subscription_key = os.getenv("AZURE_OPENAI_API_KEY", "f7b124c1e14d400395afb846b2205b98")
 
# Initialize Azure OpenAI client with key-based authentication
client = AzureOpenAI(
    azure_endpoint=endpoint,
    api_key=subscription_key,
    api_version="2024-05-01-preview",
)
 
# Prepare the chat prompt
chat_prompt = [
    {
        "role": "system",
        "content": """
  You are an AI assistant that helps people find information about source data only. Refuse to answer any other questions.
  We are creating an application for Bank which is going to suggest Personal Banking services to a customer based on customer data. A customer will get a score from 1-10 for each service.
  Services are as below:
  Savings Account Current Account Fixed Deposits Term Deposits Recurring Deposits Personal Loan Home Loan Educational Loan Vehicle Loan Cheque Payments Credit Card Online and Mobile Banking Foreign Exchange Investment Services Life Insurance Health Insurance Property Insurance Wealth Management Safe Deposit Boxes
 
  now can you predict the services with the scores and make sure to include the pitch description for the customers in 2 paragraphs for all services.,
  pitch description is a way to explain the customer why they should opt for the service.
  give 4-5 paragraphs pitch when score is high for the service and 1-2 paragraphs pitch when score is low for the service.
  please provide this data in csv format,
  also make sure to add customer id in it. also can you please make sure give more accurate results based on the customer data.
  Also include a overall score (out of 10) for the customer based on the services they should opt for.
  the prompt for this is going to be customer data with the following columns:
  Customer ID Age Gender  Marital Status  Income (Annual) Occupation  Credit Score  Outstanding Loans Banking History Current Account Balance Savings Account Balance Mortgage/Property Ownership Vehicle Owned Insurance Coverage  Investment Portfolio  Digital Banking Usage Risk Appetite Location  Spending Habits.
  in the output you have to give these columns:
  Customer ID, Service Name, Service Score, Pitch Description.
  also add the overall score for the customer as the final row in the data.
            Make sure to create the data like real-world scenario. Just give the dataset no more summary about data. format should be separated by ',' as i want to copy in CSV file. Whereever we have multiple values for a column, separate them by '--'.
"""
    },
    {
        "role": "user",
        "content": """
        Customer ID, Age, Gender, Marital Status, Income (Annual), Occupation, Credit Score, Outstanding Loans, Banking History, Current Account Balance, Savings Account Balance, Mortgage/Property Ownership, Vehicle Owned, Insurance Coverage, Investment Portfolio, Digital Banking Usage, Risk Appetite, Location, Spending Habits
        1008, 36, F, Married, 95000, Accountant, 770, 15000, Savings--Home Loan, 30000, 40000, Yes, No, Health--Life--Property, Mutual Funds, High, Aggressive, Boston, High
        """
    }
]
 
# Include speech result if speech is enabled
speech_result = chat_prompt
 
# Generate the completion (corrected call without past_messages)
completion = client.chat.completions.create(
    model=deployment,
    messages=speech_result,  # Use 'messages' instead of 'past_messages'
    max_tokens=4000,
    temperature=0.7,
    top_p=0.95,
    frequency_penalty=0,
    presence_penalty=0,
    stop=None,
    stream=False
)
 
# Include extra body for Azure search integration
extra_body = {
    "data_sources": [{
        "type": "azure_search",
        "parameters": {
            "filter": None,
            "endpoint": f"{search_endpoint}",
            #"index_name": "sweet-shark-d4n44bhlhz",
            "index_name": "azureblob-index12-h78g1w2b5z",
            "semantic_configuration": "azureml-default",
            "authentication": {
                "type": "api_key",
                "key": f"{search_key}"
            },
            "embedding_dependency": {
                "type": "endpoint",
                "endpoint": "https://GenAI-OpenAI-Andromeda.openai.azure.com/openai/deployments/text-embedding-ada-002/embeddings?api-version=2023-07-01-preview",
                "authentication": {
                    "type": "api_key",
                    "key": "f7b124c1e14d400395afb846b2205b98"
                }
            },
            "query_type": "vector_simple_hybrid",
            "in_scope": True,
            "role_information": "You are an AI assistant that helps people find information about source data only.",
            "strictness": 3,
            "top_n_documents": 5
        }
    }]
}
 
# Print the completion response as JSON
print(completion.to_json())
 