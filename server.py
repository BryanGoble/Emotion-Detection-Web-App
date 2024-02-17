"""
This module contains the Flask server for the Emotion Detection application.
"""
from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

# Route for serving index.html
@app.route('/')
def index():
    """
    Render the index.html template.
    """
    return render_template('index.html')

# Route for processing emotion detection requests
@app.route('/emotionDetector', methods=['GET'])
def analyze_emotion():
    """
    Analyze the emotion in the input text and return the result.
    """
    text_to_analyze = request.args.get('textToAnalyze')

    result = emotion_detector(text_to_analyze)

    # Check if dominant_emotion is None
    if result['dominant_emotion'] is None:
        # Return an error message
        return "Invalid text! Please try again!"

    text_response = (
    f"For the given statement, the system response is 'anger': {result['anger']}, "
    f"'disgust': {result['disgust']}, 'fear': {result['fear']}, 'joy': {result['joy']} "
    f"and 'sadness': {result['sadness']}. The dominant emotion is {result['dominant_emotion']}."
    )

    # Return the text response
    return text_response

if __name__ == '__main__':
    app.run(port=5000)
