from flask import Flask, jsonify

app = Flask(__name__)

logs = []

@app.route("/logs", methods=["GET"])
def get_logs():
    return jsonify(logs)

@app.route("/health", methods=["GET"])
def health():
    return {"status": "ok"}

if __name__ == "__main__":
    app.run(port=5000)
