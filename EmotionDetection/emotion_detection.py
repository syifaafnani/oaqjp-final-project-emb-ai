import requests
import json
import operator

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json = myobj, headers = header)
    formatted_response = json.loads(response.text)
    
    if response.status_code == 200:
        emotion_scores = formatted_response['emotionPredictions'][0]['emotion']
        emotion_scores['dominant_emotion'] = max(emotion_scores.items(), key=operator.itemgetter(1))[0]
    elif response.status_code == 400:
        emotion_scores = {'anger': None, 'disgust': None, 'fear': None,
        'joy': None, 'sadness': None, 'dominant_emotion': None}
    
    return emotion_scores