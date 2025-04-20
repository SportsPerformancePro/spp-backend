
from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import openai
import json

app = Flask(__name__)
CORS(app)

openai.api_key = os.getenv("OPENAI_API_KEY")

def load_template(sport):
    try:
        with open(f"data/templates/{sport.lower()}.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return None

@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.json
    sport = data.get("sport")
    prompt = data.get("prompt", "Analyze this performance.")

    template = load_template(sport)
    if not template:
        return jsonify({"error": "Template not found."}), 404

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": f"You are an expert coach in {sport}."},
                {"role": "user", "content": prompt}
            ]
        )
        return jsonify({"reply": response['choices'][0]['message']['content']})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
