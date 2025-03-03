# House-Pricing-Prediction
# House Price Prediction using Boston Housing Dataset

## 📌 Project Overview

This is a Flask-based web application that predicts house prices using the **Boston Housing Dataset**. The project employs **Machine Learning (ML)** to estimate property values based on various factors such as crime rate, number of rooms, and property tax rate.

## 📊 Dataset: Boston Housing Dataset

The Boston Housing Dataset contains information on various housing attributes and median home prices in different neighborhoods of Boston. The dataset includes features like:

- **CRIM**: Per capita crime rate by town
- **ZN**: Proportion of residential land zoned for large lots
- **INDUS**: Proportion of non-retail business acres per town
- **CHAS**: Charles River dummy variable (1 if tract bounds river, 0 otherwise)
- **RM**: Average number of rooms per dwelling
- **AGE**: Proportion of owner-occupied units built before 1940
- **TAX**: Property tax rate per \$10,000
- **MEDV**: Median value of owner-occupied homes (target variable)

## 🛠️ Installation & Setup

Follow these steps to set up and run the project locally:

### **1️⃣ Clone the Repository**

```sh
git clone https://github.com/aishuChan14/House-Pricing-Prediction.git
cd House-Pricing-Prediction
```

### **2️⃣ Create a Virtual Environment (Optional but Recommended)**

```sh
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate    # On Windows
```

### **3️⃣ Install Dependencies**

```sh
pip install -r requirements.txt
```

### **4️⃣ Run the Flask Application**

```sh
python app.py
```

### **5️⃣ Access the Web App**

Open your browser and go to:

```
http://127.0.0.1:5000/
```

## 🚀 Usage

- **Step 1**: Enter values for features such as crime rate, number of rooms, tax rate, etc.
- **Step 2**: Click the "Predict" button.
- **Step 3**: View the predicted house price.

## 💻 Technologies Used

- **Python** (Flask, Pandas, NumPy, Scikit-Learn)
- **Machine Learning Model** (Trained using the Boston Housing Dataset)
- **HTML, CSS, JavaScript** (Frontend for User Interface)

## 📂 Project Structure

```
House-Pricing-Prediction/
│-- app.py          # Flask web application
│-- model.py        # Machine learning model training script
│-- boston_model.pkl  # Trained ML model (saved as pickle file)
│-- templates/      # HTML templates
│-- static/         # CSS and JavaScript files
│-- datasets/       # Dataset used for training
│-- requirements.txt  # Required dependencies
│-- README.md       # Project Documentation
```

## 👤 Author

- **Aishwarya Choudhari**
- GitHub: [aishuChan14](https://github.com/aishuChan14)

##

