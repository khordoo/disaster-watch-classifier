import json
from flask import Flask, request, abort
from src.model import TweeterClassifier

classifier = TweeterClassifier()

app = Flask(__name__)


@app.route('/classify', methods=['POST', 'GET'])
def index():
    if request.method == 'GET':
        return 'Welcome to Tweeter Disaster Classifier'

    if request.method == 'POST':
        if not request.json:
            abort(400)
        tweet = request.json
        prediction = classifier.predict(tweet['tweet'])
        response = app.response_class(
            response=json.dumps(prediction),
            status=200,
            mimetype='application/json'
        )
        return response
