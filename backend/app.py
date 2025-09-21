import os
from fastapi import FastAPI
from pydantic import BaseModel
from openai import OpenAI
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware
import google.generativeai as genai

# Load OpenAI key from environment
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# ---- Helpers ----
def call_llm(prompt: str) -> str:
    """Call OpenAI LLM with a given prompt."""
    response = client.chat.completions.create(
        model="gpt-4o-mini",   # switch to gpt-4o or gpt-3.5-turbo if needed
        messages=[
            {"role": "system", "content": "You are a helpful legal assistant that simplifies legal text for non-lawyers."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content.strip()

def call_gemini(prompt: str) -> str:
    """Call Gemini LLM with a given prompt."""
    model = genai.GenerativeModel("gemini-1.5-flash")  # or "gemini-1.5-pro"
    response = model.generate_content(prompt)
    return response.text.strip() if response and response.text else "No response"

# ---- Agents ----
def summarization_agent(text: str) -> str:
    prompt = f"Simplify the following legal clause into plain English:\n\n{text}"
    return call_gemini(prompt)

def risk_agent(text: str) -> str:
    prompt = f"Identify potential risks, liabilities, or obligations in this clause:\n\n{text}"
    return call_gemini(prompt)

def rewrite_agent(text: str) -> str:
    prompt = f"Rewrite this clause in a safer, clearer way while keeping the meaning:\n\n{text}"
    return call_gemini(prompt)

def critic_agent(summary: str, risks: str, rewrite: str) -> str:
    prompt = f"""
    Review the following outputs:
    - Summary: {summary}
    - Risks: {risks}
    - Rewrite: {rewrite}

    Check for accuracy, consistency, and clarity. 
    Suggest improvements if needed.
    """
    return call_gemini(prompt)

# ---- FastAPI Setup ----
app = FastAPI()

origins = [
    "https://demystifyinglegaldocuments.onrender.com/ ",
    "chrome-extension://*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # For dev, allow all. 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Selection(BaseModel):
    text: str

class RequestBody(BaseModel):
    selection: Selection

# @app.post("/api/v1/simplify")
# async def simplify(body: RequestBody):
#     input_text = body.selection.text.strip()
#     if not input_text:
#         return {"summary": "No input text", "risks": "-", "rewrite": "-"}

#     try:
#         # Agent 1 - Summarize
#         summary = client.chat.completions.create(
#             model="gpt-4o-mini",
#             messages=[{"role": "user", "content": f"Summarize this legal text: {input_text}"}],
#             max_tokens=200
#         ).choices[0].message.content.strip()

#         # Agent 2 - Extract risks
#         risks = client.chat.completions.create(
#             model="gpt-4o-mini",
#             messages=[{"role": "user", "content": f"List potential risks or obligations in this legal text: {input_text}"}],
#             max_tokens=200
#         ).choices[0].message.content.strip()

#         # Agent 3 - Rewrite in plain English
#         rewrite = client.chat.completions.create(
#             model="gpt-4o-mini",
#             messages=[{"role": "user", "content": f"Rewrite this in plain, simple English for a non-lawyer: {input_text}"}],
#             max_tokens=300
#         ).choices[0].message.content.strip()

#         return {
#             "summary": summary,
#             "risks": risks,
#             "rewrite": rewrite
#         }

#     except Exception as e:
#         return {"summary": "Error", "risks": str(e), "rewrite": "-"}

# Run with: uvicorn app:app --reload

@app.post("/api/v1/simplify")
async def simplify(body: RequestBody):
    input_text = body.selection.text.strip()
    if not input_text:
        return {"summary": "No input text", "risks": "-", "rewrite": "-"}

    try:
        summary = call_gemini(f"Summarize this legal text: {input_text}")
        risks   = call_gemini(f"List potential risks or obligations in this legal text: {input_text}")
        rewrite = call_gemini(f"Rewrite this in plain, simple English for a non-lawyer: {input_text}")

        return {"summary": summary, "risks": risks, "rewrite": rewrite}

    except Exception as e:
        return {"summary": "Error", "risks": str(e), "rewrite": "-"}


@app.get("/health")
def health():
  return {"status": "ok"}