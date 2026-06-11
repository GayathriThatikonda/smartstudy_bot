from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

def generate_quiz(topic, n=5):

    prompt = f"""
Generate {n} multiple-choice questions (MCQs) about {topic}.

Provide:
1. Question
A) Option
B) Option
C) Option
D) Option

At the end provide an answer key.
"""

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        return response.text

    except Exception as e:
        return f"[ERROR]: {e}"