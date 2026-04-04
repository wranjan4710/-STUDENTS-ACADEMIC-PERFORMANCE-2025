# 🎓 Student Academic Performance Dashboard

A Streamlit-based dashboard project for analyzing student academic performance using data visualization and basic machine learning.

This project helps users understand how different factors such as gender, parental education, lunch type, ethnicity, and test preparation courses affect student scores.

## Features

- Login Authentication Page
- Student Performance Dashboard
- Data Visualization using Plotly
- Subject-wise Marks Analysis
- Gender and Ethnicity Filters
- Performance Prediction Model
- Interactive Charts and Graphs
- Student Score Forecasting

## Technologies Used

- Python
- Streamlit
- Pandas
- Plotly
- Scikit-learn

## Project Structure

Student_Performance_App/
│
├── app.py
├── model.py
├── Students_Data.csv
├── pages/
│   ├── 0_Login.py
│   ├── 1_Data_Visualization.py
│   └── 2_Model_Forecasting.py

## Installation

1. Clone the repository -
git clone https://github.com/your-username/student-performance-dashboard.git

2. Open project folder - 
cd student-performance-dashboard

3. Install required libraries -
pip install -r requirements.txt

4. Run Streamlit app - 
streamlit run app.py

## Requirements

streamlit
pandas
plotly
scikit-learn

## Pages

### Login Page
Allows users to login with username and password.

### Data Visualization Page
Shows charts related to:
- Gender vs Total Marks
- Parental Education Impact
- Lunch Type Effect
- Test Preparation Impact
- Reading vs Writing Relationship

### Model Forecasting Page
Predicts student total marks based on Maths, Reading, and Writing scores.

## Future Improvements

- Add Database Connectivity
- Add Real User Authentication
- Deploy on Streamlit Cloud
- Add Download Report Option
- Add Machine Learning Accuracy Metrics
- Add Dark Mode UI

## Author

Dablu Ranjan  
AI & ML Student 
