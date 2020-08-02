# -*- coding: utf-8 -*-
"""
Created on Sun Aug  2 00:40:33 2020

@author: qtckp
"""

from tonality.get_ton import tonality


if __name__ == '__main__':
    
    
    
    lines = ['очень хорошие банк', 'не могу провести оплату, постоянно вылетает']
    
    for txt in lines:
        print(tonality(txt))





