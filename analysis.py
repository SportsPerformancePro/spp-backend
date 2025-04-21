import openai, os, tempfile

openai.api_key = os.getenv('OPENAI_API_KEY')

def analyze_video(video_file, profile_json, tone):
    tmp = tempfile.NamedTemporaryFile(delete=False, suffix=".mp4")
    video_file.save(tmp.name)
    sys = f"""You are XLevel Coach.
Profile: {profile_json}
Tone: {tone}
Analyze the video at {tmp.name} and provide improvement tips."""
    resp = openai.ChatCompletion.create(
      model="gpt-4o-mini",
      messages=[{"role":"system","content":sys}]
    )
    return resp.choices[0].message.content
