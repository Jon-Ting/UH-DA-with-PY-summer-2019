#!/usr/bin/env python3

import scipy
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
from sklearn.metrics import accuracy_score


def find_permutation(n_clusters, real_labels, labels):
    permutation=[]
    for i in range(n_clusters):
        idx = labels == i
        # Choose the most common label among data points in the cluster
        new_label=scipy.stats.mode(real_labels[idx])[0][0]
        permutation.append(new_label)
    return permutation

def plant_clustering():
    data = load_iris()
    num_cluster = 3
    model = KMeans(n_clusters=num_cluster, random_state=0)
    model.fit(data.data)
    print(model.cluster_centers_)
    
    plt.scatter(data.data[:, 0], data.data[:, 1], c=model.labels_)
    plt.show()
    
    permutation = find_permutation(num_cluster, data.target, model.labels_)
    print(permutation)
    new_labels = [ permutation[label] for label in model.labels_]
    acc = accuracy_score(data.target, new_labels)
    # acc = accuracy_score(data.target, [ permutation3[label] for label in model.labels_])
    return acc

def main():
    print(plant_clustering())

if __name__ == "__main__":
    main()
