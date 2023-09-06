import numpy as np
import pandas as pd
import random
random.seed(42)


def iniatialize(dim):
    b = random.random()
    w = np.random.rand(dim)
    return b, w


def predict(b, w, X):
    return b + np.matmul(X, w)


def cost(y, y_hat):
    y_resid = y - y_hat
    return np.sum(np.matmul(y_resid, y_resid.T))/len(y_resid)


def update(X, y, y_hat, b0, w0, learning_rate):
    # gradient of bias
    db = (np.sum(y_hat - y)*2)/len(y)
    # gradient of weights
    dw = (np.dot((y_hat - y), X)*2)/len(y)
    # update bias
    b1 = b0 - learning_rate * db
    # update of weights
    w1 = w0 - learning_rate * dw

    return b1, w1


def gradient_descent(X, y, alpha=0.01, num_iterations=100):

    # initialize bias and weights
    b, w = iniatialize(X.shape[1])

    iter_num = 0
    gd_iterations_df = pd.DataFrame(columns=['iteration', 'cost'])
    result_idx = 0

    for each_iter in range(num_iterations):
        # calculating y_hat
        y_hat = predict(b, w, X)
        # calculating cost
        cost = cost(y, y_hat)
        # saving the previous weights and bias
        prev_b = b
        prev_w = w
        # updating w & b values
        b, w = update(X, y, y_hat, prev_b, prev_w, alpha)

        if (iter_num % 10 == 0):
            gd_iterations_df.loc[result_idx] = [iter_num, cost]
            result_idx += 1
        iter_num += 1

    print(f"Final estimate of b and w : {b} , {w}")

    return gd_iterations_df, b, w


if __name__ == "__main__":

    from sklearn import datasets

    X, y = datasets.make_regression(
        n_samples=100, n_features=1, noise=20, random_state=42)

    gd_iterations_df, b, w = gradient_descent(
        X, y, alpha=0.02, num_iterations=200)

    print(gd_iterations_df[0:10])
