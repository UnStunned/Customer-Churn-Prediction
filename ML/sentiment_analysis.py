import flair
import pandas as pd

df = pd.read_csv('/content/sample_data/final_data.csv')
df.head()

sentiment_model = flair.models.TextClassifier.load('en-sentiment')
sentiment = []
for sentence in df['text_']:
  sample = flair.data.Sentence(sentence)
  sentiment_model.predict(sample)
  sentiment.append(sample.labels[0].value)

print(sentiment)

df['sentiment'] = sentiment
df.to_csv('/content/sample_data/sentiment_analysis.csv')

subset = df.head(25)

for sentence in subset['text_']:
  sample = flair.data.Sentence(sentence)
  sentiment_model.predict(sample)
  print(sample)
  print(sample.labels[0].value, end=" ")
  print(sample.labels[0].score)