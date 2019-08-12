import pandas as pd


def load_parquet(file_path: str) -> pd.DataFrame:
    return pd.read_parquet(file_path)


class DummyProcessor:
    def __init__(self, features, targets):
        self.features = features
        self.targets = targets

    @classmethod
    def load_from_files(cls, features_path: str, targets_path: str):
        return cls(
            features=load_parquet(features_path),
            targets=load_parquet(targets_path)
        )

