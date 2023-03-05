import nltk
nltk.download('vader_lexicon') # Download the VADER lexicon for sentiment analysis

from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Create an instance of the sentiment analyzer
sid = SentimentIntensityAnalyzer()

# Sample text for sentiment analysis
text = "I love using Python for natural language processing. It's so easy and powerful!"

# Analyze the sentiment of the text
scores = sid.polarity_scores(text)

# Extract the positive, negative, and neutral scores
positive_score = scores['pos']
negative_score = scores['neg']
neutral_score = scores['neu']

# Determine the most prominent sentiment
if positive_score > negative_score and positive_score > neutral_score:
    sentiment = 'positive'
elif negative_score > positive_score and negative_score > neutral_score:
    sentiment = 'negative'
else:
    sentiment = 'neutral'

# Print the most prominent sentiment
print(sentiment)
