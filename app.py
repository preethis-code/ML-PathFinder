import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

st.title("ML PathFinder ⭐")

st.markdown(
    "Get a personalized Machine Learning learning roadmap based on your interests and skill level."
)

name = st.text_input("Enter Your Name")

interest = st.selectbox(
    "Select Interest",
    ["Foundation", "ML", "AI"]
)

level = st.selectbox(
    "Select Level",
    ["Beginner", "Intermediate", "Advanced"]
)

if st.button("Get Roadmap"):

    st.subheader(f"Hello {name}!")
    st.subheader("Your Personalized Learning Roadmap 💡")

    data = [
        {"topic": "Python Basics", "profile": "Foundation Beginner"},
        {"topic": "Statistics", "profile": "Foundation Beginner"},
        {"topic": "Linear Algebra", "profile": "Foundation Beginner"},

        {"topic": "Data Cleaning", "profile": "ML Beginner"},
        {"topic": "Machine Learning Basics", "profile": "ML Beginner"},

        {"topic": "Regression", "profile": "ML Intermediate"},
        {"topic": "Classification", "profile": "ML Intermediate"},

        {"topic": "Feature Engineering", "profile": "ML Advanced"},
        {"topic": "Model Optimization", "profile": "ML Advanced"},

        {"topic": "Intro to AI", "profile": "AI Beginner"},
        {"topic": "Prompt Engineering", "profile": "AI Beginner"},

        {"topic": "NLP", "profile": "AI Intermediate"},
        {"topic": "Computer Vision", "profile": "AI Intermediate"},

        {"topic": "Deep Learning", "profile": "AI Advanced"},
        {"topic": "Transformers", "profile": "AI Advanced"},
        {"topic": "MLOps", "profile": "AI Advanced"},
    ]

    user_profile = f"{interest} {level}"

    profiles = [item["profile"] for item in data]

    vectorizer = TfidfVectorizer()

    profile_vectors = vectorizer.fit_transform(profiles)

    user_vector = vectorizer.transform([user_profile])

    similarity_scores = cosine_similarity(
        user_vector,
        profile_vectors
    )[0]

    scored_topics = list(zip(similarity_scores, data))

    scored_topics.sort(reverse=True, key=lambda x: x[0])

    recommendations = []

    for score, item in scored_topics[:5]:
        recommendations.append(item["topic"])

    for i, topic in enumerate(recommendations, start=1):
        st.write(f"{i}. {topic}")

    st.success("Learning Roadmap Generated Successfully!")