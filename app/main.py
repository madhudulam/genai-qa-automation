import streamlit as st
from app.test_generator import generate_test_case

st.set_page_config(page_title="GenAI QA Test Generator", layout="centered")
st.title("🧪 Gen AI QA Automation Tool")

prompt = st.text_area("Enter your test scenario:", value="Test the login form with correct and incorrect credentials.")

if st.button("Generate Test Case"):
    with st.spinner("Generating test case..."):
        code = generate_test_case(prompt)
        st.code(code, language='python')