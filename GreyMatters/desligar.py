# coding=utf-8
import win32com.client 
import sys
import os
from playsound import playsound

speaker = win32com.client.Dispatch("SAPI.SpVoice")

def go_to_sleep():
    speaker.Speak('Adeus! Tenha um otimo dia!')
    playsound('C:\\Users\\Janai Kerana\\Documents\\Assistente\\Recursos\\Shutdown.mp3')
    os.system("TASKKILL /F /IM javaw.exe")
    sys.exit()