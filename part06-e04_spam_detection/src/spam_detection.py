#!/usr/bin/env python3
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score
# from sklearn.pipeline import make_pipeline
import pandas as pd
import numpy as np
import gzip


def spam_detection(random_state=0, fraction=1.0):
    vec = CountVectorizer()
    # model = make_pipeline(CountVectorizer(), MultinomialNB())
    
    ham_list, spam_list = [], []
    with gzip.open("src/ham.txt.gz", mode="r") as ham:
        lines = ham.readlines()
        lines_to_take = int(fraction * len(lines))
        # print("Line: {0}, Lines to take: {1}".format(len(lines), lines_to_take))
        for i, line in enumerate(lines):
            if i == lines_to_take:
                break
            ham_list.append(line)
    with gzip.open("src/spam.txt.gz", mode="r") as spam:
        lines = spam.readlines()
        lines_to_take = int(fraction * len(lines))
        for i, line in enumerate(lines):
            if i == lines_to_take:
                break
            spam_list.append(line)
    # print(ham_list, spam_list)
    # ham = ham[:int(fraction*len(ham))]
    # print(len(ham_list), len(spam_list))
    ham_label, spam_label = np.zeros((len(ham_list), 1)), np.ones((len(spam_list), 1))
    data_label = np.concatenate((ham_label, spam_label), axis=0).T[0]
    # print(data_label)
    # print(ham_label.shape, spam_label.shape, data_label.shape)
    features = vec.fit_transform(ham_list + spam_list)
    # print(features, features[0, :])
    
    X_train, X_test, y_train, y_test = train_test_split(features, data_label, train_size=0.75, test_size=0.25, random_state=random_state)
    # print(X_train.shape, X_test.shape, y_train.shape, y_test.shape) 
    model = MultinomialNB()
    model.fit(X_train, y_train.reshape(y_train.shape[0], ))
    y_fitted = model.predict(X_test)
    accuracy = model.score(X_test, y_test)
    total = len(y_test)
    # print(y_test, y_fitted)
    misclassified = (y_test != y_fitted).sum()
    return accuracy, total, misclassified
    # return None, None, None


def main():
    accuracy, total, misclassified = spam_detection(random_state=0, fraction=0.1)
    print("Accuracy score:", accuracy)
    print(f"{misclassified} messages miclassified out of {total}")

if __name__ == "__main__":
    main()
