# 1 - Função para criar audio
def cria_audio(mensagem):
    tts = gTTS(mensagem, lang="pt-br")
    tts.save("mensagem.mp3")
    playsound("mensagem.mp3")


# 2 - Utilização da função diretamente
# cria_audio("Aprendendo a linguagem Python para desenvolver Automação")

# 3 - Utilização da função via Input
# frase = input("Digite a frase a ser falada\\n")
# cria_audio(frase)

# 4 - Utilização da função via leitura de arquivo

arquivo = open("dados/texto.txt", "r", encoding="utf-8")
conteudo = arquivo.read()
cria_audio(conteudo)
