import numpy as np


class NeruralNetwork:
    def __init__(self, ):
        # Number of input, output and hidden nodes initialization
        self.inputsize = 3
        self.outputsize = 1
        self.hiddensize = 3

        # Randomly initializing the weights
        self.W1 = np.random.rand(self.inputsize, self.hiddensize)
        self.W2 = np.random.rand(self.hiddensize, self.outputsize)

        self.error_list = []
        self.limit = 0.5

        self.true_positives = 0
        self.true_negatives = 0

        self.false_positives = 0
        self.false_negatives = 0

    # Function to do Forward Propogation for pass the input and get the error
    def forwardPropogation(self, X):
        self.z = np.matmul(X, self.W1)
        self.z2 = self.sigmoid(self.z)
        self.z3 = np.matmul(self.z2, self.W2)
        output = self.sigmoid(self.z3)
        return output

    # Function to do Backward Propogation for update the weights
    def backwardPropogation(self, X, y, output):
        self.output_error = y - output
        self.output_delta = self.output_error * self.sigmoidPrime(output)
        self.z2_error = np.matmul(self.output_delta * np.matrix.transpose(self.W2))
        self.z2_delta = self.z2_error * self.sigmoidPrime(self.z2)
        self.W1 += np.matmul(np.matrix.transpose(X), self.z2_delta)
        self.W2 += np.matmul(np.matrix.transpose(self.z2), self.output_delta)

    def train(self, X, y, epochs):
        for _ in range(epochs):
            output = self.forwardPropogation(X)
            self.backwardPropogation(X, y, output)
            self.error_list.append(np.abs(self.output_error).mean())

    def predict(self, X):
        return self.forwardPropogation(X).item()
