import pyttsx3

engine = pyttsx3.init()
engine.setProperty("voice", "brazilian")
# engine.say("Hello World. Language Python")
engine.say("Olá mundo. Vamos construir um assistente virtual.")
engine.runAndWait()
