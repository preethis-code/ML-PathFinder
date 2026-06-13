import streamlit as st

st.title("ML PathFinder")
st.markdown(
    "Get a personalized Machine Learning learning roadmap based on your interests and skill level."
)

interest = st.selectbox(
    "Select Interest",
    ["Foundation", "ML", "AI"]
)

level = st.selectbox(
    "Select Level",
    ["Beginner", "Intermediate", "Advanced"]
)
name = st.text_input("Enter Your Name")

if st.button("Get Roadmap"):
    st.subheader(f"Hello {name}! ")
    st.subheader("Your Personalized Learning Roadmap")

    topics = {
    ("Foundation", "Beginner"): ["Python Basics", "Statistics", "Linear Algebra"],

    ("ML", "Beginner"): ["Machine Learning Basics", "Data Cleaning"],
    ("ML", "Intermediate"): ["Regression", "Classification"],
    ("ML", "Advanced"): ["Feature Engineering", "Model Optimization"],

    ("AI", "Beginner"): ["Intro to AI", "Prompt Engineering"],
    ("AI", "Intermediate"): ["NLP", "Computer Vision"],
    ("AI", "Advanced"): ["Deep Learning", "Transformers", "MLOps"]
}
    

    result = topics.get((interest, level), ["No topics found"])

    st.subheader("Recommended Topics")

    for i, topic in enumerate(result, start=1):
        st.write(f"{i}. {topic}")
    
    

    st.success("Learning Roadmap Generated Successfully!")