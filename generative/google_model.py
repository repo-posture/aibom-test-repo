import google.generativeai as genai
from openai import OpenAI

# google-generativeai Library + gpt-4 Model (occurrence 4 of 4)
# Covers: AIBOM-08 (gpt-4 final occurrence), AIBOM-10 (Google provider component)
# Detail drawer: google-generativeai — verify Provider=Google, Type=Library

genai.configure(api_key="GOOGLE_API_KEY")

openai_client = OpenAI()


def generate_with_gemini(prompt: str) -> str:
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(prompt)
    return response.text


def generate_with_gpt4(prompt: str) -> str:
    response = openai_client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
    )
    return response.choices[0].message.content
