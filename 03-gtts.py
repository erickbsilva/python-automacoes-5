from gtts import gTTS
from playsound import playsound

# tts = gTTS('Hello World')
tts = gTTS("Olá mundo. Vamos construir nosso assistente", lang="pt-br")
tts.save("audio.mp3")
playsound("audio.mp3")
