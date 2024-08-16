class OneHotEncoder:
    def __init__(self):
        self.categories = []

    def fit(self, data):
        self.categories = sorted(set(data.flatten()))

    def transform(self, data):
        encoded_data = []
        for value in data:
            encoded_row = [1 if value[0] == category else 0 for category in self.categories]
            encoded_data.append(encoded_row)
        return encoded_data

    def fit_transform(self, data):
        self.fit(data)
        return self.transform(data)


class OneHotDecoder:
    def __init__(self, categories):
        self.categories = categories

    def transform(self, encoded_data):
        decoded_data = [self.categories[row.index(1)] for row in encoded_data]
        return decoded_data


if __name__ == "__main__":
    from sklearn.preprocessing import OneHotEncoder as SklearnOneHotEncoder
    import numpy as np

    data = np.array(["Male", "Female", "Other"]).reshape(-1, 1)

    # My OneHotEncoder
    custom_encoder = OneHotEncoder()
    custom_encoded_data = custom_encoder.fit_transform(data)
    print(f"My Encoder:\n{custom_encoded_data}")

    # My OneHotDecoder
    custom_decoder = OneHotDecoder(custom_encoder.categories)
    custom_decoded_data = custom_decoder.transform(custom_encoded_data)
    print(f"\nMy Decoder:\n{custom_decoded_data}")

    # Scikit-learn OneHotEncoder
    sklearn_encoder = SklearnOneHotEncoder(sparse_output=False)
    sklearn_encoded_data = sklearn_encoder.fit_transform(data)
    print(f"\nScikit-Learn Encoder:\n{sklearn_encoded_data}")

    # Decoding using Scikit-learn encoder categories
    sklearn_decoded_data = [sklearn_encoder.categories_[0][row.argmax()] for row in sklearn_encoded_data]
    print(f"\nScikit-Learn Decoder:\n{sklearn_decoded_data}")
