import numpy as np

X: np.ndarray = np.array([[0, 0], [1, 1], [2, 1], [0, 2]])


def distace_matrix(X: np.ndarray) -> np.ndarray:
    """
    Compute the Euclidean distance matrix between each pair of points
    :param X: A matrix of shape (n, 2) where each row is a point in 2D
    :return: A matrix of shape (n, n) where the (i, j)th entry is the distance between the i-th and j-th point
    """
    n = X.shape[0]
    dists = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            dists[i, j] = np.linalg.norm(X[i] - X[j])
    return dists


print("Euclidean distance matrix:")
print(distace_matrix(X))

# test for distance matrix
print("Euclidean distance matrix(test):")
x: np.ndarray = np.array([2, 11, 5, 1, 7])
print(distace_matrix(x))


def Manhattan_distance(X: np.ndarray) -> np.ndarray:
    """
    Compute the Manhattan distance matrix between each pair of points
    :param X: A matrix of shape (n, 2) where each row is a point in 2D
    :return: A matrix of shape (n, n) where the (i, j)th entry is the Manhattan distance between the i-th and j-th point
    """
    n = X.shape[0]
    dists = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            dists[i, j] = np.sum(np.abs(X[i] - X[j]))
    return dists


print("Manhattan distace matrix:")
print(Manhattan_distance(X))


class Ward_clustering:
    def __init__(self, X: np.ndarray, dist_func: callable):
        """
        Initialize a new clustering model
        :param X: A matrix of shape (n, 2) where each row is a point in 2D
        :param dist_func: A function that computes the distance between two points
        """
        self.X = X
        self.dist_func = dist_func

    def fit(self, k: int) -> np.ndarray:
        """
        Compute the distance matrix and cluster the data into k clusters
        :param k: The number of clusters
        :return: A list of length n where the i-th element is the cluster label of the i-th point
        """
        n = self.X.shape[0]
        dists = self.dist_func(self.X)
        dists[np.arange(n), np.arange(n)] = np.inf
        clusters = np.argmin(dists, axis=1)
        return clusters


x1: np.ndarray = np.array([0, 0])
x2: np.ndarray = np.array([1, 1])
x3: np.ndarray = np.array([2, 1])
x4: np.ndarray = np.array([0, 2])
