from google import genai
from PIL import Image

# Sustituir por una API Key válida de Google AI Studio
client = genai.Client(api_key="TU_API_KEY")

imagen = Image.open("foto.jpg")

try:
    response = client.models.generate_content(
        model="gemini-3.8-flash",
        contents=[
            "Describe detalladamente esta imagen",
            imagen
        ]
    )

    print(response.text)

except Exception as e:
    print("Error:")
    print(e)