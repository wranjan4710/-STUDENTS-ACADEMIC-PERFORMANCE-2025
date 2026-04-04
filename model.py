# model.py

import streamlit as st

st.set_page_config(page_title="Model Forecasting", layout="wide")

st.title("📈 Student Performance Forecasting")

st.write("Enter subject marks to predict total marks")

math_score = st.slider("Maths Score", 0, 100, 50)
reading_score = st.slider("Reading Score", 0, 100, 50)
writing_score = st.slider("Writing Score", 0, 100, 50)

predicted_total = math_score + reading_score + writing_score

st.subheader("Prediction Result")
st.success(f"Predicted Total Marks: {predicted_total}")

if predicted_total >= 240:
    st.success("Excellent Performance")
elif predicted_total >= 180:
    st.info("Good Performance")
elif predicted_total >= 120:
    st.warning("Average Performance")
else:
    st.error("Needs Improvement")
