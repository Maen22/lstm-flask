from flask import Flask, request, jsonify
from model import predict_tweet
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.post("/api/predict")
def predict():
    tweet = request.json["tweet"]
    result = predict_tweet(tweet)
    if result == 1:
        result = "racist"
    else:
        result = "not racist"

    return jsonify({"result": result})
