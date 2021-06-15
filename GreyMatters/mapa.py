import webbrowser
import win32com.client 
import speech_recognition as sr

speaker = win32com.client.Dispatch("SAPI.SpVoice")

def mapa():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("Vênus ouvindo:")
        speaker.Speak("O que deseja localizar?")
        audio = r.listen(source)

    try:
        lugar = r.recognize_google(audio, language='pt-BR').lower().replace("'", "")
        print("Venus entendeu:" + lugar + "'")
        speaker.Speak("Procurando o local ...") 
        webbrowser.open('https://www.google.com/maps/place/'+lugar)
        speaker.Speak("Aguardando novas ordens ...") 

    except:
            speaker.Speak("Não consigo encontrar!")

     