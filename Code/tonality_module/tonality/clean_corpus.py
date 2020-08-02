# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 21:40:16 2020

@author: qtckp
"""


import re
import json
import Stemmer
import os

stemmer = Stemmer.Stemmer('russian')

project_dir = os.path.dirname(__file__)
project_dir = os.path.dirname(project_dir)

source = os.path.join(project_dir, r'data\useful_data\allStar.txt')

#print(source)


TOKEN_RE = re.compile(r'[\w\d]+')

rep_symb = [('ё', 'е')]

def replacor(txt):
    return txt.replace(rep_symb[0][0], rep_symb[0][1])


def tokenize_text_simple_regex(txt, min_token_size = 2):
    all_tokens = TOKEN_RE.findall(txt.lower())
    return [token for token in all_tokens if len(token) >= min_token_size or token[-1].isdigit()]


def tokenize_text_simple_regex_stemming(txt, min_token_size = 2):
    all_tokens = TOKEN_RE.findall(replacor(txt.lower()))
    return [stemmer.stemWord(token) for token in all_tokens if len(token) >= min_token_size or token[-1].isdigit()]


def delete_bad_words(txt, words):
    return ' '.join([word for word in txt.split() if word in words])


# clean text

with open(source,'r', encoding = 'utf16') as f:
    lines = f.readlines()


with open('cleaned.txt', 'w', encoding = 'utf16') as f:
    tocs = [' '.join(tokenize_text_simple_regex_stemming(line)) for line in lines]
    f.writelines([toc + '\n' for toc in tocs if toc])




# replace with ngrams

with open('cleaned.txt','r', encoding = 'utf16') as f:
    lines = f.readlines()

with open('grams.txt','r') as f:
    grams = [line.rstrip() for line in f.readlines()]
    grams = {' '.join(g.split('_')): ''.join(g.split('_')) for g in grams}
    # это чтобы сначала заменялись триграммы
    grams = {k: v for k, v in sorted(grams.items(), key = lambda item: sum([s == ' ' for s in item[0]])) }

def rep_grams(txt):
    for k in grams.keys():
        if k in txt:
            txt = txt.replace(k, grams[k])
    return txt

    
with open('cleaned_grams.txt', 'w', encoding = 'utf16') as f:
    for line in lines:
        t = rep_grams(line)

        if len(t)>2:
            f.write(t)
    
    
    


# delete some words

with open("total_voc.json", "r") as read_file:
    total_voc = json.load(read_file)
    vocs = set(total_voc.keys()).union(set('12345'))        

        
with open('cleaned_grams.txt','r', encoding = 'utf16') as f:
    lines = [delete_bad_words(line.rstrip(), vocs) for line in f]   
    
    
with open(f'cleaned{len(vocs)}.txt', 'w', encoding = 'utf16') as f:
    f.writelines([line + '\n' for line in lines if len(line) > 1])  
    
    
    
    
    
    
    
    
    

