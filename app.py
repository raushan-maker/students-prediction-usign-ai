import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier

# Page config
st.set_page_config(page_title="Student Predictor", page_icon="🎓", layout="centered")

# Custom CSS (for modern look)
st.markdown("""
    <style>
    .main {
        background-color: #0e1117;
        color: white;
    }
    .stButton>button {
        background: linear-gradient(90deg, #00c6ff, #0072ff);
        color: white;
        border-radius: 10px;
        height: 3em;
        width: 100%;
        font-size: 18px;
    }
    .result-pass {
        background-color: #1f7a1f;
        padding: 15px;
        border-radius: 10px;
        text-align: center;
        font-size: 20px;
    }
    .result-fail {
        background-color: #7a1f1f;
        padding: 15px;
        border-radius: 10px;
        text-align: center;
        font-size: 20px;
    }
    </style>
""", unsafe_allow_html=True)


# Title
st.title("🎓 Student Performance Predictor")

# Cache model
@st.cache_resource
def train_model():
    data = pd.DataFrame({
        'Study_Hours': [1,2,3,4,5,6,7,8],
        'Attendance': [50,55,60,65,70,75,80,90],
        'Previous_Marks': [40,45,50,55,60,65,70,80],
        'Result': ['Fail','Fail','Fail','Pass','Pass','Pass','Pass','Pass']
    })

    X = data[['Study_Hours', 'Attendance', 'Previous_Marks']]
    y = data['Result']

    model = DecisionTreeClassifier()
    model.fit(X, y)
    return model, data

model, data = train_model()

# Inputs
study_hours = st.slider("📚 Study Hours", 0, 12, 4)
attendance = st.slider("📊 Attendance %", 0, 100, 75)
previous_marks = st.slider("📝 Previous Marks", 0, 100, 60)

# Predict
if st.button("🚀 Predict Result"):

    result = model.predict([[study_hours, attendance, previous_marks]])

    # Result
    if result[0] == "Pass":
        st.success("✅ Student will PASS 🎉")
    else:
        st.error("❌ Student will FAIL ⚠️")

    # 📊 GRAPH SECTION
    st.subheader("📊 Performance Analysis")

    fig = plt.figure()
    values = [study_hours, attendance, previous_marks]
    labels = ["Study Hours", "Attendance", "Previous Marks"]

    plt.bar(labels, values)
    plt.xlabel("Factors")
    plt.ylabel("Values")
    plt.title("Student Input Analysis")

    st.pyplot(fig)

    # 🧠 AI SUGGESTIONS
    st.subheader("🧠 AI Suggestions")

    if study_hours < 4:
        st.warning("👉 Increase study hours to at least 5+ hours.")

    if attendance < 75:
        st.warning("👉 Improve attendance above 75%.")

    if previous_marks < 60:
        st.warning("👉 Focus on basics to improve marks.")

    if study_hours >= 5 and attendance >= 75 and previous_marks >= 60:
        st.success("🎯 Great! You are on track for good performance.")