from flask import Flask, request, jsonify
from flask_cors import CORS
import openai, os

openai.api_key = os.getenv('OPENAI_API_KEY')

app = Flask(__name__)
CORS(app)

@app.route('/api/analyze', methods=['POST'])
def analyze():
    data = request.json
    prompt = f"Analyze this {data.get('sport')} performance. Athlete: {data.get('name')}, level: {data.get('experience')}, ranking: {data.get('ranking')}. Prompt: {data.get('question')}"
    # Placeholder analysis
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150
    )
    return jsonify({ 'feedback': response.choices[0].text.strip() })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
