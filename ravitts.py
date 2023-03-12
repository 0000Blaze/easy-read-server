import pyttsx3

def textToSpeech2(text):
    filename ="response.mp3"
    engine = pyttsx3.init()
    # voice = engine.getProperty('voices') #get the available voices
    # print(voice)
    # engine.setProperty('voice', voice[1].id) #changing voice to index 1 for female voice
    engine.setProperty('rate', 150)
    engine.save_to_file(text, filename)
