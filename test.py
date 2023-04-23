import os
import pickle

import numpy as np

from data_loader.subject import Subject
from main import save_object


def load_object(fname):
    try:
        with open(fname + ".pickle", "rb") as f:
            return pickle.load(f)
    except Exception as ex:
        print("Error during unpickling object (Possibly unsupported):", ex)


data = load_object('./output/training_sets/Set_6/training_set')
print(f"Subjects: {len(data['x'])}, Targets: {len(data['y'])}")
print(f"Subject: {len(data['x'][0])}")
print(data['x'][0])
