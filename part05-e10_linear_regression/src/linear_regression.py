#!/usr/bin/env python3

import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

def fit_line(x, y):
    model = LinearRegression(fit_intercept=True)
    # model.fit(x[:, np.newaxis], y)
    model.fit(x.reshape(-1, 1), y)  # Equivalent, Single feature, -1 means infer from the rest
    # print("Coefficients: {0}".format.(model.coef_))
    m, c = model.coef_[0], model.intercept_
    return (m, c)
    
def main():
    np.random.seed(0)
    n=20   # Number of data points
    x = np.linspace(0, 10, n)
    y = 2 * x + 1 + 1 * np.random.randn(n)  # Standard deviation 1
    print(x, y)
    (slope, intercept) = fit_line(x, y)
    print("Slope: {0:.1f}".format(slope))
    print("Intercept: {0:.1f}".format(intercept))
    model = LinearRegression(fit_intercept=True)
    model.fit(x[:, np.newaxis], y)
    xfit = np.linspace(0, 10, 5 * n)
    yfit = model.predict(xfit[:, np.newaxis])
    plt.plot(xfit, yfit, color="black")
    plt.plot(x, y, "o")
    # plt.plot(np.vstack([x,x]), np.vstack([y, model.predict(x[:, np.newaxis])]), color="red")
    plt.show() 
    
    
if __name__ == "__main__":
    main()
