import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import streamlit as st

# Load your dataset
data = pd.read_csv("C:\ML app\streamlit\weather_station2 - weather_station2 (1).csv")

# Drop the "Loud Cover" column
data = data.drop("Loud Cover", axis=1)

# Separate features and target variable
X = data.iloc[:, [0]]  # Features
y = data.iloc[:, [-1]]  # Target variable

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)

# Train a simple Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions
y_pred_train = model.predict(X_train)
y_pred_test = model.predict(X_test)

# Streamlit app
st.title("Temperature Prediction")

# Sidebar for user input
apparent_temperature_input = st.number_input("Enter Apparent Temperature", min_value=-20.0, max_value=40.0, step=0.1)

# Button to trigger prediction
if st.button("Predict Temperature"):
    temperature_prediction = model.predict([[apparent_temperature_input]])
    st.write(f"Predicted Temperature: {temperature_prediction[0][0]}")
