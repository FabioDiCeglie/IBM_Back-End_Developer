"""
Module for emotion detector.
"""

import json
import requests

def emotion_detector(text_to_analyse):
    """
    Analyze emotion of the given text.

    Args:
        text_to_analyse (str): The text to analyze.

    Returns:
        dict: Containing 'label' and 'score' of the sentiment analysis.
    """
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = {"raw_document": {"text": text_to_analyse}}
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    try:
        response = requests.post(url, json=myobj, headers=header, timeout=10)
        formatted_response = json.loads(response.text)
        if response.status_code == 200:
            emotions = formatted_response['emotionPredictions'][0]['emotion']
            dominant_emotion = max(emotions, key=emotions.get)
            emotions['dominant_emotion'] = dominant_emotion
            return emotions
        elif response.status_code == 400:
            return { "anger": None, "disgust": None, 
                    "fear": None, 
                    "joy": None, 
                    "sadness": None,
                    'dominant_emotion': None} 
        return {'dominant_emotion': None}
    except requests.exceptions.RequestException as e:
        print("Error: ", e)
        return None
    