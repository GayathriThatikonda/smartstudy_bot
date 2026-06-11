from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

def summarise_notes():
    notes = input("Paste notes: ")

    prompt = f"""
Summarize the following notes in simple bullet points:

{notes}
"""

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        print("\nSummary:\n")
        print(response.text)

    except Exception as e:
        print("[ERROR]:", e)
        print("Something went wrong.\n")