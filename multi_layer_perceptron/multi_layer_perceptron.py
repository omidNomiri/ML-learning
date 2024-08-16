import numpy as np
from tqdm import tqdm

class MLP:
    def __init__(self, input_dim, output_dim, h1, h2, epochs, lr, act_func1, act_func2, act_func_output):
        self.input_dim = input_dim
        self.output_dim = output_dim
        self.h1 = h1
        self.h2 = h2
        self.epochs = epochs
        self.lr = lr

        self.act_func1 = act_func1
        self.act_func2 = act_func2
        self.act_func_output = act_func_output

        # Initialize weights and biases
        self.W1 = np.random.randn(self.input_dim, self.h1)
        self.W2 = np.random.randn(self.h1, self.h2)
        self.W3 = np.random.randn(self.h2, self.output_dim)

        self.B1 = np.random.randn(1, self.h1)
        self.B2 = np.random.randn(1, self.h2)
        self.B3 = np.random.randn(1, self.output_dim)

    def activation_function(self, func, x):
        if func == "sigmoid":
            return 1 / (1 + np.exp(-x))
        elif func == "softmax":
            exp_x = np.exp(x - np.max(x))
            return exp_x / np.sum(exp_x, axis=1, keepdims=True)
        else:
            raise ValueError(f"Unsupported activation function: {func}")

    def forward(self, x):
        x = x.reshape(1, -1)

        # Layer 1
        self.out1 = self.activation_function(self.act_func1, x @ self.W1 + self.B1)

        # Layer 2
        self.out2 = self.activation_function(self.act_func2, self.out1 @ self.W2 + self.B2)

        # Output Layer
        self.out3 = self.activation_function(self.act_func_output, self.out2 @ self.W3 + self.B3)

        return self.out3

    def backward(self, x, y):
        x = x.reshape(1, -1)

        # Calculate output layer error and gradients
        error_out = self.out3 - y
        grad_W3 = self.out2.T @ error_out
        grad_B3 = error_out

        # Calculate hidden layer 2 error and gradients
        error_h2 = (error_out @ self.W3.T) * self.out2 * (1 - self.out2)
        grad_W2 = self.out1.T @ error_h2
        grad_B2 = error_h2

        # Calculate hidden layer 1 error and gradients
        error_h1 = (error_h2 @ self.W2.T) * self.out1 * (1 - self.out1)
        grad_W1 = x.T @ error_h1
        grad_B1 = error_h1

        return grad_W1, grad_W2, grad_W3, grad_B1, grad_B2, grad_B3

    def update_weights(self, grad_W1, grad_W2, grad_W3, grad_B1, grad_B2, grad_B3):
        self.W1 -= self.lr * grad_W1
        self.B1 -= self.lr * grad_B1
        self.W2 -= self.lr * grad_W2
        self.B2 -= self.lr * grad_B2
        self.W3 -= self.lr * grad_W3
        self.B3 -= self.lr * grad_B3

    def fit(self, x_train, y_train):
        losses = []
        accuracies = []
        for _ in tqdm(range(self.epochs)):
            for x, y in zip(x_train, y_train):
                self.forward(x)
                grads = self.backward(x, y)
                self.update_weights(*grads)

            loss, accuracy = self.evaluate(x_train, y_train)
            losses.append(loss)
            accuracies.append(accuracy)

        return losses, accuracies

    def predict(self, x_test):
        return np.array([self.forward(x) for x in x_test]).reshape(-1, self.output_dim)

    def calculate_loss(self, y_pred, y_true, metric="mse"):
        if metric == "mse":
            return np.mean((y_pred - y_true) ** 2)
        elif metric == "mae":
            return np.mean(np.abs(y_pred - y_true))
        elif metric == "rmse":
            return np.sqrt(np.mean((y_pred - y_true) ** 2))
        else:
            raise ValueError("Unsupported metric")

    def calculate_accuracy(self, y_pred, y_true):
        return np.mean(np.argmax(y_pred, axis=1) == np.argmax(y_true, axis=1))

    def evaluate(self, x_test, y_test):
        y_pred = self.predict(x_test)
        loss = self.calculate_loss(y_pred, y_test)
        accuracy = self.calculate_accuracy(y_pred, y_test)
        return loss, accuracy

if __name__ == "__main__":
    from sklearn.datasets import load_digits
    from sklearn.model_selection import train_test_split
    from Onehot_method import OneHotEncoder

    encoder = OneHotEncoder()

    dataset = load_digits()
    X = dataset.data
    Y = dataset.target.reshape(-1, 1)

    Y = np.array(encoder.fit_transform(Y))

    x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.2)

    model = MLP(input_dim=x_train.shape[1], output_dim=y_train.shape[1], h1=128, h2=32,
                epochs=20, lr=.001, act_func1="sigmoid", act_func2="sigmoid", act_func_output="softmax")

    losses, accuracies = model.fit(x_train, y_train)

    loss_train, accuracy_train = model.evaluate(x_train, y_train)
    loss_test, accuracy_test = model.evaluate(x_test, y_test)

    print(f"loss_train: {loss_train:.4f}, accuracy_train: {accuracy_train:.4f}")
    print(f"loss_test: {loss_test:.4f}, accuracy_test: {accuracy_test:.4f}")
