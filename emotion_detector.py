from transformers import pipeline

emotion_pipeline = pipeline("text-classification", model="j-hartmann/emotion-english-distilroberta-base", return_all_scores=True)

def detect_emotion(text):
    results = emotion_pipeline(text)
    top_emotion = max(results[0], key=lambda x: x["score"])
    return top_emotion["label"], round(top_emotion["score"], 2)