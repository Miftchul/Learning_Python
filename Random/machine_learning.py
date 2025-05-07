# Machine Learning Example: Linear Regression (Simplified)
# This program demonstrates a simple linear regression model using scikit-learn.
# It fits a line to the data points to predict target values based on input features.

import numpy as np
from sklearn.linear_model import LinearRegression

def main():
    # Example data
    X = np.array([[1], [2], [3], [4], [5]])  # Features
    y = np.array([1.5, 3.7, 2.8, 4.5, 5.1])  # Target values

    # Create and train the model
    model = LinearRegression()
    model.fit(X, y)

    # Make predictions
    predictions = model.predict(X)
    print("Predictions:", predictions)

if __name__ == "__main__":
    main()