
import streamlit as st

st.title("Agentic AI Feature Selector")

st.markdown("""
This tool helps you select the best AI feature to build next based on:
- **User Feedback** (Importance)
- **Business Alignment**
- **Tech Effort** (Lower is better)
""")

features = ["Chatbot API", "Model Accuracy", "Explainability Dashboard", "Multilingual Support"]

user_feedback = {}
business_goals = {}
tech_effort = {}

st.subheader("Step 1: Rate Each Feature")
for feature in features:
    st.markdown(f"**{feature}**")
    user_feedback[feature] = st.slider(f"User Feedback - {feature}", 0.0, 10.0, 5.0, key=f"uf_{feature}")
    business_goals[feature] = st.slider(f"Business Alignment - {feature}", 0.0, 10.0, 5.0, key=f"bg_{feature}")
    tech_effort[feature] = st.slider(f"Tech Effort - {feature}", 1.0, 10.0, 5.0, key=f"te_{feature}")
    st.markdown("---")

if st.button("🔍 Calculate Best Feature"):
    scores = {}
    for feature in features:
        importance = user_feedback[feature]
        alignment = business_goals[feature]
        effort = tech_effort[feature]
        score = (importance * 0.5 + alignment * 0.5) / effort
        scores[feature] = score

    best_feature = max(scores, key=scores.get)
    st.success(f"✅ Best Feature to Build: **{best_feature}** (Score: {scores[best_feature]:.2f})")

    st.subheader("📊 All Feature Scores")
    for f, s in sorted(scores.items(), key=lambda x: x[1], reverse=True):
        st.write(f"**{f}**: {s:.2f}")
