import requests

url = "http://127.0.0.1:5000/predict"  

data = {
    "Dummy Policy No": 123456,  
    "ASSURED_AGE": 35,
    "NOMINEE_RELATION": 1,  # Spouse ko manually encode kiya (Example: Spouse = 1, Child = 2, Parent = 3)
    "OCCUPATION": 2,  # Salaried ka encoded value
    "POLICY SUMASSURED": 500000,
    "Premium": 12000,
    "PREMIUMPAYMENTMODE": 0,  # Annual ka encoded value
    "Annual Income": 800000,
    "HOLDERMARITALSTATUS": 1,  # Married = 1
    "INDIV_REQUIREMENTFLAG": 1,  # Y = 1, N = 0
    "Policy Term": 20,
    "Policy Payment Term": 15,
    "CORRESPONDENCECITY": 3,  # Example encoding
    "CORRESPONDENCESTATE": 2,
    "CORRESPONDENCEPOSTCODE": 110001,
    "CHANNEL": 1,  # Online ka encoded value
    "Bank code": 5,
    "Date of Death": 20240615,  # Date ko integer format me convert karo
    "INTIMATIONDATE": 20240620,
    "STATUS": 1,
    "SUB_STATUS": 2
}

response = requests.post(url, json=data)

print("Status Code:", response.status_code)
print("Response:", response.json())