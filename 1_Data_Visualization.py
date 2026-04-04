# pages/1_Data_Visualization.py

import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Data Visualization", layout="wide")

st.title("📊 Student Academic Performance Dashboard")

# Load Dataset
df = pd.read_csv("Students_Data.csv")

# Create Total Marks Column
df["Total_Marks"] = (
    df["Maths Score"] +
    df["Reading Score"] +
    df["Writing Score"]
)

# Sidebar Filters
st.sidebar.header("Filters")

selected_gender = st.sidebar.multiselect(
    "Select Gender",
    options=df["Gender"].unique(),
    default=df["Gender"].unique()
)

selected_ethnicity = st.sidebar.multiselect(
    "Select Ethnicity",
    options=df["Ethnicity"].unique(),
    default=df["Ethnicity"].unique()
)

filtered_df = df[
    (df["Gender"].isin(selected_gender)) &
    (df["Ethnicity"].isin(selected_ethnicity))
]

# KPI Section
col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Students", len(filtered_df))
col2.metric("Average Marks", round(filtered_df["Total_Marks"].mean(), 2))
col3.metric("Top Score", filtered_df["Total_Marks"].max())
col4.metric(
    "Pass %",
    round((filtered_df[filtered_df["Total_Marks"] > 120].shape[0] / len(filtered_df)) * 100, 2)
)

st.divider()

# Chart 1
st.subheader("1️⃣ Gender vs Total Marks")

fig1 = px.bar(
    filtered_df,
    x="Gender",
    y="Total_Marks",
    color="Gender"
)

st.plotly_chart(fig1, use_container_width=True)

# Chart 2
st.subheader("2️⃣ Parental Education Impact")

fig2 = px.bar(
    filtered_df,
    x="Parental Education",
    y="Total_Marks",
    color="Parental Education"
)

st.plotly_chart(fig2, use_container_width=True)

# Chart 3
st.subheader("3️⃣ Lunch Type Effect")

fig3 = px.box(
    filtered_df,
    x="Lunch Type",
    y="Total_Marks",
    color="Lunch Type"
)

st.plotly_chart(fig3, use_container_width=True)

# Chart 4
st.subheader("4️⃣ Test Preparation Course Impact")

fig4 = px.bar(
    filtered_df,
    x="Test Preparation Course",
    y="Total_Marks",
    color="Test Preparation Course"
)

st.plotly_chart(fig4, use_container_width=True)

# Chart 5
st.subheader("5️⃣ Subject Score Comparison")

fig5 = px.box(
    filtered_df,
    y=["Maths Score", "Reading Score", "Writing Score"]
)

st.plotly_chart(fig5, use_container_width=True)

# Chart 6
st.subheader("6️⃣ Reading vs Writing Relationship")

fig6 = px.scatter(
    filtered_df,
    x="Reading Score",
    y="Writing Score",
    color="Gender"
)

st.plotly_chart(fig6, use_container_width=True)
