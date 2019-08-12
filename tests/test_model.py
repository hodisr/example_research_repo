from iguazio_example.PATHS import sample_features_path, sample_targets_path, sample_model_path
from iguazio_example.experiment import train_model
from iguazio_example.model_handling import load_model
from iguazio_example.processors.processors import DummyProcessor

MIN_SCORE_THRESHOLD = 0.75


def test_model():
    data = DummyProcessor.load_from_files(features_path=sample_features_path, targets_path=sample_targets_path)
    model = load_model(sample_model_path)
    score = train_model(data, model)
    return score > MIN_SCORE_THRESHOLD


if __name__ == '__main__':
    test_model()

