# coding=utf-8
import win32com.client 
import requests
from bs4 import BeautifulSoup

speaker = win32com.client.Dispatch("SAPI.SpVoice")

def filmes_em_cartaz():
    def print_headlines(response_text):
        soup = BeautifulSoup(response_text, 'lxml')
        headlines = soup.find_all('h2', class_='movie-title movie-list-item-title')
        for headline in headlines:
            speaker.Speak(headline.text)
            
    url = 'https://cinemax.co.ao/'
    response = requests.get(url)
    print_headlines(response.text)
    
