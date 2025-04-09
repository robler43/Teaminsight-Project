from get_insights import analyze_feedback
from emotion_detector import detect_emotion

def full_analysis(text):
    analysis = analyze_feedback(text)
    emotion, confidence = detect_emotion(text)

    return {
        "feedback": text,
        "gpt_analysis": analysis,
        "emotion": emotion,
        "confidence": confidence
    }

# Test it
result = full_analysis("Our standups feel useless. No one’s engaged.")
print(result)