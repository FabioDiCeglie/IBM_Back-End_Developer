''' Executing this function initiates the application of sentiment
    analysis to be executed over the Flask channel and deployed on
    localhost:5000.
'''
from flask import Flask, render_template, request, jsonify
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_detector():
    """
    Analyzes the emotion of the provided text.
    Parameters:
        text_to_analyze (str): The text to be analyzed for sentiment.
    Returns:
        str: A message indicating the sentiment of the provided text and its score.
             Returns an error message if the input is invalid.
    """
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    if response['dominant_emotion'] is None:
        return "Invalid text ! Please try again."
    response_text = f"For the given statement, the system response is {jsonify(response)}. "
    response_text += f"The dominant emotion is {response['dominant_emotion']}."
    return response_text

@app.route("/")
def render_index_page():
    """
    Renders the index page of the web application.

    Returns:
        str: Rendered HTML content for the index page.
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=4000)
