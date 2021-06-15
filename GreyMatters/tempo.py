import requests
from googletrans import Translator
import win32com.client 

speaker = win32com.client.Dispatch("SAPI.SpVoice")
# Call example
#http://api.openweathermap.org/data/2.5/weather?q=London&units=metric&APPID=xxxxxxxxxxxxx
def como_esta_o_tempo():
    api_key = 'db273d39b6a384c12dff76a3ec93a625'
    city = 'Luanda'
    celsius = 'metric'
    url ='http://api.openweathermap.org/data/2.5/weather?q=Luanda&units={celsius}&APPID=db273d39b6a384c12dff76a3ec93a625'
    tempo = requests.get(url).json() 
    temp = tempo['weather'][0]['main']
    translator = Translator()
    temp1 = translator.translate(temp, src='en', dest='pt').text
    mini = float(tempo['main']['temp_min']) -273
    maxi = float(tempo['main']['temp_max']) -273
    falatempo = 'O tempo está: ', temp1, 'com temperatura minima de: ','%4.2f' % mini, 'graus', 'e Mássima de: ','%4.2f' % maxi, 'graus'
    speaker.Speak(falatempo)
    speaker.Speak('Aguardando suas ordem mestre.')
