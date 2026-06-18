import google.generativeai as genai
from core.config import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)

try:
    model = genai.GenerativeModel("gemini-2.0-flash")
except Exception:
    model = None


def analyze_sentiment(text: str):

    try:
        if model:
            prompt = f"""
            Analiza el sentimiento del siguiente comentario.

            Responde solamente con:
            positivo
            negativo
            neutral

            Comentario:
            {text}
            """

            response = model.generate_content(prompt)
            return response.text.strip().lower()

    except Exception:
        pass

    text = text.lower()

    positive_words = [
        "excelente",
        "bueno",
        "genial",
        "rápido",
        "recomendado",
        "perfecto"
    ]

    negative_words = [
        "malo",
        "terrible",
        "horrible",
        "lento",
        "dañado"
    ]

    if any(word in text for word in positive_words):
        return "positivo"

    if any(word in text for word in negative_words):
        return "negativo"

    return "neutral"