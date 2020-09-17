#!/usr/bin/env python3

import scipy
import pandas as pd
import numpy as np
from sklearn.cluster import AgglomerativeClustering
from sklearn.metrics import accuracy_score
from sklearn.metrics import pairwise_distances

from matplotlib import pyplot as plt

import seaborn as sns
sns.set(color_codes=True)
import scipy.spatial as sp
import scipy.cluster.hierarchy as hc

toint_dict = {"A": "0", "C": "1", "G": "2", "T": "3"}


def find_permutation(n_clusters, real_labels, labels):
    permutation=[]
    for i in range(n_clusters):
        idx = labels == i
        # Choose the most common label among data points in the cluster
        new_label=scipy.stats.mode(real_labels[idx])[0][0]
        permutation.append(new_label)
    return permutation


def toint(x):
    # d=dict(zip("ACGT", range(4)))
    # return d[x]
    for key in toint_dict.keys():
        x = x.replace(key, toint_dict[key])
    return int(x)


def get_features_and_labels(filename):
    df = pd.read_csv(filename, sep="\t")
    features = np.array([None] * 8)
    for site in df["X"]:
        site_list = []
        for nuc in site:
            int_nuc = toint(nuc)
            site_list.append(int_nuc)
        features = np.vstack((features, np.array(site_list)))
    features = np.delete(features, 0, axis=0)
    print(features.shape)
    labels = df["y"]
    # labels = df.y
    # features = np.array(df.X.map(list).values.tolist())
    # toint2 = np.vectorize(toint)
    # features = toint2(features)
    return features, labels


def plot(distances, method='average', affinity='euclidean'):
    mylinkage = hc.linkage(sp.distance.squareform(distances), method=method)
    g=sns.clustermap(distances, row_linkage=mylinkage, col_linkage=mylinkage )
    g.fig.suptitle(f"Hierarchical clustering using {method} linkage and {affinity} affinity")
    plt.show()


def cluster_euclidean(filename):
    num_cluster = 2
    features, labels = get_features_and_labels(filename)
    clustering = AgglomerativeClustering(n_clusters=num_cluster, affinity="euclidean", linkage="average")
    clustering.fit(features)
    permutation = find_permutation(num_cluster, labels, clustering.labels_)
    # print(permutation)
    new_labels = [ permutation[label] for label in clustering.labels_]
    acc = accuracy_score(labels, new_labels)
    return acc


def cluster_hamming(filename):
    num_cluster = 2
    features, labels = get_features_and_labels(filename)
    clustering = AgglomerativeClustering(n_clusters=num_cluster, affinity="precomputed", linkage="average")
    distance_mat = pairwise_distances(features, metric="hamming")
    clustering.fit_predict(distance_mat)
    idx = clustering.labels_ == -1
    permutation = find_permutation(num_cluster, labels, clustering.labels_)
    # print(permutation)
    new_labels = [permutation[label] for label in clustering.labels_[~idx]]
    # new_labels = 1 - clustering.fit_predict(distance_mat)
    acc = accuracy_score(labels[~idx], new_labels)
    plot(distance_mat, "average", "hamming")
    return acc


def main():
    print(toint("A"))
    # return
    # print(get_features_and_labels("src/data.seq"))
    print("Accuracy score with Euclidean affinity is", cluster_euclidean("src/data.seq"))
    print("Accuracy score with Hamming affinity is", cluster_hamming("src/data.seq"))

if __name__ == "__main__":
    main()
