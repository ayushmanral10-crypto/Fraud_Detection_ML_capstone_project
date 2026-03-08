import streamlit as st
import pandas as pd
import joblib

model = joblib.load("fraud_model.pkl")

st.title("💳 Fraud Detection System")

st.subheader("Enter Transaction Details")

amount = st.number_input("Transaction Amount", min_value=0.0)

payment_method = st.selectbox(
    "Payment Method",
    ["CARD", "UPI", "WALLET", "NETBANKING"]
)

merchant_category = st.selectbox(
    "Merchant Category",
    ["Fashion", "Electronics", "Travel", "Utilities", "Food"]
)

is_international = st.selectbox("International Transaction?", [0,1])

location_change_flag = st.selectbox("Location Change Flag", [0, 1])

ip_risk = st.slider("IP Risk Score", 0.0, 1.0, 0.5)

device_trust = st.slider("Device Trust Score", 0.0, 1.0, 0.8)

txn_count_24h = st.number_input("Transactions Last 24h", min_value=0)

avg_amount_24h = st.number_input("Avg Amount Last 24h", min_value=0.0)

merchant_diversity = st.number_input("Merchant Diversity Last 7d", min_value=0)

device_change = st.selectbox("Device Changed?", [0,1])

authentication_method = st.selectbox(
    "Authentication Method",
    ["OTP", "PIN", "NONE"]
)

otp_success = st.slider("OTP Success Rate", 0.0, 1.0, 0.8)

past_fraud = st.number_input("Past Fraud Count", min_value=0)

past_disputes = st.number_input("Past Disputes", min_value=0)

merchant_fraud_rate = st.slider("Merchant Historical Fraud Rate", 0.0, 1.0, 0.1)

hour_of_day = st.slider("Hour of Day", 0, 23, 12)

day_of_week = st.selectbox(
    "Day of Week",
    ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
)

is_weekend = st.selectbox("Is Weekend?", [0,1])

# Create DataFrame
input_data = pd.DataFrame({
    "amount": [amount],
    "location_change_flag": [location_change_flag],
    "payment_method": [payment_method],
    "merchant_category": [merchant_category],
    "is_international": [is_international],
    "ip_address_risk_score": [ip_risk],
    "device_trust_score": [device_trust],
    "txn_count_last_24h": [txn_count_24h],
    "avg_amount_last_24h": [avg_amount_24h],
    "merchant_diversity_last_7d": [merchant_diversity],
    "device_change_flag": [device_change],
    "authentication_method": [authentication_method],
    "otp_success_rate_customer": [otp_success],
    "past_fraud_count_customer": [past_fraud],
    "past_disputes_customer": [past_disputes],
    "merchant_historical_fraud_rate": [merchant_fraud_rate],
    "hour_of_day": [hour_of_day],
    "day_of_week": [day_of_week],
    "is_weekend": [is_weekend]
})

if st.button("🔍 Predict Transaction"):

    prediction = model.predict(input_data)[0]
    probability = model.predict_proba(input_data)[0][1]

    st.write(f"Fraud Probability: {round(probability * 100,2)}%")

    if prediction == 1:
        st.error("Fraud Transaction Detected")
    else:
        st.success("Legitimate Transaction")