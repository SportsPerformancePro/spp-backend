from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return "SPP Backend Running"

@app.route("/upload", methods=["POST"])
def upload():
    if 'file' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400
    file = request.files['file']
    ext = file.filename.split('.')[-1].lower()
    if ext not in ["mp4", "mov", "avi"]:
        return jsonify({"status": "fail", "reason": "Invalid file format"}), 400
    return jsonify({"status": "success", "filename": file.filename})

@app.route("/get-template/<sport>", methods=["GET"])
def get_template(sport):
    path = f"data/templates/{sport}.json"
    if not os.path.exists(path):
        return jsonify({"error": "Template not found"}), 404
    with open(path, "r") as f:
        return f.read()

if __name__ == "__main__":
    app.run(debug=True)
