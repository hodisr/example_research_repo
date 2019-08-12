from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


def train_model(dataset, model, test_size=0.33, seed=7):
    features_train, features_test, targets_train, targets_test = train_test_split(
        dataset.features, dataset.targets, test_size=test_size, random_state=seed
    )
    model.fit(features_train, targets_train)
    # make predictions for test data
    y_pred = model.predict(features_test)
    predictions = [round(value) for value in y_pred]
    # evaluate predictions
    accuracy = accuracy_score(targets_test, predictions)
    print("Accuracy: %.2f%%" % (accuracy * 100.0))
    return accuracy


