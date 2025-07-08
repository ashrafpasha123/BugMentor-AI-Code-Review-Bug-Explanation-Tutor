# 🐞 BugMentor

AI-powered tool that explains bugs in code in natural language.

## Features
- Paste code and get explanations
- Shows what's wrong, why, and how to fix it
- Ideal for learners, juniors, and interviews

## Tech Stack
- FastAPI, OpenAI GPT-4, React (planned)

## Setup
1. Add your OpenAI API key in `.env`
2. Run the backend using Uvicorn

```bash
pip install fastapi uvicorn openai python-dotenv
uvicorn backend.main:app --reload
```