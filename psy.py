import streamlit as st
import pandas as pd

def calculate_score(responses):
    return sum(responses)

def interpret_score(score, category):
    interpretation = {
        "Physical Health": ["Excellent physical health", "Good, but minor areas for improvement", "Moderate concerns—consider healthier habits", "Poor physical health—consult a professional"],
        "Mental & Emotional Well-being": ["Strong emotional resilience and mental well-being", "Generally stable, but occasional struggles", "Some concerns—consider stress management or therapy", "High risk—may need professional mental health support"],
        "Social & Behavioral Well-being": ["Healthy social life and balanced behavior", "Mostly stable, but could improve connections", "Some isolation or poor time management—work on balance", "Social withdrawal or poor habits—seek community engagement"],
        "Addiction & Dependency": ["No addiction concerns", "Occasional risky behaviors, but manageable", "Signs of dependency—consider moderating habits", "High addiction risk—seek professional guidance"],
        "Mental Health 'Red Alert' Screening": ["No immediate mental health risks", "Some emotional distress—monitor closely", "Moderate risk—consider seeking professional help", "Severe risk—immediate intervention needed"]
    }
    
    if score >= 17:
        return interpretation[category][0]
    elif score >= 13:
        return interpretation[category][1]
    elif score >= 9:
        return interpretation[category][2]
    else:
        return interpretation[category][3]

st.set_page_config(page_title="Wellness Screening", page_icon="🧘", layout="wide")
st.title("🌿 Rathinam's AI-Driven Comprehensive Wellness Screening for College Community 🌿")

categories = {
    "Physical Health": ["How often do you engage in physical exercise?", "How would you rate your sleep quality?", "Do you eat a balanced diet?", "Do you experience chronic pain?", "How often do you get medical checkups?"],
    "Mental & Emotional Well-being": ["How well do you handle stress?", "How often do you feel anxious?", "Do you have a strong sense of purpose?", "Do you feel joy in life?", "How would you describe your self-esteem?"],
    "Social & Behavioral Well-being": ["How satisfied are you with your social relationships?", "How often do you spend quality time with family?", "Do you have a balanced work-life schedule?", "Do you engage in hobbies?", "Do you manage your time efficiently?"],
    "Addiction & Dependency": ["Do you consume substances like alcohol or nicotine?", "Do you feel an urge to use substances?", "Does screen time interfere with responsibilities?", "Have you tried to cut down on a habit but struggled?", "Does your behavior negatively impact work or relationships?"],
    "Mental Health 'Red Alert' Screening": ["Have you lost interest in things you used to enjoy?", "Have you experienced thoughts of hopelessness?", "Do you experience excessive worry or panic attacks?", "Have you noticed major changes in sleep patterns?", "Have you had significant weight changes due to stress?"]
}

options = {"a) 4": 4, "b) 3": 3, "c) 2": 2, "d) 1": 1}
responses = {}

tabs = st.tabs(categories.keys())
for i, (category, questions) in enumerate(categories.items()):
    with tabs[i]:
        st.subheader(f"🎯 {category}")
        category_scores = []
        for question in questions:
            response = st.radio(question, list(options.keys()), index=None, key=f"{category}_{question}")
            if response:
                category_scores.append(options[response])
        responses[category] = calculate_score(category_scores) if category_scores else 0
        
        if st.button(f"Submit {category}", key=f"submit_{category}"):
            st.write(f"**{category} Score:** {responses[category]} | {interpret_score(responses[category], category)}")

if st.button("🚀 Submit Overall Assessment"):
    overall_score = sum(responses.values())
    st.subheader("📊 Overall Results")
    for category, score in responses.items():
        st.write(f"**{category}**: Score = {score} | {interpret_score(score, category)}")
    st.write(f"**Total Overall Score:** {overall_score}")
    
    st.write("**📌 Guidance:** If any domain scores below 9, consider seeking professional help.")
