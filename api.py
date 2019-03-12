"""
api.py
~~~~~~

This file define simple REST APi for a Machine Learning Model
"""

from os import environ as env

from joblib import load
from flask import abort, Flask, jsonify, make_response, request
from pandas import DataFrame


service_name = env['SERVICE_NAME']
version = env['API_VERSION']
model = load('data/model.joblib')
app = Flask(__name__)


@app.route(f'/{service_name}/v{version}/predict', methods=['POST'])
def predict():
    """Predict Incoming Request"""
    try:
        req = request.json
        print(req)
        features = DataFrame(req)
        prediction = model.predict(features).tolist()
        return make_response(jsonify({'prediction': prediction}))
    except ValueError:
        raise RuntimeError('Features are not in the correct format.')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)

