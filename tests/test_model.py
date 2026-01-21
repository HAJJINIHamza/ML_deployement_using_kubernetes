import pickle

import pytest


@pytest.mark.model  # Mark it a model test
def test_model():
    # Import model
    try:
        with open("models/vanilla_model.pkl", "rb") as f_model:
            model = pickle.load(f_model)
    except FileNotFoundError:
        raise FileNotFoundError("Model file not found")
    # test1
    data_1 = [[5.1, 3.5, 1.4, 0.2]]
    assert model.predict(data_1) == [0]
    # test2
    data_2 = [[6.7, 3.1, 4.7, 1.5]]
    assert model.predict(data_2) == [1]
