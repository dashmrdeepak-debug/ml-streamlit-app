import streamlit as st
import joblib
import pandas as pd

# Load model
model = joblib.load(r"C:\Users\dashm\Downloads\model (2).pkl")

st.title("🛒 Purchase Prediction App")

# Inputs
age = st.number_input("Age", 10, 60)
time_on_site = st.number_input("Time on Site", 0, 300)
pages_viewed = st.number_input("Pages Viewed", 1, 25)
previous_purchases = st.number_input("Previous Purchases", 0, 20)
cart_items = st.number_input("Cart Items", 0, 15)

discount_seen = st.selectbox("Discount Seen", [0, 1])
ad_clicked = st.selectbox("Ad Clicked", [0, 1])
returning_user = st.selectbox("Returning User", [0, 1])

avg_session_time = st.number_input("Avg Session Time", 0, 100)
bounce_rate = st.number_input("Bounce Rate", 0.0, 1.0)

gender_e = st.selectbox("Gender (Encoded)", [0, 1])
device_deskt = st.selectbox("Device Desktop", [0, 1])
device_tabl = st.selectbox("Device Tablet", [0, 1])

# DataFrame
input_data = pd.DataFrame({
    'age': [age],
    'time_on_site': [time_on_site],
    'pages_viewed': [pages_viewed],
    'previous_purchases': [previous_purchases],
    'cart_items': [cart_items],
    'discount_seen': [discount_seen],
    'ad_clicked': [ad_clicked],
    'returning_user': [returning_user],
    'avg_session_time': [avg_session_time],
    'bounce_rate': [bounce_rate],
    'gender_e': [gender_e],
    'device_deskt': [device_deskt],
    'device_tabl': [device_tabl]
})