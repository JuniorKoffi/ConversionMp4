import streamlit as st
from moviepy.editor import *
import tempfile


# Fonction de conversion vidéo en audio
def convert_video_to_audio(video_path, audio_path):
    video = VideoFileClip(video_path)
    audio = video.audio
    audio.write_audiofile(audio_path)


# Page Streamlit
def main():
    st.title("Convertir une vidéo en fichier audio")

    # Upload de la vidéo
    st.header("1. Téléchargez la vidéo")
    video_file = st.sidebar.file_uploader("Sélectionnez une vidéo", type=["mp4"])

    if video_file is not None:
        # Conversion vidéo en audio
        st.header("2. Conversion en cours...")
        video_path = os.path.join(tempfile.gettempdir(), "input.mp4")  # Chemin du fichier vidéo temporaire
        with open(video_path, "wb") as f:
            f.write(video_file.read())

        audio_file = os.path.join(tempfile.gettempdir(), "output.mp3")  # Chemin du fichier audio de sortie
        convert_video_to_audio(video_path, audio_file)

        # Téléchargement du fichier audio
        st.header("3. Télécharger le fichier audio")
        audio_bytes = open(audio_file, "rb").read()
        st.download_button(
            label="Cliquez ici pour télécharger le fichier audio",
            data=audio_bytes,
            file_name="audio.mp3",
        )


if __name__ == "__main__":
    main()
