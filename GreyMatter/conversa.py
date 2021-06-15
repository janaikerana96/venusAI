import pyttsx3

engine = pyttsx3.init('sapi5')


def speak(audio):
    print('Computer: ' + audio)
    engine.say(audio)
    engine.runAndWait()

def quem_es_tu():
    message = 'Eu sou a venus, sua assistente pessoal.'
    speak(message)
def undefined():
    speak('Não consigo perceber!')