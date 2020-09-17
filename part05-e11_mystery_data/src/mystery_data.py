#!/usr/bin/env python3

import pandas as pd
from sklearn.linear_model import LinearRegression

def mystery_data():
    df = pd.read_csv("src/mystery_data.tsv", sep="\t")
    model = LinearRegression(fit_intercept=False)
    X = df[["X1", "X2", "X3", "X4", "X5"]]
    # print(X.transpose())
    model.fit(X, df["Y"])
    return model.coef_

def main():
    coefficients = mystery_data()
    # Print the coefficients here
    for i in range(5):
        print("Coefficient of X{0} is {1}".format(i + 1, coefficients[i]))

if __name__ == "__main__":
    main()
