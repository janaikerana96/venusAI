# coding=utf-8
import os,sys
import win32com.client
import webbrowser

speaker = win32com.client.Dispatch("SAPI.SpVoice")

#abrir os meus documentos
def abrir_documentos():
    speaker.Speak("Abrindo os Documentos: ")
    webbrowser.open('C:\\Users\\Janai Kerana\\Documents')
 
#abrir as tranferencias
def abrir_transferencias():
    speaker.Speak("Abrindo as transferências: ")
    webbrowser.open(r"C:\Users\Janai Kerana\Downloads")

#abrir musicas
def abrir_musicas():
    speaker.Speak("Abrindo as Musicas: ")
    webbrowser.open(r"C:\Users\Janai Kerana\Music")

#abrir imagens
def abrir_imagens():
    speaker.Speak("Abrindo as imagens: ")
    webbrowser.open(r"C:\Users\Janai Kerana\Pictures")

#abrir videos
def abrir_videos():
    speaker.Speak("Abrindo os videos: ")
    webbrowser.open(r"C:\Users\Janai Kerana\Videos")
    

