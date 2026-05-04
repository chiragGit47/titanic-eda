import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import pickle

df = pd.read_csv("Salary Data.csv")

# Clean
df["Department"] = pd.factorize(df['Department'])[0]
df["Gender"] = pd.factorize(df['Gender'])[0]
df["Education"] = pd.factorize(df['Education'])[0]
df.dropna(inplace=True)

# Train
X = df[["Age","Gender","Education","Department","Experience"]]
y = df["Salary"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

st.title("💰 Salary Predictor")
st.write("Enter your details to get a salary prediction")

age = st.slider("Age", 20, 60, 30)
experience = st.slider("Years of Experience", 0, 40, 5)
gender = st.radio("Gender", [0, 1], captions=["Female", "Male"])

education = st.select_slider("Education Level", [0, 1, 2], format_func=lambda x: ["High School", "Bachelor", "Master"][x])
department = st.select_slider("Department", [0, 1, 2], format_func=lambda x: ["Engineering", "Finance", "Marketing"][x])

if st.button("Predict Salary"):
    input_data = [[age, gender, education, department, experience]]
    prediction = model.predict(input_data)[0]
    
    st.success(f"🎯 Predicted Salary: ₹{prediction:,.0f}")
    st.write(f"**Age:** {age} | **Experience:** {experience} years | **Department:** {['Engineering', 'Finance', 'Marketing'][department]}")