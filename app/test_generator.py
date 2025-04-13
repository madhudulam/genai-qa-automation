import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
model = os.getenv("OPENAI_MODEL", "gpt-3.5-turbo")

def generate_test_case(prompt_text):
    response = openai.ChatCompletion.create(
        model=model,
        messages=[
            {"role": "system", "content": "You are a QA automation engineer who writes Selenium tests in Python using pytest."},
            {"role": "user", "content": prompt_text}
        ],
        temperature=0.2
    )
    return response.choices[0].message['content']