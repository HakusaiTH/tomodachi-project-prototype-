import openai
import nltk
nltk.download('vader_lexicon') 

from nltk.sentiment.vader import SentimentIntensityAnalyzer

sid = SentimentIntensityAnalyzer()

openai.api_key = "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"

model_engine = "text-davinci-003"

text = str(input("type :"))

completion = openai.Completion.create(
    engine=model_engine,
    prompt=text,
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=0.5,
)

response = completion.choices[0].text
scores = sid.polarity_scores(response)

positive_score = scores['pos']
negative_score = scores['neg']
neutral_score = scores['neu']

if positive_score > negative_score and positive_score > neutral_score:
    sentiment = 'positive'
elif negative_score > positive_score and negative_score > neutral_score:
    sentiment = 'negative'
else:
    sentiment = 'neutral'

print(text)
print(f'{response}  "{sentiment}"')