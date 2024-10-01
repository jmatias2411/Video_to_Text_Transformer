# Video to Text Transformer

Este proyecto es un transformador de video a texto que utiliza bibliotecas como `moviepy`, `SpeechRecognition` y `pydub` para convertir un archivo de video en un archivo de texto. El flujo principal consiste en extraer el audio del video, dividir el audio en fragmentos de 60 segundos, y luego transcribir cada fragmento a texto.

## Características

- Extrae el audio de archivos de video utilizando `moviepy`.
- Divide el audio en fragmentos de 60 segundos para ajustarse a las limitaciones de la API gratuita de `SpeechRecognition`.
- Transcribe cada fragmento de audio a texto utilizando la API de Google.
- Guarda el texto transcrito en un archivo `.txt`.

## Requisitos

Este proyecto utiliza las siguientes bibliotecas de Python:

- [moviepy](https://github.com/Zulko/moviepy) - Para extraer el audio de los archivos de video.
- [SpeechRecognition](https://github.com/Uberi/speech_recognition) - Para la transcripción del audio a texto.
- [pydub](https://github.com/jiaaro/pydub) - Para dividir el audio en fragmentos de 60 segundos.

## Instalación

Primero, clona este repositorio en tu máquina local:

```bash
git clone <https://github.com/tuusuario/nombre-repositorio.git>
cd nombre-repositorio

```

Luego, instala las dependencias necesarias utilizando `pip`:

```bash
pip install moviepy SpeechRecognition pydub

```

> Nota: Asegúrate de tener instalado FFmpeg, ya que es necesario para que moviepy y pydub funcionen correctamente.
> 

Para instalar `FFmpeg`, puedes seguir las instrucciones de instalación del sitio web oficial o, en sistemas basados en Debian (como Ubuntu), puedes usar el siguiente comando:

```bash
sudo apt-get install ffmpeg

```

## Contribuciones

Si deseas contribuir a este proyecto, no dudes en hacer un fork y enviar una pull request. Cualquier contribución es bienvenida.

## Licencia

Este proyecto está bajo la licencia MIT. Consulta el archivo [LICENSE](https://www.notion.so/jmatias2411/LICENSE) para más detalles.
