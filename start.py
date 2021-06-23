from flask import Flask, jsonify
from flask_cors import CORS
from MooBaa import MooBaa

app = Flask(__name__)
CORS(app)

state = MooBaa()

@app.route("/moo", methods=["GET"])
def playMoo():
    res = state.moo()
    return jsonify(result=res)

@app.route("/baa", methods=["GET"])
def playBaa():
    res = state.baa()
    return jsonify(result=res)

@app.route("/baamoo", methods=["GET"])
def getBaaMoo():
    res = state.getBaaMoo()
    return jsonify(result=res)

# run the flask app.
if __name__ == "__main__":
    app.run(host="0.0.0.0",port=16000,debug=True)