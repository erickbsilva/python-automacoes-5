import pyttsx3

engine = pyttsx3.init()
engine.setProperty("voice", "brazil")
engine.setProperty("languages", "brazilian")

"""VOLUME"""
volume = engine.getProperty(
    "volume"
)  # getting to know current volume level (min=0 and max=1)
print(volume)  # printing current volume level
engine.setProperty("volume", 100.0)  # setting up volume level  between 0 and 1


# 2 - Utilizando Leitura do Arquivo de Texto
arquivo = open("dados/texto.txt", "r", encoding="utf-8")
conteudo = arquivo.read()
engine.say(conteudo)
engine.runAndWait()
