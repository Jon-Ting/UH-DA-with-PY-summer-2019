#!/usr/bin/env python3
 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
 
def explained_variance():
    df=pd.read_csv("src/data.tsv", sep="\t")
    variance = df.var(axis=0).values
    pca = PCA(10)
    pca.fit(df)
    return variance, pca.explained_variance_
 
def main():
    v, ev = explained_variance()
    print(sum(v), sum(ev))
    print("The variances are:", " ".join([f"{x:.3f}" for x in v]))
    print("The explained variances after PCA are:", " ".join([f"{x:.3f}" for x in ev]))
    plt.plot(np.arange(1,11), np.cumsum(ev));
    plt.show()
 
if __name__ == "__main__":
    main()
 
