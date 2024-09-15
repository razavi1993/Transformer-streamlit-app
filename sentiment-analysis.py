import streamlit as st
from transformers import pipeline

analyze_sentiment = pipeline('sentiment-analysis')

with st.form("Sentiment Analysis"):
    text = st.text_area(label="Enter Text")
    st.form_submit_button(label="Analyze sentiment")

if text:
    answer = analyze_sentiment(text)
    st.write(answer)




