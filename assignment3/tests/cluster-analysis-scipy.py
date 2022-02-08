import numpy as np
import scipy.cluster.hierarchy
import scipy.spatial.distance
from matplotlib import pyplot as plt

x1: np.ndarray = np.array([0, 0])
x2: np.ndarray = np.array([1, 1])
x3: np.ndarray = np.array([2, 1])
x4: np.ndarray = np.array([0, 2])

X = np.array([x1, x2, x3, x4])

Z = scipy.cluster.hierarchy.linkage(scipy.spatial.distance.pdist(X, metric="euclidean"), method="ward")

fig, ax = plt.subplots(dpi=100)
dn = scipy.cluster.hierarchy.dendrogram(Z, labels=["x1", "x2", "x3", "x4"], ax=ax)
ax.set_ylabel("Euclidean distance")
plt.show()
