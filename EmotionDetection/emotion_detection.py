import json
import requests

# Define a function named emotion_detector that takes a string input (text_to_analyse)
def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyze } }

    # Send a POST request to the API with the text and headers
    response = requests.post(url, json = myobj, headers=header)

    if response.status_code == 400:
        return 'empty'

    # Parsing the JSON response from the API
    json_response = json.loads(response.text)

    # Extracting the set of emotions
    set_of_emotions = json_response['emotionPredictions'][0]['emotion']

    # Defining max emotion
    max_emotion = max(set_of_emotions, key=set_of_emotions.get)

    # Appending dominant emotion
    set_of_emotions['dominant_emotion'] = max_emotion

    # Return output
    return set_of_emotions