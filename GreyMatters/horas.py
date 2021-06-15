# coding=utf-8
from datetime import datetime
import win32com.client
from googletrans import Translator

speaker = win32com.client.Dispatch("SAPI.SpVoice")

def que_horas_sao():
    speaker.Speak("As horas são: " + datetime.strftime(datetime.now(), '%H:%M:%S'))
    speaker.Speak('Aguardando suas ordem Senhorita!')
    
def que_dia_e_hoje():
    speaker.Speak("Hoje é dia: " + datetime.strftime(datetime.now(), '%d'))
    speaker.Speak('Aguardando suas ordem Senhorita!')
    
def mes():
    translator = Translator()
    temp1 = translator.translate(datetime.strftime(datetime.now(), '%B'), src='en', dest='pt').text
    speaker.Speak("Estamos no mês de: " + temp1)
    speaker.Speak('Aguardando suas ordem Senhorita!')
    
def ano():
    speaker.Speak("Estamos em: " + datetime.strftime(datetime.now(), '%Y'))
    speaker.Speak('Aguardando suas ordem Senhorita!')