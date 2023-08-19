import json

import requests
from flask import Flask, jsonify, request

app = Flask(__name__)

def fetch_numbers(url):
    try:
        response = requests.get(url)
        data = response.json()
        if "numbers" in data and isinstance(data["numbers"], list):
            return data["numbers"]
        else:
            return None
    except Exception as e:
        return None

@app.route('/numbers', methods=['GET'])
def get_numbers():
    urls = request.args.getlist('url')

    if not urls:
        return jsonify(error="No URLs provided"), 400

    result = []
    for url in urls:
        numbers = fetch_numbers(url)
        if numbers is not None:
            result.extend(numbers)

    return jsonify(numbers=result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8008)
