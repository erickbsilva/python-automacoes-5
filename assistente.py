from gtts import gTTS
from playsound import playsound
import speech_recognition as sr
import sys
import funcoes_so


def cria_audio(audio, mensagem):
    tts = gTTS(mensagem, lang="pt-br")
    tts.save(audio)
    playsound(audio)


def monitora_audio():
    recon = sr.Recognizer()
    with sr.Microphone() as source:
        while True:
            print("Diga alguma coisa")
            audio = recon.listen(source)
            try:
                mensagem = recon.recognize_google(audio, language="pt-br")
                mensagem = mensagem.lower()
                print("Você disse ", mensagem)
                executa_comandos(mensagem)
                break
            except sr.UnknownValueError:
                pass
            except sr.RequestError:
                pass
        return mensagem


def executa_comandos(acao):
    if "fechar assistente" in acao:
        sys.exit()


def main():
    cria_audio("wellcome.mp3", "Olá, sou a Maria. Em que posso lhe ajudar?")
    while True:
        monitora_audio()


main()
