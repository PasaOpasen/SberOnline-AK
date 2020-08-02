# -*- coding: utf-8 -*-
"""
Created on Sun Jul  5 14:20:38 2020

@author: qtckp
"""

import sys, os, io
sys.path.append(os.path.dirname(__file__))

from Ngrams import txt_list_to_grams

from stemmer_rus import Get_dictionary_values, Stem_text, get_soft_skills2

from prepare_functions import *



def get_content_from_text(lines_of_text, vocab = None):
    
    grams = txt_list_to_grams(lines_of_text,0)
    #print(grams)
    
    h = []
    
    s = []
    
    for g in grams:
        if has_more_than_x_russian_symbols(g,2):
            s.append(g)
        else:
            h.append(g)
    #print(s);print(h)
    if vocab == None:
        soft_skills = get_soft_skills2(s, h)
    else:
        soft_skills = get_soft_skills2(s, h, vocab)
    
    
    return soft_skills



if __name__=='__main__':
    
    
    with io.open("0.txt",'r', encoding = 'utf-8') as f:
        doclines = f.readlines()
        
    answer = get_content_from_text(doclines)
    print(answer)
    
    

