# coding=utf-8
import win32com.client 
import os
import sqlite3
from datetime import datetime

speaker = win32com.client.Dispatch("SAPI.SpVoice")
 
 
def ler_o_lembrete():
     lembrete = open('C:\\Users\\Janai Kerana\\Desktop\\lembrete\\lembretes.txt')
     msg =lembrete.read()
     speaker.Speak("A Senhorita deve se lembrar que:" + msg + ". Lembrete concluido")