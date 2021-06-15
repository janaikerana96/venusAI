# coding=utf-8
import win32com.client 
import requests
from bs4 import BeautifulSoup

speaker = win32com.client.Dispatch("SAPI.SpVoice")

def ler_as_noticias():
    def print_headlines(response_text):
        soup = BeautifulSoup(response_text, 'lxml')
        headlines = soup.find_all('h2', class_='title-h3')
        for headline in headlines:
            speaker.Speak(headline.text)
    
    url = 'http://jornaldeangola.sapo.ao/mundo'
    response = requests.get(url)
    print_headlines(response.text)