import pickle
import xgboost as xgb
from flask import Flask
from flask import request
from flask import jsonify
import streamlit as st

model_file = 'model.pkl'

with open(model_file, 'rb') as f_in:
    dv, model = pickle.load(f_in)

app = Flask('subscribe')

@app.route('/predict', methods=['POST'])
def predict():
    customer = request.get_json()
    print(customer)
    features = dv.get_feature_names()
    print(features)
    X = dv.transform([customer])
    print(X)
    dX = xgb.DMatrix(X, feature_names = features)
    y_pred = model.predict(dX)
    subscribe = y_pred >= 0.5

    result = {
        'subscribe_probability': float(y_pred),
        'subscribe': bool(subscribe)
    }

    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=9696)