from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

def chat():
    while True:
        user_input = input("Ask something (or type exit): ")

        if user_input.lower() == "exit":
            break

        try:
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=user_input
            )

            print("\nBot:", response.text, "\n")

        except Exception as e:
            print("[ERROR]:", e)
            print("Something went wrong.\n")