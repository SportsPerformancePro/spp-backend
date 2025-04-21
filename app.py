from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import os, tempfile, json
import openai

app = Flask(__name__)
CORS(app)

openai.api_key = os.getenv('OPENAI_API_KEY')

STATIC_DIR = 'static'

@app.route('/static/<path:filename>')
def static_files(filename):
    return send_from_directory(STATIC_DIR, filename)

@app.route('/analyze', methods=['POST'])
def analyze():
    # Save video temporarily
    video = request.files.get('video')
    prompt = request.form.get('prompt')
    profile = json.loads(request.form.get('profile', '{}'))
    mode = request.form.get('mode', 'Pro')
    tempdir = tempfile.mkdtemp()
    video_path = os.path.join(tempdir, video.filename)
    video.save(video_path)
    # TODO: Extract still frame using ffmpeg if available
    still_frame_url = None

    # Build AI prompt
    system_msg = f"You are a professional {profile.get('sport','sport')} coach. Provide feedback in {mode} mode for {profile.get('name','athlete')}."
    user_msg = f"{prompt} Profile: {profile}"
    response = openai.ChatCompletion.create(
        model='gpt-4o-mini',
        messages=[{'role':'system','content':system_msg}, {'role':'user','content':user_msg}],
    )
    analysis = response.choices[0].message.content

    return jsonify({'feedback': analysis, 'stillFrameUrl': still_frame_url})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.getenv('PORT',5000)))