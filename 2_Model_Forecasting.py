# pages/2_Model_Forecasting.py

import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression

st.set_page_config(page_title="Model Forecasting", layout="wide")

st.title("📈 Student Performance Prediction Dashboard")

# Load Dataset
df = pd.read_csv("Students_Data.csv")

# Create Total Marks Column
df["Total_Marks"] = (
    df["Maths Score"] +
    df["Reading Score"] +
    df["Writing Score"]
)

# Features and Target
X = df[["Maths Score", "Reading Score", "Writing Score"]]
y = df["Total_Marks"]

# Train Model
model = LinearRegression()
model.fit(X, y)

# User Input
st.sidebar.header("Enter Student Scores")

math_score = st.sidebar.slider("Maths Score", 0, 100, 50)
reading_score = st.sidebar.slider("Reading Score", 0, 100, 50)
writing_score = st.sidebar.slider("Writing Score", 0, 100, 50)

# Prediction
prediction = model.predict([[math_score, reading_score, writing_score]])

st.subheader("Predicted Total Marks")
st.success(f"{prediction[0]:.2f}")

# Performance Category
if prediction[0] >= 240:
    st.success("Excellent Performance")
elif prediction[0] >= 180:
    st.info("Good Performance")
elif prediction[0] >= 120:
    st.warning("Average Performance")
else:
    st.error("Needs Improvement")
