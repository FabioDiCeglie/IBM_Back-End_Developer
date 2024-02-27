"""
Module for sentiment analysis.
"""

import json
import requests

def sentiment_analyzer(text_to_analyse):
    """
    Analyze sentiment of the given text.

    Args:
        text_to_analyse (str): The text to analyze.

    Returns:
        dict: Containing 'label' and 'score' of the sentiment analysis.
    """
    url = 'https://sn-watson-sentiment-bert.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/SentimentPredict'
    myobj = {"raw_document": {"text": text_to_analyse}}
    header = {"grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"}
    try:
        response = requests.post(url, json=myobj, headers=header, timeout=10)
        formatted_response = json.loads(response.text)
        if response.status_code == 200:
            label = formatted_response['documentSentiment']['label']
            score = formatted_response['documentSentiment']['score']
        elif response.status_code == 500:
            label = None
            score = None
        return {'label': label, 'score': score}
    except requests.exceptions.RequestException as e:
        print("Error: ", e)
        return None
