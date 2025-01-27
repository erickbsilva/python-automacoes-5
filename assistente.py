from gtts import gTTS
from playsound import playsound
import speech_recognition as sr
import sys
import funcoes_so
import funcoes_noticias
import funcoes_moedas
import os


def cria_audio(audio, mensagem):
    tts = gTTS(mensagem, lang="pt-br")
    tts.save(audio)
    playsound(audio)
    os.remove(audio)


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
    elif "horas" in acao:
        cria_audio("mensagem.mp3", funcoes_so.verifica_hora())
    elif "desligar computador" in acao and "uma hora" in acao:
        funcoes_so.desliga_computador_uma_hora()
    elif "desligar computador" in acao and "meia hora" in acao:
        funcoes_so.desliga_computador_meia_hora()
    elif "cancelar desligamento" in acao:
        funcoes_so.cancela_desligamento()
    elif "notícias" in acao:
        cria_audio("mensagem.mp3", funcoes_noticias.ultima_noticias())
    elif "cotação" in acao and "dólar" in acao:
        cria_audio("mensagem.mp3", funcoes_moeda.cotacao_moeda("Dólar"))
    elif "cotação" in acao and "euro" in acao:
        cria_audio("mensagem.mp3", funcoes_moeda.cotacao_moeda("Euro"))
    elif "cotação" in acao and "bitcoin" in acao:
        cria_audio("mensagem.mp3", funcoes_moeda.cotacao_moeda("Bitcoin"))


def main():
    cria_audio("wellcome.mp3", "Olá, sou a Maria. Em que posso lhe ajudar?")
    while True:
        monitora_audio()


main()
