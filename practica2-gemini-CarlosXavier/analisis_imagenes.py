from google import genai
from PIL import Image
import os

# Configuración del cliente
client = genai.Client(api_key="TU_API_KEY")

# Carpetas
carpeta_imagenes = "imagenes"
archivo_salida = "resultados/informe_imagenes.txt"

# Crear o sobrescribir el informe
with open(archivo_salida, "w", encoding="utf-8") as informe:

    for archivo in os.listdir(carpeta_imagenes):

        if archivo.lower().endswith((".jpg", ".jpeg", ".png")):

            ruta = os.path.join(carpeta_imagenes, archivo)

            titulo = (
                f"\n{'='*60}\n"
                f"Analizando {archivo}\n"
                f"{'='*60}\n"
            )

            print(titulo)
            informe.write(titulo)

            try:
                # Abrir imagen
                imagen = Image.open(ruta)

                prompt = """
                Analiza esta imagen e indica:

                1. Texto detectado (OCR)
                2. Descripción detallada de la escena
                3. Tipo de escena
                4. Objetos detectados
                """

                # Enviar a Gemini
                respuesta = client.models.generate_content(
                    model="gemini-3.8-flash",
                    contents=[prompt, imagen]
                )

                print(respuesta.text)
                informe.write(respuesta.text + "\n\n")

            except Exception as e:

                error = f"Error: {e}\n\n"

                print(error)
                informe.write(error)

print("\nInforme guardado en resultados/informe_imagenes.txt")