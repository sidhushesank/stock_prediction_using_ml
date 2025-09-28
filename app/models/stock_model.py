import joblib

# Load the trained model at startup to reuse
model = joblib.load('ml/model.pkl')

def predict_next_close(close_price):
    """
    Given today's close price (float), predict tomorrow's price using the loaded model.
    """
    prediction = model.predict([[close_price]])
    return prediction[0]
