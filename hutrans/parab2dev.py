#!/usr/bin/env python 
#!-*- coding: utf-8 -*-

# Copyright Irshad Ahmad Bhat 2015

"""
Transliteration Tool:
Persio-Arabic to Devnagari transliterator for Urdu-Hindi transliteration
"""

import re
import os
import sys
import string
import warnings

import numpy as np

import viterbi
import one_hot_repr
from converter_indic import wxConvert

warnings.filterwarnings("ignore")

class PD_Transliterator():
    """Transliterates words from Urdu to Hindi"""

    def __init__(self): 
        self.lookup = dict()
        self.space = '\x02\x03' 

        self.fit()

    def fit(self):
        self.con = wxConvert(order='wx2utf', rmask=False)
        path = os.path.abspath(__file__).rpartition('/')[0]

        #load models
        sys.path.append(path)
        self.coef_            = np.load('%s/models/uh_coef.npy' %path)[0]
        self.classes_         = np.load('%s/models/uh_classes.npy' %path)[0]
        self.vectorizer_      = np.load('%s/models/uh_sparse-vec.npy' %path)[0]
        self.intercept_init_  = np.load('%s/models/uh_intercept_init.npy' %path)
        self.intercept_trans_ = np.load('%s/models/uh_intercept_trans.npy' %path)
        self.intercept_final_ = np.load('%s/models/uh_intercept_final.npy' %path)
    
        #compile regexes
        self.non_alpha = re.compile(u'([^\u0621-\u063a\u0641-\u064a\u0674-\u06d3]+)')

        #initialize character maps    
        self.ascii_letters = set(string.ascii_letters)
        self.letter_set = set([unichr(i) for i in range(int("0x0621", 16), int("0x063b", 16))]) | \
                          set([unichr(i) for i in range(int("0x0641", 16), int("0x064b", 16))]) | \
                          set([unichr(i) for i in range(int("0x0674", 16), int("0x06d4", 16))])

        #initialize punctuation map table
        self.punkt_tbl = dict()
        with open('%s/mapping/punkt.map' %path) as punkt_fp:
            for line in punkt_fp:
                line = line.decode('utf-8')
                src, trg = line.split()
                self.punkt_tbl[ord(trg)] = src

        #initialize urdu normalization table
        self.canonical_eq = dict()
        with open('%s/mapping/urdu_urdu.map' %path) as nu_fp:
            for line in nu_fp:
                line = line.decode('utf-8')
                src, trg = line.split()
                self.canonical_eq[ord(src)] = trg

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

        y =  [self.classes_[pid] for pid in y]
        y = ''.join(y)

        return y.replace('_', '') 

    def case_trans(self, word):
        if word in self.lookup:
            return self.con.convert(self.lookup[word])
        word_feats = ' '.join(word)
        word_feats = word_feats.replace(u' \u06be', u'\u06be')
        word_feats = word_feats.encode('utf-8')
        word_feats = word_feats.split()
        word_feats = self.feature_extraction(word_feats)
        op_word = self.predict(word_feats)
        self.lookup[word] = op_word

        return self.con.convert(op_word)

    def unicode_equivalence(self, line):
        line  = line.translate(self.canonical_eq)
        #hamza and mada normalizations
        line = line.replace(u'\u0627\u0653', u'\u0622')
        line = line.replace(u'\u0648\u0654', u'\u0624')
        line = line.replace(u'\u06cc\u0654', u'\u0626')
        line = line.replace(u'\u06d2\u0654', u'\u06d3')
        line = line.replace(u'\u0627\u0654', u'\u0623')
        line = line.replace(u'\u06c1\u0654', u'\u06c0')
        line = line.replace(u'\u06d5\u0654', u'\u06c0')
        
        return line

    def matra_norm(self, line):
        line = line.replace(u'\u0650', '')
        line = line.replace(u'\u064e', '')
        line = line.replace(u'\u064f', '')
        line = line.replace(u'\u0652', '')
        line = line.replace(u'\u0654', '')
        line = line.replace(u'\u0655', '')
        line = line.replace(u'\u0656', '')
        line = line.replace(u'\u0657', '')
        line = line.replace(u'\u064d', '')
        line = re.sub(u'(.)\u0651', r'\1\1', line)  # tashdeed
        line = re.sub(u'\u06cc\u0670([^\u0621-\u063a\u0641-\u064a\u0674-\u06d3])', ur'\u0627\1', line)  # khada-alif
        line = re.sub(u'\u06d2\u0670([^\u0621-\u063a\u0641-\u064a\u0674-\u06d3])', ur'\u0627\1', line)  # khada-alif
        line = re.sub(u'\u0670\u06cc([^\u0621-\u063a\u0641-\u064a\u0674-\u06d3])', ur'\u0627\1', line)  # khada-alif
        line = re.sub(u'\u0670\u06d2([^\u0621-\u063a\u0641-\u064a\u0674-\u06d3])', ur'\u0627\1', line)  # khada-alif
        line = line.replace(u'\u0627\u0670', u'\u0622') #khada-alif
        line = line.replace(u'\u0622\u0670', u'\u0622') #khada-alif
        line = line.replace(u'\u0670', u'\u0627')   #khada-alif
        line = re.sub(u'\u0627\u064b([^\u0621-\u063a\u0641-\u064a\u0674-\u06d3])', ur'\u0646\1', line)  # double-zabar 
        line = re.sub(u'\u064b\u0627([^\u0621-\u063a\u0641-\u064a\u0674-\u06d3])', ur'\u0646\1', line)  # double-zabar
        line = re.sub(u'\u064b([^\u0621-\u063a\u0641-\u064a\u0674-\u06d3])', ur'\u0646\1', line)  # double-zabar
        line = line.replace(u'\u064b', '')  #double-zabar
        line = line.replace(u'\u0644\u0644\u06c1', u'\u0644\u0644\u0627\u06c1')  #llh > llah
        line = re.sub(u'([^\u06a9\u06af\u0686\u062c\u0679\u0688\u062a\u062f\u067e\u0628\u0691])\u06be', ur'\1\u06c1', line)

        return line

    def transliterate(self, text):
        trans_list = list()
        if isinstance(text, str):
            text = text.decode('utf-8')
        #unicode_equivalence
        text = self.unicode_equivalence(text)
        #matra normalization
        text = self.matra_norm(text)
        text = text.replace(' ', self.space)
        text = text.replace('\t', self.space)
        lines = text.split("\n")
        for line in lines:
            if not line.strip():
                trans_list.append(line.encode('utf-8'))
                continue
            line = self.non_alpha.split(line)
            trans_line = str()
            for word in line:
                if not word:
                    continue
                elif word[0] not in self.letter_set:
                    punkt_trans = word.translate(self.punkt_tbl)
                    punkt_trans = punkt_trans.encode('utf-8')
                    trans_line += punkt_trans
                else:
                    trans_word = self.case_trans(word)
                    trans_line += trans_word
            trans_list.append(trans_line)
        
        trans_line = '\n'.join(trans_list)
        trans_line = trans_line.replace(self.space, ' ')
        trans_line = trans_line.replace(self.space, '\t')

        return trans_line
