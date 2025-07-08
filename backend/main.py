from fastapi import FastAPI, Request
import openai
import os
from fastapi.middleware.cors import CORSMiddleware

# Load your OpenAI API key from environment
openai.api_key = os.getenv("OPENAI_API_KEY")

app = FastAPI()

# Allow CORS for frontend development
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "BugMentor backend is running!"}

@app.post("/explain-bug")
async def explain_bug(request: Request):
    try:
        data = await request.json()
        code = data.get("code")

        if not code:
            return {"error": "No code provided."}

        prompt = (
            "You are a senior software engineer helping a junior developer. "
            "Explain the bug in this code in simple terms. Describe why it's a bug, "
            "what the impact is, and how to fix it.\n\nCode:\n" + code
        )

        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are an expert code reviewer."},
                {"role": "user", "content": prompt}
            ]
        )

        explanation = response['choices'][0]['message']['content']
        return {"explanation": explanation}

    except Exception as e:
        return {"error": str(e)}