from google import genai
import os

# Configuración del cliente
client = genai.Client(api_key="TU_API_KEY")

# Carpetas
carpeta_textos = "textos"
archivo_salida = "resultados/informe_textos.txt"

# Crear o sobrescribir el informe
with open(archivo_salida, "w", encoding="utf-8") as informe:

    for archivo in os.listdir(carpeta_textos):

        if archivo.endswith(".txt"):

            ruta = os.path.join(carpeta_textos, archivo)

            with open(ruta, "r", encoding="utf-8") as f:
                texto = f.read()

            prompt = f"""
            Analiza el siguiente texto e indica:

            1. Idioma
            2. Entidades nombradas
            3. Sentimiento
            4. Resumen

            Texto:
            {texto}
            """

            titulo = f"\n{'='*50}\nAnalizando {archivo}\n{'='*50}\n"

            print(titulo)
            informe.write(titulo)

            try:
                respuesta = client.models.generate_content(
                    model="gemini-3.8-flash",
                    contents=prompt
                )

                print(respuesta.text)
                informe.write(respuesta.text + "\n\n")

            except Exception as e:

                error = f"Error: {e}\n"

                print(error)
                informe.write(error)

print("\nInforme guardado en resultados/informe_textos.txt")
