#!/usr/bin/env python 
#!-*- coding: utf-8 -*-

"""
Transliteration Tool:
Persio-Arabic to Devnagari transliterator for Urdu-Hindi transliteration
"""

import re
import os
import sys
import warnings

import numpy as np

import viterbi
import one_hot_repr
from converter_indic import wxConvert

warnings.filterwarnings("ignore")

__author__ = "Irshad Ahmad Bhat"
__version__ = "1.0"
__email__ = "irshad.bhat@research.iiit.ac.in"

class PD_Transliterator():
    """Transliterates words from Urdu to Hindi"""

    def __init__(self): 
        self.n = 4
        self.tab = chr(1)*2
        self.space = chr(2)*2
        self.lookup = dict()
        self.con = wxConvert(order='wx2utf')
        path = os.path.abspath(__file__).rpartition('/')[0]
	sys.path.append(path)
	self.coef_ = np.load('%s/models/uh_coef.npy' %path)[0]
        self.vec = np.load('%s/models/uh_sparse-vec.npy' %path)[0]
	self.classes_ = np.load('%s/models/uh_classes.npy' %path)[0]
        self.intercept_init_ = np.load('%s/models/uh_intercept_init.npy' %path)
        self.intercept_trans_ = np.load('%s/models/uh_intercept_trans.npy' %path)
        self.intercept_final_ = np.load('%s/models/uh_intercept_final.npy' %path)
	self.lrange = set(range(int("0x0621", 16), int("0x063b", 16))) | \
		      set(range(int("0x0641", 16), int("0x064b", 16))) | \
		      set(range(int("0x0674", 16), int("0x06d4", 16))) 
	self.digits_ = set(range(int("0x0660", 16), int("0x066a", 16))) | \
		       set(range(int("0x06f0", 16), int("0x06fa", 16))) 
	self.letters = re.compile(u'([^\u0621-\u063a\u0641-\u064a\u0674-\u06d3]+)')

	self.punkt_str = str()
	self.punkt_tbl = dict()
        with open('%s/extras/punkt.map' %path) as punkt_fp:
       	    for line in punkt_fp:
		line = line.decode('utf-8')
		s,t = line.split()
		self.punkt_str += t	
		self.punkt_tbl[ord(t)] = s

    def feature_extraction(self, letters):
        out_letters = list()
        dummies = ["_"] * self.n
        context = dummies + letters + dummies
        for i in range(self.n, len(context)-self.n):
            current_token = context[i]
            wordContext = context[i-self.n:i] + [current_token] + context[i+1:i+(self.n+1)]
            word_ngram_context = wordContext + ["%s|%s" % (p,q) for p,q in zip(wordContext[:-1], wordContext[1:])] + \
                ["%s|%s|%s" % (r,s,t) for r,s,t in zip(wordContext[:-2], wordContext[1:], wordContext[2:])] +\
                ["%s|%s|%s|%s" % (u,v,w,x) for u,v,w,x in zip(wordContext[:-3],wordContext[1:],wordContext[2:],wordContext[3:])] #+\
            out_letters.append(word_ngram_context)
        return out_letters

    def predict(self, word):   
        X = self.vec.transform(word)
        scores = X.dot(self.coef_.T).toarray() 

        y = viterbi.decode(scores, self.intercept_trans_,
               self.intercept_init_, self.intercept_final_)

        y =  [self.classes_[pred] for pred in y]
        return re.sub('_','',''.join(y))

    def case_trans(self, word):
        if word in self.lookup:
            return self.lookup[word]
        word_feats = ' '.join(word).replace(u' ھ', u'ھ').encode('utf-8').split()
        word_feats = self.feature_extraction(word_feats)
        op_word = self.con.convert(self.predict(word_feats))
        self.lookup[word] = op_word

        return op_word

    def transliterate(self, text):
        tline = str()
	if not isinstance(text, unicode):
	    text = text.decode('utf-8')
        lines = text.split("\n")
	for line in lines:
	    if not line.strip():
                tline += "\n"
		continue
            line = line.replace('\t', self.tab)
            line = line.replace(' ', self.space)
            # remove vowels
            line = re.sub(ur'([\u064b\u0670\u0650\u0651\u064f\u064e]+)', r'', line)
	    # normalize
	    line = line.replace(u'ه', u'ہ')
	    line = line.replace(u'للہ', u'للاہ')
	    line = line.replace(u'ا\u0670', u'ن')
	    line = re.sub(u'([^کگچجٹڈتدپب])ھ([یے])', ur'\1ہ\2', line)
            line = self.letters.split(line)
            for word in line:
		if not word:
		    continue
		if word == self.space:
		    tline += " "
		elif word == self.tab:
		    tline += "\t"
		elif ord(word[0]) not in self.lrange:
		    tline += word.translate(self.punkt_tbl).encode('utf-8')
		else:
		    tline += self.case_trans(word)
	    tline += "\n"

	tline = tline.replace(self.tab, '\t')
	tline = tline.replace(self.space, ' ').strip()
        return tline
