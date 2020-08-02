# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 01:56:11 2020

@author: qtckp
"""


import re
from gensim.models.phrases import Phrases, Phraser, original_scorer
#from gensim.test.utils import datapath
#from gensim.models.word2vec import Text8Corpus
from collections import defaultdict

with open('cleaned.txt','r', encoding = 'utf-16') as f:
    #lines = [line.split() for line in f.readlines()]
    lines = [line.rstrip(' 12345').split() for line in f]


bigram = Phrases(lines, min_count = 1)
bigram_transformer = Phraser(bigram)


def text_generator_bigram():
    for text in lines:
        yield bigram_transformer[ text ]

trigram = Phrases(text_generator_bigram(), min_count = 1)

grams = {}

decode_format = 'utf-8'



vocab2 = bigram.vocab
bi_vocab = defaultdict(list)
for p, c in vocab2.items():
    if re.findall('_', p.decode(decode_format)):
        bi_vocab[c].append(p)
        
len_vocab = float(len(vocab2))
min_count = float(bigram.min_count)
corpus_word_count = float(bigram.corpus_word_count)
print('-----> Table of bigrams')
for c in sorted(bi_vocab.keys(),reverse=True):
    for val in bi_vocab[c]:
        if any((v.isalpha() for v in val.decode(decode_format))):
            [worda, wordb] = re.split(b'_', val,1)
            
            s1 = vocab2[worda]
            s2 = vocab2[wordb]
            
            if s1>0 and s2 >0:
                score = original_scorer(
                    worda_count=float(s1),
                    wordb_count=float(s2),
                    bigram_count=float(c),
                    len_vocab=len_vocab, min_count=min_count, corpus_word_count = corpus_word_count)
                if c>100:
                    print(f"{val.decode(decode_format):10} {c:5} \t{score:.4}")
                grams[val.decode(decode_format)] = (c, score)
        





vocab3 = trigram.vocab
tri_vocab = defaultdict(list)
for p, c in vocab3.items():
    if len(re.findall(b'_', p)) == 2:
        tri_vocab[c].append(p)


len_vocab = float(len(vocab3))
min_count = float(trigram.min_count)
corpus_word_count = float(trigram.corpus_word_count)


print('-----> Table of trigrams')
comb = lambda x, y: x+b'_'+y
for c in sorted(tri_vocab.keys(),reverse=True):
    for val in tri_vocab[c]:
        if any((v.isalpha() for v in val.decode(decode_format))):
            #print(val.decode(decode_format))
            [worda, wordb, wordc] = re.split(b'_', val, 2)
            
            #print(worda.decode(decode_format), wordb.decode(decode_format), wordc.decode(decode_format))
            
            score = 0.0
            
            s1 = vocab3[worda]
            s2 = vocab3[comb(wordb,wordc)]
            
            #print(f'{s1} {s2}')
            
            if s1 > 0 and s2 > 0:
                score += original_scorer(
                    worda_count=float(s1),
                    wordb_count=float(s2),
                    bigram_count=float(c),
                    len_vocab=len_vocab, min_count=min_count, corpus_word_count = corpus_word_count)
            
            s1 = vocab3[comb(worda, wordb)]
            s2 = vocab3[wordc]
            
            if s1 > 0 and s2 > 0:
                score += original_scorer(
                    worda_count=float(s1),
                    wordb_count=float(s2),
                    bigram_count=float(c),
                    len_vocab=len_vocab, min_count=min_count, corpus_word_count = corpus_word_count)
                       
            if score > 0 and c>100:       
                    print(f"{val.decode(decode_format):22} {c:5} \t{score:.6}")
                    grams[val.decode(decode_format)] = (c, score)




# print('-----> Table of trigrams')
# comb = lambda x, y: x+b'_'+y
# for c in sorted(tri_vocab.keys(),reverse=True)[:20]:
#     for val in tri_vocab[c]:
#         #print(val.decode(decode_format))
#         [worda, wordb] = re.split(b'_', val, 1)
        
#         #print(worda.decode(decode_format), wordb.decode(decode_format), wordc.decode(decode_format))
        
#         score = 0.0
        
#         s1 = vocab3[worda]
#         s2 = vocab3[wordb]
        
#         #print(f'{s1} {s2}')
        
#         if s1 > 0 and s2 > 0:
#             score += original_scorer(
#                 worda_count=float(s1),
#                 wordb_count=float(s2),
#                 bigram_count=float(c),
#                 len_vocab=len_vocab, min_count=min_count, corpus_word_count = corpus_word_count)
        
#             if score > 0:       
#                 print(f"{val.decode(decode_format):15} {c:5} \t{score:.4}")



grams = {k: v for k, v in sorted(grams.items(), key = lambda item: (len(item[0].split('_')), item[1][0], item[1][0]), reverse = True)}

for k in list(grams.keys())[:15]:
    print(f'{k} {grams[k]}')


with open('grams.txt', 'w') as f:
    f.writelines([line + '\n' for line, (c, s) in grams.items() if c > 100 and s > 1])








