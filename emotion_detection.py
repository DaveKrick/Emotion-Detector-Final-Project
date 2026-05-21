import requests

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }
    myObject = {
        "raw_document": {
            "text": text_to_analyze
        }
    }
    response = requests.post(url, json = myObject, headers=header)
    
    #Convert response to json
    jsonResponse = response.json()
    
    #Get all emotions from jsonResponse
    emotions = jsonResponse["emotionPredictions"][0]["emotion"]
    
    #Find dominant emotion name
    dominant_emotion = max(emotions, key=emotions.get)
    
    #Add dominant emotion do dictionary/json
    emotions["dominant_emotion"] = dominant_emotion

    return emotions