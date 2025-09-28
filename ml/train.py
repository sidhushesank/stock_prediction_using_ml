import joblib
from sklearn.linear_model import LinearRegression
from preprocess import fetch_stock_data, preprocess_data

def train_model(ticker='AAPL'):
    """
    Fetch stock data, preprocess it, train Linear Regression model,
    and save the trained model to disk as 'model.pkl'.
    """
    print(f"Fetching data for {ticker}...")
    df = fetch_stock_data(ticker)

    print("Preprocessing data...")
    X, y = preprocess_data(df)

    print("Training Linear Regression model...")
    model = LinearRegression()
    model.fit(X, y)

    print("Saving the model as ml/model.pkl")
    joblib.dump(model, 'ml/model.pkl')
    print("Training complete.")

if __name__ == "__main__":
    train_model()
