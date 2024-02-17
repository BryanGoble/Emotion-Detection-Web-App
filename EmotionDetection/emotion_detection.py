import requests, json

def emotion_detector(input_text):
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    payload = { "raw_document": { "text": input_text } }

    data = requests.post(url, headers=header, json=payload)
    
    # Check the status code of the response
    if data.status_code == 200:
        emotion_dict = json.loads(data.text)
        emotions = emotion_dict["emotionPredictions"][0]["emotion"]
        dominant_emotion = max(emotions, key=emotions.get)

        result = {
            'anger': emotions.get('anger', 0),
            'disgust': emotions.get('disgust', 0),
            'fear': emotions.get('fear', 0),
            'joy': emotions.get('joy', 0),
            'sadness': emotions.get('sadness', 0),
            'dominant_emotion': dominant_emotion
        }
    elif data.status_code == 400:
        # Return a dictionary with None values for all keys if status code is not 200
        result = {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
    else:
        result = f"Error: Status Code {data.status_code}"

    return result


# Testing Purposes
# if __name__ == "__main__":
#     emotion_detector("I love this new technology.")