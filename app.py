from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from analysis import analyze_video

app = Flask(__name__)
CORS(app)

@app.route('/api/analyze', methods=['POST'])
def analyze():
    vid = request.files.get('video')
    profile = request.form.get('profile')
    tone = request.form.get('tone')
    feedback = analyze_video(vid, profile, tone)
    return jsonify({ 'feedback': feedback })

if __name__ == '__main__':
    app.run(debug=True)
