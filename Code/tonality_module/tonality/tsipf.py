# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 22:42:14 2020

@author: qtckp
"""




with open('cleaned_grams.txt','r', encoding = 'utf16') as f:
    #lines = [line.split() for line in f.readlines()]
    lines = [line.strip() for line in f.readlines()]



# https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.CountVectorizer.html
from sklearn.feature_extraction.text import CountVectorizer

vectorizer = CountVectorizer()

X = vectorizer.fit_transform(lines)

vectorizer.get_feature_names()


# most popular words

d = dict(zip(vectorizer.get_feature_names(), X.sum(axis=0).tolist()[0]))

d = {k:v for k, v in sorted(d.items(), key=lambda item: item[1], reverse = True)}

k = 0

for word, count in d.items():
    print(f'{word}: {count}')
    k += 1
    if k == 50:
        break
    
print(f'total words: {sum(d.values())}, unique: {len(d)}') 



import matplotlib.pyplot as plt

plt.hist(d.values(), log = True, bins = 100, color = 'green')
plt.suptitle('Histogram of word counts')
plt.title(f'total words: {sum(d.values())}, unique: {len(d)}')

plt.show()    
    


with open('not deleted words.txt','r', encoding = 'utf-8') as f:
    not_del = [line.rstrip() for line in f if len(line) > 1]
    not_del = set(not_del)


total_vocab = {k: v for k, v in d.items() if (v > 75 and v < 5000) or k in not_del }
print(f'total words: {sum(total_vocab.values())}, unique: {len(total_vocab)}') 



import json

with open('total_voc.json','w') as f:
    json.dump(total_vocab,f, indent = 4)









