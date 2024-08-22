import numpy as np


class Perceptron:
    def __init__(self, lr_w, lr_b, epochs):
        self.learning_rate_w = lr_w
        self.learning_rate_b = lr_b
        self.epochs = epochs

    def fit(self, X_train, Y_train):
        n_samples, n_features = X_train.shape
        self.w = np.random.randn(n_features) * 0.01
        self.b = 0.0

        for epoch in range(self.epochs):
            for i in range(n_samples):
                x = X_train[i]
                y = Y_train[i]

                y_pred = self.predict(x.reshape(1, -1))
                error = y - y_pred

                self.w += self.learning_rate_w * error * x
                self.b += self.learning_rate_b * error

            print(f"Epoch {epoch + 1}")

    def predict(self, X_test):
        return np.dot(X_test, self.w) + self.b

    def calculate_loss(self, X_test, Y_test, metric="mse"):
        y_pred = self.predict(X_test)
        if metric == "mse":
            loss = np.mean((y_pred - Y_test) ** 2)
        elif metric == "mae":
            loss = np.mean(np.abs(y_pred - Y_test))
        else:
            raise Exception("Not supported metric")
        return loss

    def calculate_accuracy(self, X_test, Y_test, metric="sigmoid"):
        y_pred = self.predict(X_test)
        if metric == "sigmoid":
            y_pred = np.where(y_pred > 0.5, 1, 0)
        else:
            raise Exception("Not supported accuracy metric")
        return np.mean(y_pred == Y_test)

    def evaluate(self, X_test, Y_test, metric="mae"):
        y_pred = self.predict(X_test)
        error = Y_test - y_pred
        if metric == "mae":
            loss = np.mean(np.abs(error))
        elif metric == "mse":
            loss = np.mean(error ** 2)
        elif metric == "rmse":
            loss = np.sqrt(np.mean(error ** 2))
        else:
            raise Exception("Not supported metric")
        return loss
