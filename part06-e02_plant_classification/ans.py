#!/usr/bin/env python3
 
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn import naive_bayes
from sklearn import metrics
 
def plant_classification():
    data = load_iris()
    X = data.data
    y = data.target
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0,
                                                        train_size=0.8)
    model = naive_bayes.GaussianNB()
 
    model.fit(X_train, y_train)
    y_predicted = model.predict(X_test)
    return metrics.accuracy_score(y_test, y_predicted)
 
def main():
    print(f"Accuracy is {plant_classification()}")
 
if __name__ == "__main__":
    main()
 
