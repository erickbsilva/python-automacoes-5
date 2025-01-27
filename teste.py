# import pyttsx3

# engine = pyttsx3.init()
# engine.setProperty("voice", "brazil")

# engine.say("Hello World!")
# engine.say("My current speaking rate is " + str(rate))
# engine.runAndWait()
# engine.stop()

import pyttsx3

engine = pyttsx3.init()
rate = engine.getProperty("rate")
engine.setProperty("rate", rate + 50)
engine.setProperty("voice", "brazil")
engine.setProperty("volume", 1.0)  # setting up volume level  between 0 and 1
engine.setProperty("languages", "brazil")
engine.say("Sally sells seashells by the seashore.")
# engine.say("The quick brown fox jumped over the lazy dog.")
engine.runAndWait()
