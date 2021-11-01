import requests

url = "http://localhost:9696/predict"

customer = {"age":"49", 
             "job":"blue-collar", 
             "marital":"married", 
             "education":"basic.9y", 
             "default":"unknown", 
             "housing":"no", 
             "load":"no", 
             "contact":"cellural", 
             "month":"nov", 
             "day_of_week":"wed", 
             "duration":227, 
             "campaign":4, 
             "poutcome":"nonexistent"}

response = requests.post(url, json=customer).json()
print(response)

if response["subscribe"] == True:
    print("The customer will subscirbe")
else:
    print("The customer will not subscirbe")