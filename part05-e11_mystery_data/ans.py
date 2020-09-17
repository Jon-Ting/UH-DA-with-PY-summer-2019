#!/usr/bin/env python3
 
import pandas as pd
from sklearn.linear_model import LinearRegression
 
def mystery_data():
    df = pd.read_csv("src/mystery_data.tsv", sep="\t")
    X = df.loc[:, "X1":"X5"]
    y = df.Y
    reg = LinearRegression(fit_intercept=False)
    reg.fit(X, y)
 
    return reg.coef_
 
def main():
    coefficients = mystery_data()
    for i, c in enumerate(coefficients):
        print(f"Coefficient of X{i+1} is {c:.4f}")
    
if __name__ == "__main__":
    main()
 
