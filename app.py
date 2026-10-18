
import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Student Course Recommendation System",
    page_icon="🎓"
)

st.title("🎓 Student Course Recommendation System")
st.write("Get personalized course recommendations based on your profile.")

data = {
    "Course": [
        "Python Programming", "Java Programming",
        "Web Development", "Data Science",
        "Machine Learning", "Artificial Intelligence",
        "Cyber Security", "Cloud Computing",
        "Database Management", "Data Structures",
        "C Programming", "UI UX Design"
    ],
    "Category": [
        "Programming", "Programming", "Web", "Data",
        "AI", "AI", "Security", "Cloud",
        "Database", "Programming", "Programming", "Design"
    ],
    "Level": [
        "Beginner", "Intermediate", "Beginner",
        "Intermediate", "Advanced", "Advanced",
        "Intermediate", "Intermediate", "Beginner",
        "Intermediate", "Beginner", "Beginner"
    ]
}

courses = pd.DataFrame(data)

career_courses = {
    "Software Developer": [
        "Python Programming", "Java Programming",
        "Data Structures", "Web Development"
    ],
    "Data Scientist": [
        "Python Programming", "Data Science",
        "Machine Learning", "Database Management"
    ],
    "AI Engineer": [
        "Python Programming", "Artificial Intelligence",
        "Machine Learning", "Data Science"
    ],
    "Cyber Security": [
        "Cyber Security", "Python Programming",
        "Data Structures"
    ],
    "Web Developer": [
        "Web Development", "Java Programming",
        "Database Management"
    ],
    "Cloud Engineer": [
        "Cloud Computing", "Python Programming",
        "Database Management"
    ],
    "UI/UX Designer": [
        "UI UX Design", "Web Development"
    ]
}

course_info = {
    "Python Programming": "Learn Python programming from basics.",
    "Java Programming": "Learn Java and Object-Oriented Programming.",
    "Web Development": "Learn HTML, CSS, JavaScript and web development.",
    "Data Science": "Learn data analysis, statistics and data science.",
    "Machine Learning": "Learn machine learning and predictive models.",
    "Artificial Intelligence": "Learn AI concepts and intelligent systems.",
    "Cyber Security": "Learn network security basics.",
    "Cloud Computing": "Learn cloud services and technologies.",
    "Database Management": "Learn SQL and database management.",
    "Data Structures": "Learn data structures and algorithms.",
    "C Programming": "Learn C programming fundamentals.",
    "UI UX Design": "Learn UI and UX design."
}

with st.form("student_form"):
    name = st.text_input("👤 Student Name")
    branch = st.selectbox(
        "🎓 Branch", ["CSE", "ECE", "EEE", "MECH", "CIVIL"]
    )
    interest = st.selectbox(
        "💡 Area of Interest",
        ["Programming", "Web", "Data", "AI",
         "Security", "Cloud", "Database", "Design"]
    )
    level = st.selectbox(
        "📊 Skill Level",
        ["Beginner", "Intermediate", "Advanced"]
    )
    goal = st.selectbox(
        "🎯 Career Goal", list(career_courses.keys())
    )
    submitted = st.form_submit_button("Get Recommendations")

if submitted:
    results = []

    for _, course in courses.iterrows():
        score = 0

        if interest == course["Category"]:
            score += 50
        if level == course["Level"]:
            score += 20
        if course["Course"] in career_courses[goal]:
            score += 30

        if score >= 50:
            results.append({
                "Course": course["Course"],
                "Category": course["Category"],
                "Level": course["Level"],
                "Match %": score,
                "Description": course_info[course["Course"]]
            })

    result_df = pd.DataFrame(results)

    if not result_df.empty:
        result_df = result_df.sort_values(
            "Match %", ascending=False
        ).head(5)
        st.success(f"Recommendations for {name or 'Student'}")
        st.dataframe(result_df, use_container_width=True)
    else:
        st.info("No matching courses found.")
      
