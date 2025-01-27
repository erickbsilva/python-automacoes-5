import speech_recognition as sr
from gtts import gTTS
from playsound import playsound


def cria_audio(audio, mensagem):
    tts = gTTS(mensagem, lang="pt-br")
    tts.save(audio)
    playsound(audio)


cria_audio("wellcome.mp3", "Olá. Vou reconhecer a sua voz")

recon = sr.Recognizer()
with sr.Microphone() as source:
    print("Diga alguma coisa\n")
    audio = recon.listen(source)

frase = recon.recognize_google(audio, language="pt-br")

cria_audio("mensagem2.mp3", frase)
