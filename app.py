from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load the trained model
model = pickle.load(open('boston_model.pkl', 'rb'))

@app.route("/", methods=["GET", "POST"])
def predict():
    price = None  # Reset price on page reload
    feature_names = ["CRIM", "ZN", "INDUS", "CHAS", "NOX", "RM", "AGE", "DIS", "RAD", "TAX", "PTRATIO", "B", "LSTAT"]
    
    if request.method == "POST":
        try:
            # Get user input and convert to float
            features = [float(request.form[f]) for f in feature_names]
            # Reshape input for model prediction
            features = np.array(features).reshape(1, -1)
            # Predict house price
            price = model.predict(features)[0]
            price = round(price, 2)  # Round the output
        except ValueError:
            price = "Invalid input. Please enter numeric values."

    return render_template("index.html", price=price)

if __name__ == "__main__":
    app.run(debug=True)
