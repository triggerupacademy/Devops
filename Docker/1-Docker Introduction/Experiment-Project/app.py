# app.py
import requests
from flask import Flask, jsonify
import numpy as np

app = Flask(__name__)

@app.route('/')
def home():
    # Use requests to get data from a public API
    response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    bitcoin_data = response.json()
    
    # Use numpy to create a simple array
    data = np.array([1, 2, 3, 4, 5])
    
    return jsonify({
        'message': 'Hello from Dockerized Python App!',
        'bitcoin_price': bitcoin_data['bpi']['USD']['rate'],
        'array': data.tolist()
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

