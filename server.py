'''Emotion Detector Module'''
from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emo_detector():
    '''Analyze emotion from text'''
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)

    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    return f"For the given statement, the system response is 'anger': {response['anger']}, \
    'disgust': {response['disgust']}, 'fear': {response['fear']}, 'joy': {response['joy']} \
    and 'sadness': {response['sadness']}. The dominant emotion is {response['dominant_emotion']}."

@app.route("/")
def render_index_page():
    '''Index page'''
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host='localhost', port=5000)
