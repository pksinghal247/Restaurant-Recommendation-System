import  numpy as np
import pandas as pd

df = pd.read_csv('temp.csv')
print('Data Loaded...')

li = []
for val in df['phone']:
    ph = ''
    val = val.replace('\n', ', ')
    val = val.replace('\n\n', ', ')
    val = val.replace('\n\n\n', ', ')
    val = val.replace('\n\n\n\n', ', ')
    ph = ph + val
    li.append(ph)

del df['phone']
df['phone'] = li

print(df.shape)

df.drop_duplicates(keep='first',inplace=True)
print(df.shape)

df.to_csv('temp_final.csv')

df = pd.read_csv('temp_final.csv')

li = []
for val in df['phone']:
    ph = ''
    val = val.replace(', , ', ', ')
    ph = ph + val
    li.append(ph)

del df['phone']
df['phone'] = li

print(df.shape)

df.drop_duplicates(keep='first',inplace=True)
print(df.shape)

df.to_csv('temp2.csv')

import csv
import json

with open('temp2.csv', "r") as file_in:
    with open('final.json', "w") as file_out:
        csvReader = csv.DictReader(file_in)
        for rows in csvReader:
            file_out.write(json.dumps(rows, indent=5    ))