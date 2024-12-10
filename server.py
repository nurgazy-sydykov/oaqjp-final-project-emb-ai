import json
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

#Initiate the flask app :
app = Flask('Emotion Detector')

@app.route("/emotionDetector")
def detector():
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')
    # Pass the text to the sentiment_analyzer function and store the response
    response = emotion_detector(text_to_analyze)
    text = json.dumps(response)
    text = text[1:-2]
    new_text = text.replace(', "dominant_emotion": "', '. The dominant emotion is ')
    return f'For the given statement, the system response is {new_text}.'
@app.route("/")
def render_index_page():
    # Returning rendered template
    return render_template('index.html')

if __name__ == "__main__":
    # Launching an app
    app.run(host='0.0.0.0', port=5000)
