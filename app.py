from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import openai

app = Flask(__name__)
CORS(app)

openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/")
def home():
    return "Backend is running."

@app.route("/analyze", methods=["POST"])
def analyze():
    try:
        data = request.json
        sport = data.get("sport")
        prompt = data.get("prompt")
        if not sport or not prompt:
            return jsonify({"error": "Missing sport or prompt"}), 400

        messages = [
            {"role": "system", "content": f"You are an AI coach specialized in {sport}."},
            {"role": "user", "content": prompt}
        ]

        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=messages
        )

        reply = response.choices[0].message["content"]
        return jsonify({"response": reply})

    except Exception as e:
        return jsonify({"error": str(e)}), 500
