import streamlit as st
import pandas as pd
from textblob import TextBlob
import matplotlib.pyplot as plt

# Load the CSV data
data = pd.read_csv("customer_review.csv", on_bad_lines='skip')

# Add Sentiment Column
def get_sentiment(text):
    analysis = TextBlob(text)
    if analysis.sentiment.polarity > 0:
        return "Positive"
    elif analysis.sentiment.polarity == 0:
        return "Neutral"
    else:
        return "Negative"

# Apply sentiment analysis
data['Sentiment'] = data['Review'].apply(get_sentiment)

# Streamlit App UI
st.title("📊 Customer Review Sentiment Dashboard")

# Show the data table
st.subheader("📋 Raw Data with Sentiment")
st.dataframe(data)

# Sentiment counts
sentiment_counts = data['Sentiment'].value_counts()

# Show bar chart
st.subheader("📌 Sentiment Counts")
st.bar_chart(sentiment_counts)

# Show pie chart
st.subheader("📎 Sentiment Pie Chart")
fig, ax = plt.subplots()
sentiment_counts.plot.pie(autopct='%1.1f%%', startangle=90, ax=ax)
ax.set_ylabel("")
st.pyplot(fig)
