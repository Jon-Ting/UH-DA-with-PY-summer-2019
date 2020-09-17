#!/usr/bin/env python3

import pandas as pd
import numpy as np
from sklearn import linear_model


def coefficient_of_determination():
    df = pd.read_csv("src/mystery_data.tsv", sep="\t")
    model = linear_model.LinearRegression(fit_intercept=True)
    model.fit(df[["X1", "X2", "X3", "X4", "X5"]], df["Y"])
    # print(df[["X1", "X2", "X3", "X4", "X5"]])
    pred = model.predict(df[["X1", "X2", "X3", "X4", "X5"]])
    # pred = np.vstack(model.predict(df["X1"]), model.predict(df["X2"]), model.predict(df["X3"]), model.predict(df["X4"]), model.predict(df["X5"])).T
    print(df[["X1", "X2", "X3", "X4", "X5"]].shape)
    # print(np.vstack(model.predict(df["X1"]), model.predict(df["X2"])).shape)
    print(pred.shape, df["Y"].shape)
    coefficients = []
    coefficients.append(model.score(df[["X1", "X2", "X3", "X4", "X5"]], df["Y"]))
    for i in range(1, 6):
        var = "X{0}".format(i)
        model.fit(df[var][:, np.newaxis], df["Y"])
        pred = model.predict(df[var][:, np.newaxis])
        coefficients.append(model.score(df[var][:, np.newaxis], df["Y"]))
    print(coefficients)
    return coefficients
    

def main():
    coefficients = coefficient_of_determination()
    print("R2 score with feature(s) of X: {0}".format(coefficients[0]))
    for i in range(1, 6):
        print("R2 score with feature(s) of X{0}: {1}".format(i, coefficients[i]))


if __name__ == "__main__":
    main()
