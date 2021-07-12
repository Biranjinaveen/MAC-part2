from flask import Flask, jsonify, request
app = Flask(__name__)

link = [
  
]

@app.route("/api/v1/ping", methods=['POST'])
def get_link():
  link.append(request.get_json())
  return jsonify(link)

@app.route("/health")
def get_link():
  return "Checking Health"
