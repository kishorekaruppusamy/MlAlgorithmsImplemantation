import numpy as np

class LinearRegression():

    def __init__(self, lr = 0.001, n_iters = 1000):
        self.lr = lr
        self.n_iters = n_iters
        self.weights = None
        self.bais = None

    def fit(self, X, y):
        n_samples, n_features = X.shape
        print(n_samples, n_features)
        self.weights = np.zeros(n_features)
        self.bais = 0

        for _ in range(self.n_iters):

            # y = mX + c
            y_pred = np.dot(X, self.weights) + self.bais

            # dw = 1/n Σ x(y^ - y)
            dw = (1/n_samples) * np.dot(X.T, (y_pred - y))

            #db = 1/n Σ (y^ - y)
            db = (1/n_samples) * np.sum(y_pred - y)

            self.weights = self.weights - self.lr * dw

            self.bais = self.bais = self.lr * db
        
        print(self.weights)
        print(self.bais)
        
    def predict(self, X):

        # y = mX + c

        y_pred = np.dot(X, self.weights) + self.bais

        return y_pred


