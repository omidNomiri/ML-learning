def calculate_precision(y_true, y_pred):
    true_positives = sum((true == 1 and pred == 1)
                         for true, pred in zip(y_true, y_pred))
    false_positives = sum((true == 0 and pred == 1)
                          for true, pred in zip(y_true, y_pred))

    if true_positives + false_positives == 0:
        return 0

    return true_positives / (true_positives + false_positives)


def calculate_recall(y_true, y_pred):
    true_positives = sum((true == 1 and pred == 1)
                         for true, pred in zip(y_true, y_pred))
    false_negatives = sum((true == 1 and pred == 0)
                          for true, pred in zip(y_true, y_pred))

    if true_positives + false_negatives == 0:
        return 0

    return true_positives / (true_positives + false_negatives)


if __name__ == "__main__":
    from sklearn.metrics import precision_score, recall_score

    y_true = [1, 0, 1, 1, 0, 1, 0]
    y_pred = [1, 1, 1, 0, 0, 1, 1]

    precision_scratch = calculate_precision(y_true, y_pred)
    recall_scratch = calculate_recall(y_true, y_pred)

    precision_sklearn = precision_score(y_true, y_pred)
    recall_sklearn = recall_score(y_true, y_pred)

    print(f"Precision (from scratch): {precision_scratch:.4f}")
    print(f"Recall (from scratch): {recall_scratch:.4f}")
    print("\n")
    print(f"Precision (scikit-learn): {precision_sklearn:.4f}")
    print(f"Recall (scikit-learn): {recall_sklearn:.4f}")
