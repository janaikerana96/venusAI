# coding=utf-8
import win32com.client
import subprocess
import os


speaker = win32com.client.Dispatch("SAPI.SpVoice")

def abrir_firefox():
    speaker.Speak("Abrindo o navegador: ")
    subprocess.Popen(['C:\\Program Files\\Mozilla Firefox\\firefox.exe', '-new-tab'])
    
def abrir_word():
    speaker.Speak("Abrindo o word: ")
    subprocess.Popen(['C:\\Program Files (x86)\Microsoft Office\\root\Office16\\WINWORD.EXE'])
    speaker.Speak('Aguardando suas ordem Senhorita!')

def abrir_musicas():
    speaker.Speak("Abrindo o programa de musicas: ")
    os.startfile(['C:\\Users\\Janai Kerana\\Music\\m\\Jhene Aiko - Comfort Inn Ending  The Theorist Piano Cover.mp3'])
    
def abrir_antivirus():
    speaker.Speak("Abrindo o antivirus: ")
    subprocess.Popen(['C:\\Program Files\\AVAST Software\\Avast\\AvastUI.exe'])