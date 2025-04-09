import streamlit as st
from teaminsight import full_analysis

st.title("🧠 TeamInsight: Feedback Analyzer")

user_input = st.text_area("Paste team feedback below:")

if st.button("Analyze"):
    if user_input:
        result = full_analysis(user_input)
        st.subheader("🔍 Result")
        st.write(result["gpt_analysis"])
        st.subheader("🎭 Detected Emotion")
        st.write(f"{result['emotion']} (Confidence: {result['confidence']}/1)")
    else:
        st.warning("Please enter some feedback.")