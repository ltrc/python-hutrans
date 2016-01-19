#!/usr/bin/env python 
#!-*- coding: utf-8 -*-

# Copyright Irshad Ahmad Bhat 2015

"""
Transliteration Tool:
Devnagri to Persio-Arabic transliterator for hindi-urdu transliteration
"""

import os
import re
import sys
import string
import warnings

import numpy as np

import viterbi
import one_hot_repr
from converter_indic import wxConvert

warnings.filterwarnings("ignore")

class DP_Transliterator():
    """Transliterates words from Hindi to Urdu"""

    def __init__(self):        
        self.lookup = dict()
        self.esc_ch = '\x00'
        self.tab = '\x01\x02'
        self.space = '\x02\x01'

        self.fit()

    def fit(self):
        self.con = wxConvert(order='utf2wx', rmask=False)
        path = os.path.abspath(__file__).rpartition('/')[0]

        #load models
        sys.path.append(path)
        self.coef_            = np.load('%s/models/hu_coef.npy' %path)[0]
        self.classes_         = np.load('%s/models/hu_classes.npy' %path)[0]
        self.vectorizer_      = np.load('%s/models/hu_sparse-vec.npy' %path)[0]
        self.intercept_init_  = np.load('%s/models/hu_intercept_init.npy' %path)
        self.intercept_trans_ = np.load('%s/models/hu_intercept_trans.npy' %path)
        self.intercept_final_ = np.load('%s/models/hu_intercept_final.npy' %path)
        
        #initialize character maps  
        self.letters = set(string.ascii_letters)
        self.mask_roman = re.compile(r'([a-zA-Z]+)')
        self.rom_dev = re.compile(ur'([a-zA-Z])([\u0900-\u097f])')
        self.dev_rom = re.compile(ur'([\u0900-\u097f])([a-zA-Z])')
        self.non_alpha = re.compile(r"([^a-zA-Z%s]+)" %(self.esc_ch))

        #initialize punctuation map table
        self.punkt_tbl = dict()
        with open('%s/mapping/punkt.map' %path) as punkt_fp:
            for line in punkt_fp:
                line = line.decode('utf-8')
                s,t = line.split()
                if s in ["'", '"']: 
                    continue
                self.punkt_tbl[ord(s)] = t

    def feature_extraction(self, letters):
        ngram = 4
        out_letters = list()
        dummies = ["_"] * ngram
        context = dummies + letters + dummies
        for i in range(ngram, len(context)-ngram):
            unigrams  = context[i-ngram: i] + [context[i]] + context[i+1: i+(ngram+1)]
            bigrams   = ["%s|%s" % (p,q) for p,q in zip(unigrams[:-1], unigrams[1:])]
            trigrams  = ["%s|%s|%s" % (r,s,t) for r,s,t in zip(unigrams[:-2], unigrams[1:], unigrams[2:])]
            quadgrams = ["%s|%s|%s|%s" % (u,v,w,x) for u,v,w,x in zip(unigrams[:-3], unigrams[1:], unigrams[2:], unigrams[3:])]
            ngram_context = unigrams + bigrams + trigrams + quadgrams
            out_letters.append(ngram_context)

        return out_letters

    def predict(self, word):
        X = self.vectorizer_.transform(word)
        scores = X.dot(self.coef_.T).toarray()
        y = viterbi.decode(scores, self.intercept_trans_, 
                           self.intercept_init_, self.intercept_final_)

        y = [self.classes_[pid] for pid in y]
        y = ''.join(y)

        return y.replace('_', '')

    def case_trans(self, word):
        if word in self.lookup:
            return self.lookup[word]
        word_feats = ' '.join(word).replace(' a', 'a')
        word_feats = word_feats.replace(' Z', 'Z')
        word_feats = word_feats.encode('utf-8').split()
        word_feats = self.feature_extraction(word_feats)
        op_word = self.predict(word_feats)
        self.lookup[word] = op_word

        return op_word

    def transliterate(self, text):
        if isinstance(text, str):
            text = text.decode('utf-8')
        trans_list = list()
        text = self.rom_dev.sub(r'\1 \2', text)
        text = self.dev_rom.sub(r'\1 \2', text)
        text = self.mask_roman.sub(r'%s\1' %(self.esc_ch), text)
        text = self.con.convert(text) # Convert to wx
        text = text.decode('utf-8') 
        text = text.replace('\t', self.tab)
        text = text.replace(' ', self.space)
        lines = text.split("\n")
        for line in lines:
            if not line.strip():
                trans_list.append(line.encode('utf-8'))
                continue
            trans_line = str()
            line = self.non_alpha.split(line)
            for word in line:
                if not word:
                    continue
                elif word[0] == self.esc_ch:
                    word = word[1:]
                    word = word.encode('utf-8')
                    trans_line += word
                elif word[0] not in self.letters:
                    punkt_trans = word.translate(self.punkt_tbl)
                    punkt_trans = punkt_trans.encode('utf-8')
                    trans_line += punkt_trans
                else:
                    op_word = self.case_trans(word)
                    trans_line += op_word
            trans_list.append(trans_line)

        trans_line = '\n'.join(trans_list)
        trans_line = trans_line.replace(self.space, ' ')
        trans_line = trans_line.replace(self.tab, '\t')

        return trans_line
