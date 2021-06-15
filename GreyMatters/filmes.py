# coding=utf-8
import win32com.client 
import subprocess
import os
import random

speaker = win32com.client.Dispatch("SAPI.SpVoice")

def colocar_um_filme():
    speaker.Speak('Aprecie o seu filme, janai')
    movies = ['C:\\Users\\Janai Kerana\\Videos\\Avengers Infinity War (2018)\\Avengers.Infinity.War.2018.1080p.BluRay.x264-[YTS.AM].mp4',
          'C:\\Users\\Janai Kerana\\Videos\\Filmes Animes\\Kuroko no Basket Last Game.mp4',
          'C:\\Users\\Janai Kerana\\Videos\\Filmes Animes\\Boku no Hero Os Dois Herois\\Boku no Hero Os Dois Herois.mp4']
    subprocess.Popen([os.path.join("C:/", "Program Files", "VideoLAN", "VLC", "vlc.exe"),os.path.join(random.choice(movies))])