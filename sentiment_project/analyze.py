import pandas as pd
data = pd.read_csv("customer_review.csv",on_bad_lines='skip')
print(data.head())
from textblob import TextBlob

# Function to get sentiment
def get_sentiment(text):
    analysis = TextBlob(text)
    if analysis.sentiment.polarity > 0:
        return "Positive"
    elif analysis.sentiment.polarity == 0:
        return "Neutral"
    else:
        return "Negative"

# Add sentiment column
data['Sentiment'] = data['Review'].apply(get_sentiment)

# Show updated data
print(data)
# Count how many Positive/Negative/Neutral
sentiment_counts = data['Sentiment'].value_counts()
print(sentiment_counts)
import matplotlib.pyplot as plt
import seaborn as sns

# Bar chart
sns.countplot(x='Sentiment', data=data)
plt.title("Sentiment Counts")
plt.show()
