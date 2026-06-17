import google.generativeai as genai

genai.configure(api_key="GOOGLE_API_KEY")

# Models: gemini-1.5-pro, gemini-1.5-flash, gemini-pro


def chat_gemini_pro(prompt: str) -> str:
    model = genai.GenerativeModel("gemini-1.5-pro")
    return model.generate_content(prompt).text


def chat_gemini_flash(prompt: str) -> str:
    model = genai.GenerativeModel("gemini-1.5-flash")
    return model.generate_content(prompt).text


def chat_gemini_legacy(prompt: str) -> str:
    model = genai.GenerativeModel("gemini-pro")
    return model.generate_content(prompt).text
