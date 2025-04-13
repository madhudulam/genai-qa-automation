import streamlit as st
from app.test_generator import generate_test_case
import os
import subprocess

st.set_page_config(page_title="GenAI QA Test Generator", layout="centered")
st.title("🧪 Gen AI QA Automation Tool")

prompt = st.text_area("Enter your test scenario:", value="Test the login form with correct and incorrect credentials.")

if st.button("Generate Test Case"):
    with st.spinner("Generating test case..."):
        code = generate_test_case(prompt)
        st.code(code, language='python')

        os.makedirs("tests/ui", exist_ok=True)
        with open("tests/ui/test_generated.py", "w") as f:
            f.write(code)
        st.success("✅ Test case saved to tests/ui/test_generated.py")

if st.button("Run Test with Pytest"):
    with st.spinner("Running tests..."):
        result = subprocess.run(["pytest", "tests/ui/test_generated.py"], capture_output=True, text=True)
        st.text(result.stdout)
        if result.stderr:
            st.text(result.stderr)