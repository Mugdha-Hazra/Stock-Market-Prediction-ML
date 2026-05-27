import streamlit as st
import pandas as pd
import joblib

# =========================================
# LOAD MODEL
# =========================================

model = joblib.load("models/final_stock_model.pkl")

# =========================================
# PAGE TITLE
# =========================================

st.title("Stock Market Prediction System")

st.write(
    "MBA Major Project using Machine Learning and Python"
)

# =========================================
# USER INPUTS
# =========================================

st.header("Enter Stock Information")

open_price = st.number_input("Open Price")

high_price = st.number_input("High Price")

low_price = st.number_input("Low Price")

close_price = st.number_input("Close Price")

volume = st.number_input("Volume")

ma10 = st.number_input("10 Day Moving Average")

ma50 = st.number_input("50 Day Moving Average")

daily_return = st.number_input("Daily Return")

volatility = st.number_input("Volatility")

gdp = st.number_input("GDP Growth")

inflation = st.number_input("Inflation")

unemployment = st.number_input("Unemployment")

# =========================================
# PREDICT BUTTON
# =========================================

if st.button("Predict Stock Movement"):

    sample_data = pd.DataFrame({

        'Open': [open_price],
        'High': [high_price],
        'Low': [low_price],
        'Close': [close_price],
        'Volume': [volume],

        'MA10': [ma10],
        'MA50': [ma50],

        'Daily_Return': [daily_return],
        'Volatility': [volatility],

        'GDP_Growth': [gdp],
        'Inflation': [inflation],
        'Unemployment': [unemployment]
    })

    prediction = model.predict(sample_data)

    if prediction[0] == 1:

        st.success(
            "Prediction: Stock Price Likely To Rise"
        )

    else:

        st.error(
            "Prediction: Stock Price Likely To Fall"
        )