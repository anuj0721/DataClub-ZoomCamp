from flask import Flask
from flask import request
from flask import jsonify
import pickle


with open('model1.bin', 'rb') as f:
    model = pickle.load(f)

with open('dv.bin', 'rb') as f:
    dv = pickle.load(f)


app = Flask('churn')


@app.route('/predict', methods=['POST'])
def predict():
    customer_data = request.get_json()

    y_pred = model.predict_proba(dv.transform(customer_data))[0][1]

    result = {
        'churn_probability': float(y_pred)
    }

    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=9696)
