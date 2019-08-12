import pickle


def save_model(model, dest_path):
    pickle.dump(model, open(dest_path, "wb"))


def load_model(model_path):
    return pickle.load(open(model_path, 'rb'))

