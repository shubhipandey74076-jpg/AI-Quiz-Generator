import os
import time
from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY not found in .env")

client = genai.Client(api_key=api_key)


def generate_quiz(topic, difficulty, number):

    prompt = f"""
Create {number} multiple-choice quiz questions about {topic}.

Difficulty: {difficulty}

For each question provide:
1. Question
2. Four options: A, B, C, D
3. Correct answer
4. Short explanation

Keep the questions suitable for college students.
"""

    for attempt in range(3):
        try:
            response = client.models.generate_content(
                model="gemini-3.5-flash-lite",
                contents=prompt
            )

            return response.text

        except Exception as e:
            if attempt < 2:
                time.sleep(3)
            else:
                return f"Gemini Error: {e}"