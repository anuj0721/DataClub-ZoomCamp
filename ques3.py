import pickle

with open('model1.bin', 'rb') as f:
    model = pickle.load(f)

with open('dv.bin', 'rb') as f:
    dv = pickle.load(f)

customer_data = {
    'contract': 'two_year',
    'tenure': 12,
    'monthlycharges': 19.7
}

print(model.predict_proba(dv.transform(customer_data))[0][1])
