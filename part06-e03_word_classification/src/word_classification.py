#!/usr/bin/env python3
# -*- coding: utf-8 -*- 

from collections import Counter
import urllib.request
from lxml import etree

import numpy as np

from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import cross_val_score, KFold
from sklearn import model_selection

alphabet="abcdefghijklmnopqrstuvwxyzäö-"
alphabet_set = set(alphabet)

# Returns a list of Finnish words
def load_finnish():
    finnish_url="https://www.cs.helsinki.fi/u/jttoivon/dap/data/kotus-sanalista_v1/kotus-sanalista_v1.xml"
    filename="src/kotus-sanalista_v1.xml"
    load_from_net=False
    if load_from_net:
        with urllib.request.urlopen(finnish_url) as data:
            lines=[]
            for line in data:
                lines.append(line.decode('utf-8'))
        doc="".join(lines)
    else:
        with open(filename, "rb") as data:
            doc=data.read()
    tree = etree.XML(doc)
    s_elements = tree.xpath('/kotus-sanalista/st/s')
    return list(map(lambda s: s.text, s_elements))

def load_english():
    with open("src/words", encoding="utf-8") as data:
        lines=map(lambda s: s.rstrip(), data.readlines())
    return lines

def get_features(a):
    X =  np.zeros((a.size, len(alphabet)))
    for i, string in enumerate(a):
        # counts = Counter(s)
        for j, alp in enumerate(alphabet):
            alp_count = string.count(alp)
            X[i, j] = alp_count
            # X[i, j] = counts[alp]
    print(X.shape)
    return X

def contains_valid_chars(s):
    # return alphabet_set.issuperset(s)
    set1 = set(s)
    # print(set1, s)
    if set1.issubset(alphabet_set):
        return True
    else:
        return False

def get_features_and_labels():
    fin_list, eng_list = load_finnish(), list(load_english())
    fin = np.array(list(filter(contains_valid_chars, map(lambda s: s.lower(), fin_list))))
    eng=np.array(list(filter(contains_valid_chars, map(lambda s: s.lower(), filter(lambda s: s[0].islower(), eng_list)))))
    '''
    for i, fin_word in enumerate(fin):
        lower_fin_word = fin_word.lower()
        if not contains_valid_chars(lower_fin_word):
            fin.remove(fin_word)
    for i, eng_word in enumerate(eng):
        if eng_word[0].isupper():
            eng.remove(eng_word)
        else:
            lower_eng_word = eng_word.lower()
            if not contains_valid_chars(lower_eng_word):
                eng.remove(eng_word)
    '''
    target_y = np.concatenate((np.zeros((fin.shape[0], )), np.ones((eng.shape[0], ))))
    word_array = np.concatenate((np.array(fin), np.array(eng)))
    features_X = get_features(word_array)
    # print(features_X, target_y)
    return features_X, target_y


def word_classification():
    X, y = get_features_and_labels()
    # print(y.shape)
    model = MultinomialNB()
    cv = KFold(n_splits=5, shuffle=True, random_state=0) 
    acc = cross_val_score(model, X, y, cv=cv)
    return acc


def main():
    print("Accuracy scores are:", word_classification())

if __name__ == "__main__":
    main()
