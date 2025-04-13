import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_test_case(prompt_text):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a QA automation engineer who writes Selenium tests in Python."},
            {"role": "user", "content": prompt_text}
        ],
        temperature=0.2
    )
    return response.choices[0].message['content']