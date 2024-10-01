from moviepy.editor import VideoFileClip
import speech_recognition as sr
from pydub import AudioSegment

# Solicitar al usuario la ruta del video
mi_video = input("Ingresa la ruta de tu video (por ejemplo, /content/video.mp4): ")

# Función para convertir video mp4 a audio
def convertir_video_a_audio(video_path, output_audio_path):
    try:
        # Cargamos el video
        video = VideoFileClip(video_path)

        # Extraemos el audio y lo guardamos como un archivo .mp3 o .wav
        video.audio.write_audiofile(output_audio_path)
        print(f"El audio se ha guardado correctamente en {output_audio_path}")

    except Exception as e:
        print(f"Ocurrió un error: {e}")

# Ruta del video MP4 ingresada por el usuario
ruta_video = mi_video

# Ruta donde se guardará el audio extraído
ruta_salida_audio = "audio.wav"  # Puedes cambiar la ruta del archivo de salida si lo necesitas

# Convertimos el video a audio
convertir_video_a_audio(ruta_video, ruta_salida_audio)

audio_path = "/content/audio.wav"

# Función para dividir el audio en partes más pequeñas
def dividir_audio_en_segmentos(audio_path, duracion_segmento_ms=60000):
    audio = AudioSegment.from_wav(audio_path)
    segmentos = [audio[i:i+duracion_segmento_ms] for i in range(0, len(audio), duracion_segmento_ms)]
    return segmentos

# Función para convertir un segmento de audio en texto
def audio_a_texto_por_segmentos(audio_segment, recognizer, contador):
    audio_path_segmento = f"segmento_{contador}.wav"
    audio_segment.export(audio_path_segmento, format="wav")
    with sr.AudioFile(audio_path_segmento) as source:
        audio_data = recognizer.record(source)
        try:
            texto = recognizer.recognize_google(audio_data, language="es-ES")
            print(f"Texto del segmento {contador}:")
            print(texto)
            return texto
        except sr.UnknownValueError:
            print(f"No se pudo entender el audio del segmento {contador}")
        except sr.RequestError as e:
            print(f"No se puede conectar al servicio de Google en el segmento {contador}: {e}")
    return ""

# Convertir todo el audio a texto, dividiendo en segmentos más pequeños
def convertir_audio_completo_a_texto(audio_path):
    recognizer = sr.Recognizer()
    segmentos = dividir_audio_en_segmentos(audio_path)
    texto_completo = ""
    for i, segmento in enumerate(segmentos):
        texto_segmento = audio_a_texto_por_segmentos(segmento, recognizer, i)
        texto_completo += texto_segmento + " "

    # Guardar el texto completo en un archivo
    with open("texto_extraido_audio.txt", "w", encoding="utf-8") as f:
        f.write(texto_completo)

    return texto_completo

# Ejecutar
texto_extraido = convertir_audio_completo_a_texto(audio_path)
print("Texto completo extraído del audio: ")
print(texto_extraido)