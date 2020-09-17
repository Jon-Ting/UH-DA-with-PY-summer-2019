#!/usr/bin/env python3

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA


def explained_variance():
    X = pd.read_csv("src/data.tsv", sep="\t")
    pca = PCA(n_components=10)
    pca.fit(X)
    variance = list(X.var())
    # variance = X.var(axis=0).values
    # Z = pca.transform(X)
    # print("Principal axes:", pca.components_)
    # print("Explained variances:", pca.explained_variance_)
    # print("Mean:", pca.mean_)
    return variance, pca.explained_variance_


def main():
    v, ev = explained_variance()
    print(v, ev)
    print(sum(v), sum(ev))
    
    # print("The variances are:", " ".join([f"{x:.3f}" for x in v]))
    print("The variances are: ", end="")
    for i in v:
        print("{0:.3f} ".format(i), end="")
    print("\nThe explained variances after PCA are: ", end="")
    for i in ev:
        print("{0:.3f} ".format(i), end="")
    plt.plot(np.arange(1, 11), np.cumsum(ev))
    plt.show()


if __name__ == "__main__":
    main()
