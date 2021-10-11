import requests

url = 'http://localhost:9696/predict'
customer_data = {
    'contract': 'two_year',
    'tenure': 12,
    'monthlycharges': 10
}
response = requests.post(url, json=customer_data).json()

print(response)
