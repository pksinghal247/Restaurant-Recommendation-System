import  numpy as np
import pandas as pd
from textblob import TextBlob

df = pd.read_csv('Banglore.csv')
print('Data Loaded...')


print(df.columns)


senti = []
i = 1
for val in df['Reviews']:
    blob = TextBlob(val)
    polarity = blob.polarity

    if polarity >= 0.25:
        sentiment = 'Positive'
    elif polarity < 0:
        sentiment = 'Negative'
    else:
        sentiment = 'Neutral'
    senti.append(sentiment)
    print(f'{i}/{len(df["Reviews"])} Sentiment Analyzed...')
    i += 1

df['Sentiment'] = senti

del df['Reviews']

df.to_csv('temp.csv')
print('Data Written to csv.')