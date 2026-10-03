from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/hello")
def hello():
    name = request.args.get("name")
    return jsonify({"message": f"안녕하세요 {name}님!"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)