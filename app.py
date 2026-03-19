mport streamlit as st
import numpy as np
import pickle
import plotly.graph_objects as go

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="AI Student Analyzer", layout="centered")

# ---------------- LOAD MODEL ----------------
model = pickle.load(open("model.pkl", "rb"))

# ---------------- UI HEADER ----------------
st.title("🎓 AI Student Performance Analyzer")
st.markdown("### 📊 Smart Dashboard with AI Suggestions")

# ---------------- INPUT SECTION ----------------
st.subheader("📥 Enter Student Details")

math = st.number_input("📘 Math Marks", 0, 100)
physics = st.number_input("⚡ Physics Marks", 0, 100)
chemistry = st.number_input("🧪 Chemistry Marks", 0, 100)

study_hours = st.slider("⏳ Study Hours per day", 0, 12)

# ---------------- PREDICTION ----------------
if st.button("🔍 Analyze Performance"):

    data = np.array([[math, physics, chemistry, study_hours]])
    prediction = model.predict(data)[0]

    avg_marks = (math + physics + chemistry) / 3

    # Fake probability (you can improve later)
    pass_prob = min(100, int(avg_marks + study_hours * 5))

    # ---------------- RESULT ----------------
    st.subheader("🎯 Result")

    if prediction == 1:
        st.success("✅ PASS")
    else:
        st.error("❌ FAIL")

    st.info(f"📈 Pass Probability: {pass_prob}%")

    # ---------------- GRAPH (BAR CHART) ----------------
    st.subheader("📊 Subject-wise Performance")

    fig = go.Figure(
        data=[
            go.Bar(
                x=["Math", "Physics", "Chemistry"],
                y=[math, physics, chemistry]
            )
        ]
    )

    st.plotly_chart(fig)

    # ---------------- RADAR CHART ----------------
    st.subheader("📌 Performance Radar")

    radar = go.Figure()

    radar.add_trace(go.Scatterpolar(
        r=[math, physics, chemistry],
        theta=["Math", "Physics", "Chemistry"],
        fill='toself'
    ))

    radar.update_layout(polar=dict(radialaxis=dict(visible=True, range=[0, 100])))

    st.plotly_chart(radar)

    # ---------------- AI SUGGESTIONS ----------------
    st.subheader("🧠 AI Suggestions")

    if math < 40:
        st.warning("📘 Improve Mathematics – practice daily problems")
    if physics < 40:
        st.warning("⚡ Focus on Physics numericals")
    if chemistry < 40:
        st.warning("🧪 Revise Chemistry concepts")

    if study_hours < 2:
        st.warning("⏳ Increase study time to at least 2–3 hours/day")

    if avg_marks > 70:
        st.success("🔥 Excellent performance! Keep it up")

    # ---------------- STUDY PLAN ----------------
    st.subheader("📅 Suggested Study Plan")

    st.write("""
    Day 1: Math practice  
    Day 2: Physics numericals  
    Day 3: Chemistry revision  
    Day 4: Mock test  
    Repeat 🔁
    """)
