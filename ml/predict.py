import joblib

def load_model():
    return joblib.load("ml/model.pkl")

def predict(model, features):
    return model.predict_proba([list(features.values())])[0][1]