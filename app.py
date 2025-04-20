from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return 'Backend is running.'

@app.route('/api/ask', methods=['POST'])
def ask():
    data = request.json
    sport = data.get('sport')
    prompt = data.get('prompt')
    # Simulate a response
    return jsonify({
        "response": f"AI Coach response for sport: {sport}, with prompt: {prompt}"
    })

if __name__ == '__main__':
    app.run(debug=True)
