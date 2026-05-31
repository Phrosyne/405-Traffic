from flask import Flask, jsonify, request

app = Flask(__name__)
@app.route("/")
def hello():
    return "<p>Hello World!</p>"
@app.route("/timestamps", methods=['GET'])
def time():
    return "timestamps"