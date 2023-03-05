from flask import Flask, render_template, request,url_for, jsonify

import openai
import nltk
nltk.download('vader_lexicon') 

from nltk.sentiment.vader import SentimentIntensityAnalyzer

import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

import requests

cred = credentials.Certificate("D:\\tomodachi\\ai\\led-iot-c29ca-firebase-adminsdk-r8xds-687021e5e8.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://led-iot-c29ca-default-rtdb.asia-southeast1.firebasedatabase.app/'
})

ref = db.reference('/')

app = Flask(__name__)

@app.route('/')
def home():
    image_url = url_for('static', filename='img/n.png')
    return render_template('index.html',img=image_url)

@app.route('/process', methods=['POST'])
def process():
    text=request.form['name']
        
    if(text == "led1 on") :
        final = "led1 is on"
        ref.set({'iot_1': '1'})

    elif (text == "led1 off") :
        final = "led1 is off"
        ref.set({'iot_1': '0'})

    else :
        sid = SentimentIntensityAnalyzer()

        openai.api_key = "openai.api_key"

        model_engine = "text-davinci-003"

        completion = openai.Completion.create(
            engine=model_engine,
            prompt=text,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.5,
        )

        response = completion.choices[0].text
        scores = sid.polarity_scores(response)

        positive_score = scores['pos']
        negative_score = scores['neg']
        neutral_score = scores['neu']

        if positive_score > negative_score and positive_score > neutral_score:
            image_url = "h.png"
            sentiment = 'positive'
        elif negative_score > positive_score and negative_score > neutral_score:
            image_url = "s.png"
            sentiment = 'negative'
        else:
            image_url = "n.png"
            sentiment = 'neutral'

        final = f'{response}    [{sentiment}]'

        return jsonify({'name': final, 'image_url': url_for('static', filename=f'img/{image_url}')})

    return jsonify({'name': final, 'image_url': url_for('static', filename='img/n.png')})

if __name__ == '__main__':
	app.run(debug=True)
