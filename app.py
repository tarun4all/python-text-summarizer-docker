import os
import csv
import urllib.request
import pandas as pd
import csv

from flask import Flask, json, render_template, request, jsonify
from summaryService import summarize
from datetime import date

from senitmentService import predictEmotion
from customSentiment import predict_custom_sentiment
from shellHelper import run_sentiment_training, edit_sentiment_csv
from TwitterSentiment.classifier import predictTweet
from uploadFile import allowed_file, save_file

api = Flask(__name__)

@api.route('/', methods=['GET'])
def get_companies():
    return render_template('sentiment.html')

@app.route('/sentiment/<task>', methods = ['POST'])
def sentimentHandle(task):
    requestData = request.get_json()
    data = {}

    if task == 'train':
        run_sentiment_training()
        data = {"status" : "ok"}
    elif task == 'report':
        enterData = [requestData['emotion'], requestData['para'], date.today()]
        with open(os.path.join(os.path.dirname( __file__ ), './sentiments.csv'), 'a', newline='\n') as file:
            writer = csv.writer(file)
            writer.writerow(enterData)
        data = {"status" : "ok"}
    elif task == "find":
        if requestData['type'] == '1':
            summary = predictEmotion(requestData['para'])
            data = {"summary": "positive" if summary == 1 else "negative"}
        elif requestData['type'] == '2':
            summary = predict_custom_sentiment(requestData['para'])
            data = {"summary": summary[0]}
        elif requestData['type'] == '3':
            summary = predictTweet(requestData['para'])
            data = {"summary": "positive" if summary[0] == 1 else "negative"}

    response = app.response_class(
        response=json.dumps(data),
        status=200,
        mimetype='application/json'
    )
    return response


if __name__ == '__main__':
    api.run(debug=True, host='0.0.0.0', port=8028)