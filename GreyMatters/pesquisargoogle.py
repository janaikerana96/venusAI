# coding=utf-8
import webbrowser
import win32com.client 
import speech_recognition as sr

speaker = win32com.client.Dispatch("SAPI.SpVoice")

def pesqgoo():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("Vênus ouvindo:")
        speaker.Speak("O que deseja pesquisar?") 
        audio = r.listen(source)
    try:
        pesq1 = r.recognize_google(audio, language='pt-BR').lower().replace("'", "")
        print("Venus entendeu:" + pesq1 + "'")
        speaker.Speak("Pesquisando ...") 
        webbrowser.open('https://www.google.com.br/search?source=hp&ei=Ye1qXZz-CcjHwAKDuqOAAQ&q='+ pesq1 + '&oq=justib+&gs_l=psy-ab.3.0.0i10l10.2621.3889..5415...0.0..0.627.4097.4-4j4......0....1..gws-wiz.....0..0.hD8k53F0Efo+')
        speaker.Speak("Pesquisa concluida ...") 
    except:
        speaker.Speak("Não consigo encontrar!")


     
     