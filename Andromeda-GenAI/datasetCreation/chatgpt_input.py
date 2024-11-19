import os
import requests
import base64
import json
import openai
# Configuration
API_KEY = "f7b124c1e14d400395afb846b2205b98"
BASE = "https://GenAI-OpenAI-Andromeda.openai.azure.com/"
openai.api_key = API_KEY
openai.api_base = BASE
file_path= "C:\\Users\\JMalani\\Documents\\Andromeda\\dataset\\Financial_Statements\\Financial Statements.csv"

headers = {
    "Content-Type": "application/json",
    "api-key": API_KEY,
}

def getFileContent(file_path):
    with open(file_path, "rb") as f:
        return f.read()

# Payload for the request
payload = {
  "messages": [
    {
      "role": "system",
      "content": [
        {
          "type": "text",
          "text": "You are an AI assistant that helps to create the dataset for customer. Make sure to create the data in the real-world scenario. Just give the dataset no more summary about data. format should be separated by ',' as i want to copy in CSV file. Whereever we have multiple values for a column, separate them by '--'."
        }
      ]
    },
            {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": f"Below I want you to create a new dataset for personal banking customers. based on this dataset we are gonna provide recommanded services to the customer that bank provides try to include varitation of data as much as possible, also do generate 50 customers data. iIn the dataset I want you to include the following columns: Customer ID	,Age	,Gender	,Marital Status	,Income (Annual) ,Occupation	,Credit Score	,Outstanding Loans	,Banking History	,Current Account Balance	,Savings Account Balance	,Mortgage/Property Ownership	,Vehicle Owned	,Insurance Coverage	,Investment ,Portfolio	,Digital Banking Usage	,Risk Appetite	,Location, Spending Habits. example of the dataset is as below: Customer ID	Age	Gender	Marital Status	Income (Annual)	Occupation	Credit Score	Outstanding Loans	Banking History	Current Account Balance	Savings Account Balance	Mortgage/Property Ownership	Vehicle Owned	Insurance Coverage	Investment Portfolio	Digital Banking Usage	Risk Appetite	Location	Spending Habits \n\n1001	32	M	Married	80000	Engineer	750	10000	Savings--Home Loan	5000	20000	Yes	Yes	Health--Life	Mutual Funds	High	Balanced	New York	Moderate\n\n1002	45	F	Single	120000	Business Owner	650	50000	Savings--Credit Card	10000	5000	No	Yes	Health--Life--Auto	Stocks	Medium	Aggressive	Chicago	High. Start customer ID with 1051"
        }
      ]
    }
  ],
  "temperature": 0.7,
  "top_p": 0.95,
  "max_tokens": 3000
}

ENDPOINT = "https://genai-openai-andromeda.openai.azure.com/openai/deployments/gpt-4o/chat/completions?api-version=2024-02-15-preview"

# Send request
try:
    response = requests.post(ENDPOINT, headers=headers, json=payload)
    response.raise_for_status()  # Will raise an HTTPError if the HTTP request returned an unsuccessful status code
except requests.RequestException as e:
    raise SystemExit(f"Failed to make the request. Error: {e}")

# Handle the response as needed (e.g., print or process)
print(response.status_code)

# response = openai.Completion.create(
#     model="gpt-4o",
#     prompt=f"can you please analyze the data in the file? filecontent: {getFileContent(file_path)}",
#     max_tokens=200
#     )

def writeResponseInJSONFile(response):
    with open('response.csv', 'w') as f:
        json.dump(response.json()['choices'][0]['message']['content'], f, indent=4)



writeResponseInJSONFile(response)


# def createFileWithOpenAI(file_path):
#     with open(file_path, "rb") as f:
#         file_content = base64.b64encode(f.read()).decode("utf-8")
    
#     print(file_content)
#     response = openai.File.create(
#         purpose="answers",
#         file=file_content
#     )
#     return response





# file_response = createFileWithOpenAI(file_path)
# print(file_response)