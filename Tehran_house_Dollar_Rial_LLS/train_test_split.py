import numpy as np

def train_test_split(x, y, test_size=.2):
    indices = np.arange(len(x))
    np.random.shuffle(indices)

    split_index = int((1 - test_size) * len(x))

    x_train, x_test = x[indices[:split_index]], x[indices[split_index:]]
    y_train, y_test = y[indices[:split_index]], y[indices[split_index:]]

    return x_train, y_train ,x_test, y_test

if __name__ == "__main__":
    X = np.random.rand(1000, 3)
    Y = np.random.rand(1000, 1)

    x_train, y_train, x_test, y_test = train_test_split(X, Y, test_size=0.2)

    print(f'X_train shape: {x_train.shape}')
    print(f'y_train shape: {y_train.shape}')
    print(f'X_test shape: {x_test.shape}')
    print(f'y_test shape: {y_test.shape}')
