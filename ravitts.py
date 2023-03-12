import pyttsx3

def textToSpeech2(text):
    filename ="response.mp3"
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    # engine.runAndWait()
    engine.save_to_file(text, filename)
    engine.runAndWait()
