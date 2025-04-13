# 🧠 Gen AI QA Automation Framework

This project uses Generative AI to automatically create and execute test cases (Selenium + Python) from natural language prompts.

## Features
- 🔥 Natural language → Selenium test case generator
- 🧪 Pytest-based test execution
- 📊 HTML test reports
- ☁️ OpenAI or LLM model support
- 🔁 CI/CD with GitHub Actions

## Getting Started

```bash
git clone https://github.com/yourname/genai-qa-automation.git
cd genai-qa-automation
pip install -r requirements.txt
```

Set your environment variables:

```bash
touch .env
# Add OPENAI_API_KEY=your_key_here
```

## Run a sample test generation
```bash
streamlit run app/main.py
```

## Folder Structure
- `app/`: Core logic
- `tests/`: Generated test cases
- `prompts/`: Custom input examples
- `templates/`: Reusable AI prompt templates

---

## Future Work
- CI/CD test runs
- Allure reports
- UI crawler for element discovery