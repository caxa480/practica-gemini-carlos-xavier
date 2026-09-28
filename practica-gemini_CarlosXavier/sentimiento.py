from google import genai

# Sustituir por una API Key válida de Google AI Studio
client = genai.Client(api_key="TU_API_KEY")

textos = [
    "Me encanta este producto.",
    "El servicio fue horrible.",
    "Hoy es lunes.",
    "La película estuvo fantástica.",
    "Estoy descontento con la compra.",
    "I love this application.",
    "The service was terrible.",
    "The sky is blue.",
    "This movie is amazing.",
    "I am unhappy with the result."
]

for texto in textos:

    prompt = f"""
    Analiza el siguiente texto:

    {texto}

    Devuelve únicamente:

    Sentimiento: Positivo, Negativo o Neutro

    Entidades:
    """

    try:
        response = client.models.generate_content(
            model="gemini-3.8-flash",
            contents=prompt
        )

        print("\n" + "=" * 60)
        print("Texto:", texto)
        print(response.text)

    except Exception as e:
        print("\nError procesando:", texto)
        print(e)