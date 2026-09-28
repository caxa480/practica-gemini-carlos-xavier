from google import genai
 
 # Sustituir por una API Key válida de Google AI Studio
client = genai.Client(api_key="TU_API_KEY")
 
response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents="Hola. Responde únicamente: Conexión correcta."
)
 
print(response.text)