import pickle

with open("artifacts/preprocessor.pkl", "rb") as f:
    obj = pickle.load(f)

print("Preprocessor Loaded")