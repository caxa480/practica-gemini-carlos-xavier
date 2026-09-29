# Práctica 2 - Análisis de Texto e Imágenes con Gemini

## Autor

**Carlos Eduardo Xavier Pereira**

---

# Descripción del Proyecto

El objetivo de esta práctica es desarrollar una solución basada en la API de Gemini para realizar tareas de análisis automático de texto e imágenes utilizando Python.

Para ello se han implementado dos scripts independientes:

- `analisis_texto.py`
- `analisis_imagenes.py`

Ambos scripts utilizan modelos de inteligencia artificial de Gemini para extraer información relevante de diferentes tipos de contenido.

---

# Objetivos

## Análisis de Texto

El script de análisis de texto permite:

- Detectar el idioma del texto.
- Identificar entidades nombradas.
- Analizar el sentimiento.
- Generar resúmenes automáticos.

Se procesan automáticamente diez documentos de prueba almacenados en la carpeta `textos`.

---

## Análisis de Imágenes

El script de análisis de imágenes permite:

- Extraer texto mediante OCR.
- Describir el contenido visual de una imagen.
- Clasificar el tipo de escena.
- Detectar objetos presentes en la imagen.

Se procesan automáticamente cinco imágenes almacenadas en la carpeta `imagenes`.

---

# Tecnologías Utilizadas

- Python 3
- Gemini API
- Google GenAI SDK
- Pillow (PIL)
- Librería OS

---

# Estructura del Proyecto

```text
practica2-gemini-CarlosXavier/
│
├── imagenes/
│   ├── imagen1.jpg
│   ├── imagen2.jpg
│   ├── imagen3.jpg
│   ├── imagen4.jpg
│   └── imagen5.jpg
│
├── textos/
│   ├── texto1.txt
│   ├── texto2.txt
│   ├── texto3.txt
│   ├── texto4.txt
│   ├── texto5.txt
│   ├── texto6.txt
│   ├── texto7.txt
│   ├── texto8.txt
│   ├── texto9.txt
│   └── texto10.txt
│
├── resultados/
│   ├── informe_textos.txt
│   └── informe_imagenes.txt
│
├── analisis_texto.py
├── analisis_imagenes.py
├── notebook.ipynb
└── README.md
```

---

# Instalación

## 1. Descargar el proyecto

Clonar el repositorio o descargar el proyecto en formato ZIP.

```bash
git clone URL_DEL_REPOSITORIO
```

---

## 2. Instalar las dependencias

Instalar las librerías necesarias:

```bash
pip install google-genai
pip install pillow
```

Comprobar que la instalación se ha realizado correctamente:

```bash
pip list
```

---

## 3. Configurar la API Key

Generar una API Key desde Google AI Studio.

Posteriormente sustituir:

```python
client = genai.Client(api_key="TU_API_KEY")
```

por la clave de la API personal correspondiente.

> Importante: No compartir ni publicar la API Key en repositorios públicos o en chats de IA, pues así cualquier persona podría utilizar su cuota del servicio.

---

# Ejecución del Proyecto

## Análisis de Texto

Ejecutar:

```bash
python analisis_texto.py
```

El script recorrerá automáticamente todos los documentos de la carpeta `textos`, enviará la información a Gemini y almacenará los resultados en:

```text
resultados/informe_textos.txt
```

---

## Análisis de Imágenes

Ejecutar:

```bash
python analisis_imagenes.py
```

Así como en el análisis de texto el script de análisis de imágenes recorrerá todas las imágenes de la carpeta `imagenes`, realizará el análisis visual mediante Gemini y almacenará los resultados en:

```text
resultados/informe_imagenes.txt
```

---

# Funcionamiento del Script de Texto

El archivo `analisis_texto.py` realiza los siguientes pasos:

1. Accede a la carpeta `textos`.
2. Lee automáticamente cada archivo `.txt`.
3. Construye un prompt para Gemini.
4. Envía el contenido a la API.
5. Obtiene la respuesta generada por el modelo.
6. Guarda los resultados en un informe.

Para cada texto se solicita:

- Idioma detectado.
- Entidades nombradas.
- Sentimiento.
- Resumen.

### Ejemplo de resultado

```text
Idioma: Español

Entidades:
- Microsoft

Sentimiento:
- Positivo

Resumen:
Microsoft presentó nuevas funcionalidades de inteligencia artificial orientadas a mejorar la productividad empresarial.
```

---

# Funcionamiento del Script de Imágenes

El archivo `analisis_imagenes.py` realiza las siguientes tareas:

1. Accede a la carpeta `imagenes`.
2. Abre cada imagen utilizando la librería Pillow.
3. Envía la imagen junto con un prompt de análisis a Gemini.
4. Obtiene los resultados generados por el modelo.
5. Guarda toda la información en un informe.

Para cada imagen se solicita:

- OCR --> texto detectado.
- Descripción de la escena.
- Clasificación de la escena.
- Objetos detectados.

### Ejemplo de resultado

```text
Texto detectado:
Factura Nº12345

Descripción:
Documento fotografiado sobre una mesa.

Tipo de escena:
Interior - Documento

Objetos detectados:
- Papel
- Mesa
```

---

# Resultados Obtenidos

Durante las pruebas realizadas se comprobó el correcto funcionamiento de:

- Lectura automática de archivos de texto.
- Procesamiento masivo de documentos.
- Generación automática de análisis mediante Gemini.
- Apertura y procesamiento de imágenes mediante Pillow.
- Envío de contenido multimodal a Gemini.
- Generación automática de informes de resultados.

Los resultados obtenidos se almacenan en los siguientes archivos:

```text
resultados/informe_textos.txt
```

```text
resultados/informe_imagenes.txt
```

---

# Dificultades Encontradas

Durante el desarrollo del proyecto se detectaron algunas limitaciones asociadas al uso de la API de Gemini, que hizo que la execución del proyecto no fuera completamente satisfactoria.

En determinados momentos el servicio devolvió errores relacionados con:

```text
503 UNAVAILABLE
```

debido a periodos de alta demanda de los servidores.

También se obtuvieron errores:

```text
429 RESOURCE_EXHAUSTED
```

cuando se alcanzó el límite de peticiones disponibles en la cuota gratuita de la API.

Los scripts incluyen gestión de errores para registrar estas incidencias dentro de los informes generados.

---

# Conclusiones

Esta práctica ha permitido aplicar técnicas de inteligencia artificial generativa mediante la API de Gemini para resolver tareas de procesamiento de texto e imágenes.

A través de los scripts desarrollados se han trabajado conceptos como:

- Integración de APIs.
- Procesamiento automático de archivos.
- Ingeniería de prompts.
- Análisis de lenguaje natural.
- OCR.
- Clasificación visual.
- Detección de objetos.
- Generación automática de informes.

Además, se ha adquirido experiencia en el uso de algunos modelos multimodales y en la automatización de procesos mediante Python.Además, se ha adquirido experiencia en el uso de algunos modelos multimodales y en la automatización de procesos mediante Python. Aunque, al haber alcanzado la cuota gratuita de la API de Gemini, ha sido muy interesante explorar y obtener esa experiencia.

---
