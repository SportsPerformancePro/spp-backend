
from flask import Flask, request, jsonify
from flask_cors import CORS
import openai
import os

app = Flask(__name__)
CORS(app)

openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.json
    sport = data.get("sport", "")
    prompt = data.get("prompt", "")
    
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": f"You are an expert {sport} coach analyzing video performance."},
                {"role": "user", "content": prompt}
            ]
        )
        result = response.choices[0].message["content"]
        return jsonify({"analysis": result})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
