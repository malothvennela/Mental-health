# llm_response.py

import google.generativeai as genai

genai.configure(api_key="AIzaSyAiOgBuAB88YuIvhtKQO-G2S6XcJrOPoBY")

model = genai.GenerativeModel(model_name="gemini-2.0-flash")

def generate_response(message):
    try:
        response = model.generate_content(message)
        return response.text
    except:
        return "I'm here for you. Tell me more."
