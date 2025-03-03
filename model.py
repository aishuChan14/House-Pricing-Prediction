import pandas as pd
import numpy as np
import pickle
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score

# Define correct column names
column_names = [
    "CRIM", "ZN", "INDUS", "CHAS", "NOX", "RM", "AGE", "DIS", "RAD",
    "TAX", "PTRATIO", "B", "LSTAT", "MEDV"
]

# ✅ Load dataset properly (handling spaces)
df = pd.read_csv("datasets/boston.csv", names=column_names, header=None, sep="\s+")


# ✅ Convert all values to numeric (handling any errors)
df = df.apply(pd.to_numeric, errors='coerce')

# ✅ Drop any rows with missing values
df = df.dropna()

# ✅ Features (X) and Target (y)
X = df.drop(columns=['MEDV'])  # Independent variables
y = df['MEDV']  # House Price (dependent variable)

# ✅ Split dataset (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# ✅ Train model
model = LinearRegression()
model.fit(X_train, y_train)

# ✅ Predictions
y_pred = model.predict(X_test)

# ✅ Model evaluation
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Mean Absolute Error: {mae}")
print(f"R² Score: {r2}")

# ✅ Save the trained model
with open("boston_model.pkl", "wb") as file:
    pickle.dump(model, file)

print("✅ Model trained and saved as 'boston_model.pkl'")
