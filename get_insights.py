import os
from openai import OpenAI 
from dotenv import load_dotenv
from transformers import pipeline

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=api_key)

def analyze_feedback(feedback_text):
    prompt = f"""
    You are a smart assistant helping teams improve.
    Analyze this team feedback:
    - List key communication or productivity issues
    - Suggest ways to improve
    - Be concise but insightful

    Feedback:
    \"\"\"{feedback_text}\"\"\"
    """

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content

emotion_detector = pipeline("text-classification", model="distilbert-base-uncased-finetuned-sst-2-english")

def detect_emotion(feedback_text):
    result = emotion_detector(feedback_text)
    label = result[0]['label']
    score = result[0]['score']
    return f"Detected emotion: {label} (confidence: {score:.2f})"
