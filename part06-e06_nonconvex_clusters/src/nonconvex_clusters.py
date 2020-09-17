#!/usr/bin/env python3

import scipy
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import DBSCAN
from sklearn.metrics import accuracy_score


def find_permutation(n_clusters, real_labels, labels):
    permutation=[]
    for i in range(n_clusters):
        idx = labels == i
        # Choose the most common label among data points in the cluster
        new_label=scipy.stats.mode(real_labels[idx])[0][0]
        permutation.append(new_label)
    return permutation


def nonconvex_clusters():
    data = pd.read_csv("src/data.tsv", sep="\t")
    X, y = data[["X1", "X2"]], data["y"]
    print(X, y)
    eps_list = np.arange(0.05, 0.2, 0.05)
    data_dict = {"eps": [], "Score": [], "Clusters": [], "Outliers": []}
    for i, eps_val in enumerate(eps_list):
        model = DBSCAN(eps=eps_val)
        # print(model)
        model.fit(X)
        num_cluster = len(np.unique(model.labels_)) - (1 if -1 in model.labels_ else 0)
        # num_cluster = max(model.labels_) + 1
        idx = model.labels_ == -1
        num_noise = list(model.labels_).count(-1)
        # num_noise = np.sum(idx)
        permutation = find_permutation(num_cluster, y, model.labels_)
        # print(permutation)
        new_labels = [ permutation[label] for label in model.labels_[~idx]]
        if num_cluster != len(np.unique(y)):
            acc = np.nan
        else:
            acc = accuracy_score(y[~idx], new_labels)
        data_dict["eps"].append(float(eps_val))
        # data_dict["Score"].append(float(round(acc, 1)))
        data_dict["Score"].append(float(acc))
        data_dict["Clusters"].append(float(num_cluster))
        data_dict["Outliers"].append(float(num_noise))
    # plt.scatter(X["X1"], X["X2"], c=model.labels_)
    # plt.show()
    df = pd.DataFrame(data_dict)
    return df


def main():
    print(nonconvex_clusters())

if __name__ == "__main__":
    main()
