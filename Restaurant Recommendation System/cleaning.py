import numpy as np
import pandas as pd
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Load data
data=pd.read_csv('/home/sunbeam/Downloads/zomato.csv')
print('loaded')
# Delete unnecessary Column
del data['url']
del data['location']
del data['listed_in(type)']
del data['menu_item']
del data['votes']

print('deleted')
# change useless  values with NA
data['rate'] = data['rate'].replace('NEW',np.NaN)
data['rate'] = data['rate'].replace('-',np.NaN)

# Change names of few columns
data=data.rename(columns={'approx_cost(for two people)':'cost','listed_in(type)':'type', 'listed_in(city)':'city', 'reviews_list': 'reviews', 'rest_type': 'type'})
# remove /5 from rateand convert into float
data.rate=data.rate.astype(str)
data.rate=data.rate.apply(lambda x : x.replace('/5',''))
data.rate = data.rate.astype(float)

# remove , from cost column
data.cost = data.cost.astype(str)
data.cost = data.cost.apply(lambda x : x.replace(',',''))
data.cost = data.cost.astype(float)
data.reviews = data.reviews.apply(lambda x : x.replace('.',' '))

# remove unnecessary data  from phone column and seperate phone numbers with comma(,)
data.phone = data.phone.astype(str)
data.phone = data.phone.apply(lambda x : x.replace('\r\n',','))

# Drop all rows containing NA values
data.dropna(how='any',inplace=True)

# Drop rows containing Duplicate values
data.drop_duplicates(keep='first',inplace=True)
print('duplicate deleted')
# Remove stopwords and punctuations from 'reviews'
import string
punctuation = []
for symbol in string.punctuation:
    punctuation.append(symbol)
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '😍']
stop_words = set(stopwords.words('english'))
stop_words.add('rated')
stop_words.add('ratedn')
new_col = []
print('review cleaning started...')
i = 1
for val in data['reviews']:
    words = []
    for char in punctuation:
        val = val.replace(char, '')
    for char in numbers:
        val = val.replace(char, '')
    word = word_tokenize(val)
    for val in word:
        words.append(val.lower())
    filter = [w for w in words if not w in stop_words]
    val = ''
    for word in filter:
        val = val + word + ' '
    new_col.append(val)
    print(f'{i} out of {len(data["reviews"])} reviews cleaned...')
    i += 1

del data['reviews']
data['Reviews'] = new_col
print('new column added')
data.to_csv('temp.csv',sep=',')
print(data.shape)
data = pd.read_csv('temp.csv')
data.dropna(how='any',inplace=True)
print(data.shape)
data.to_csv('Banglore.csv',sep=',')