# -*- coding: utf-8 -*-
"""
Created on Sun Aug  2 00:09:21 2020

@author: qtckp
"""

from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import TfidfVectorizer
import re
import json
import Stemmer
import os, sys
import pickle

sys.path.append(os.path.dirname(__file__))

def combiner(file_name):
    return os.path.join(os.path.dirname(__file__), file_name)

TOKEN_RE = re.compile(r'[\w\d]+')
stemmer = Stemmer.Stemmer('russian')
rep_symb = [('ё', 'е')]


def replacor(txt):
    return txt.replace(rep_symb[0][0], rep_symb[0][1])

def tokenize_text_simple_regex_stemming(txt, min_token_size = 2):
    all_tokens = TOKEN_RE.findall(replacor(txt.lower()))
    return [stemmer.stemWord(token) for token in all_tokens if len(token) >= min_token_size or token[-1].isdigit()]


def delete_bad_words(txt, words):
    return ' '.join([word for word in txt.split() if word in words])

def get_grams_and_vocs():
    with open(combiner('grams.txt'),'r') as f:
        grams = [line.rstrip() for line in f.readlines()]
        grams = {' '.join(g.split('_')): ''.join(g.split('_')) for g in grams}
        # это чтобы сначала заменялись триграммы
        grams = {k: v for k, v in sorted(grams.items(), key = lambda item: sum([s == ' ' for s in item[0]])) } 
    with open(combiner("total_voc.json"), "r") as read_file:
        total_voc = json.load(read_file)
        vocs = set(total_voc.keys()).union(set('12345'))    
    return grams, vocs
    
def get_models():
    
    tfidf = pickle.load(open(combiner('tfidf.model'),'rb'))
    logreg = pickle.load(open(combiner('logreg.model'),'rb'))
    
    return tfidf, logreg


def prepare_text(txt, grams, vocs):
    
    txt = ' '.join(tokenize_text_simple_regex_stemming(txt))
    
    
    for k in grams.keys():
        if k in txt:
            txt = txt.replace(k, grams[k])
    
    return delete_bad_words(txt, vocs)

grams, vocs = get_grams_and_vocs()
tf, fit = get_models()

def get_tonality(txt, grams, vocs, tokenizer, model):
    
    txt = prepare_text(txt, grams, vocs)
    
    vec = tokenizer.transform([txt])
    
    p = model.predict_proba(vec)
    
    return p[0][1]*2-1


def tonality(txt):
    return get_tonality(txt, grams, vocs, tf, fit)

# if __name__ == '__main__':
    
#     grams, vocs = get_grams_and_vocs()
#     tf, fit = get_models()
    
#     lines = ['плохо работает', 'конченный банк', 'лагает при запуске', 'отвратительно, лагает много', 'доволен', "))))"]
#     for line in lines:
#         print(get_tonality(line, grams, vocs, tf, fit))
        
    
    
    
    
    
    
    
    
    
    
    

