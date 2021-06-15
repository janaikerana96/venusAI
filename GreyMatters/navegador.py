import webbrowser
import win32com.client 

speaker = win32com.client.Dispatch("SAPI.SpVoice")
 
def abrir_youtube():
	speaker.Speak('abrindo o youtube')
	webbrowser.open('https://www.youtube.com')

def abrir_jornal_de_angola():
    speaker.Speak('abrindo o jornal')
    webbrowser.open('http://jornaldeangola.sapo.ao')
    
def abrir_facebook():
    speaker.Speak('abrindo o facebook')
    webbrowser.open('http://facebook.com')

def abrir_google():
    speaker.Speak('abrindo o google')
    webbrowser.open('http://google.com')

def filmes_online():
    speaker.Speak('abrindo os filmes')
    webbrowser.open('https://tuga.tv/filmes')
    
def baixar_series():
    speaker.Speak('abrindo as séries')
    webbrowser.open('https://tuga.tv/series')

def abrir_netflix():
    speaker.Speak('abrindo a netflix')
    webbrowser.open('https://www.netflix.com/browse')
    

  
  