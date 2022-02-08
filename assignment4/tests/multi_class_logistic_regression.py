import numpy as np
from sklearn.linear_model import SGDClassifier

x1 = np.array([1, -1])


def multi_class_logistic_regression_p(x: np.ndarray) -> np.ndarray:
    """
    Multi-class Logistic Regression
    """
    w1 = np.array([0, 1])
    w2 = np.array([1, 0])
    w3 = np.array([-1, -1])
    W = np.array([w1, w2, w3])

    b1, b2, b3 = 1, -1, 0
    B = np.array([b1, b2, b3])

    y = np.zeros(B.shape[0], dtype=np.float64)
    for i in range(B.shape[0]):
        y[i] = np.exp((W[i, :].T) @ x + B[i])

    return y / np.sum(y)


print(multi_class_logistic_regression_p(x1))

model = SGDClassifier(loss="log", max_iter=1000)
