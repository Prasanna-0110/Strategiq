import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
import os
import requests
import json
# Configuration
API_KEY = "f7b124c1e14d400395afb846b2205b98"
BASE = "https://GenAI-OpenAI-Andromeda.openai.azure.com/"
headers = {
    "Content-Type": "application/json",
    "api-key": API_KEY,
}

# Define the file where items will be stored
ITEM_FILE = 'items_data.json'

def read_items_from_json():
    try:
        with open(ITEM_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def write_items_to_json(items):
    with open(ITEM_FILE, 'w') as file:
        json.dump(items, file, indent=4)

# GET endpoint: List all items
def item_list(request):
    items = read_items_from_json()
    return JsonResponse(items, safe=False)

def getData(customers):
    all_customers_data = []
    for i in range(0,len(customers)):
        payload = {
        "messages": [
        {
            "role": "system",
            "content": [
            {
                "type": "text",
                "text": """
                We are creating an application for Bank which is going to suggest Personal Banking services to a customer based on customer data. A customer will get a score from 1-10 for each service. 
    Services are as below: 
    Savings Account Current Account Fixed Deposits Term Deposits Recurring Deposits Personal Loan Home Loan Educational Loan Vehicle Loan Cheque Payments Credit Card Online and Mobile Banking Foreign Exchange Investment Services Life Insurance Health Insurance Property Insurance Wealth Management Safe Deposit Boxes

    now can you predict the services with the scores and make sure to include the pitch description for the customers in 2 paragraphs for all services.,
    pitch description is a way to explain the customer why they should opt for the service.
    give 4-5 paragraphs pitch when score is high for the service and 1-2 paragraphs pitch when score is low for the service. 
    also can you please make sure give more accurate results based on the customer data.
    Also include a overall score (out of 10) for the customer based on the services they should opt for.
    the prompt for this is going to be customer data with the following columns: 
    Customer ID	Age	Gender	Marital Status	Income (Annual)	Occupation	Credit Score	Outstanding Loans	Banking History	Current Account Balance	Savings Account Balance	Mortgage/Property Ownership	Vehicle Owned	Insurance Coverage	Investment Portfolio	Digital Banking Usage	Risk Appetite	Location	Spending Habits.
    in the output you have to give these columns:
    Customer ID, Service Name, Service Score, Pitch Description.
    also add the overall score for the customer as the final row in the data.
                Make sure to create the data like real-world scenario. Just give the dataset no more summary about data. 
                give response in json format, 
            response format: \{
"customers": [
{
"customerId": "string",
"age":"string",
"gender": "string",
"maritalStatus": "string",
"income": "string",
"occupation": "string",
"creditScore": "string",
"outStandingLoans": "string",
"bankingHistory": "string",
"currentAccountBalance": "string",
"savingsAccountBalance": "string",
"propertyOwnership": "string",
"vehicleOwned": "string",
"insuranceCoverage": "string",
"investmentPortfolio": "string",
"digitalBankingUsage": "string",
"riskAppetite": "string",
"location": "string",
"spendingHabits": "string",
"cscore": "string",
"services": [
				{
					"serviceName": "string",
					"sscore": "string",
					"pitchDesciption":"string"
				}
            ]
    }
]

                \}"""
            }
            ]
        },
                {
            "role": "user",
            "content": [
            {
                "type": "text",
                "text": f"{customers[i]}"
            }
            ]
        }
        ],
        "temperature": 0.7,
        "top_p": 0.95,
        "max_tokens": 4000
    }
        data = fetchDataFromModel(payload).replace('\n', '')
        jsonIndex = data.index('{')
        jsonEndIndex = find_last_occurrence(data, '}')
        data = data[jsonIndex:jsonEndIndex+1]
        data = json.loads(data)
        all_customers_data.append(data)
        print(i, " customers are completed")

    return all_customers_data

def find_last_occurrence(s, sub):
    return s.rfind(sub)

def fetchDataFromModel(payload):
  
  ENDPOINT = "https://genai-openai-andromeda.openai.azure.com/openai/deployments/gpt-4o/chat/completions?api-version=2024-02-15-preview"

  # Send request
  try:
      response = requests.post(ENDPOINT, headers=headers, json=payload)
      response.raise_for_status()  # Will raise an HTTPError if the HTTP request returned an unsuccessful status code
  except requests.RequestException as e:
      raise SystemExit(f"Failed to make the request. Error: {e}")

  # Handle the response as needed (e.g., print or process)
  print(response.status_code)
  return response.json()['choices'][0]['message']['content']

# POST endpoint: Create a new item
@csrf_exempt
def create_item(request):
    if request.method == "POST":
        data = json.loads(request.body)
        response = getData(data['customers'])
        customers = []
        for customer in response:
            customers.append(customer['customers'][0])
        return JsonResponse({"customers": customers}, status=201)

    return JsonResponse({'error': 'Invalid request method'}, status=405)
