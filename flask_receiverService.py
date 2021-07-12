from flask import Flask, jsonify, request
app = Flask(__name__)

link = [
  
]

@app.route("/api/v1/info")
def get_link():
  return "getting info of entered url"
