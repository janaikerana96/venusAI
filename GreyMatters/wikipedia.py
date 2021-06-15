# coding=utf-8
import win32com.client 
import re
import wikipedia
from googletrans import Translator

speaker = win32com.client.Dispatch("SAPI.SpVoice")

def pesquise(speech_text):
    words_of_message = speech_text.split()
    words_of_message.remove('pesquise')
    cleaned_message = ' '.join(words_of_message)
    
    try:
        wiki_data = wikipedia.summary(cleaned_message, sentences=3) 
        regEx = re.compile(r'([^\(]*)\([^\)]*\) *(.*)')
        m = regEx.match(wiki_data)
        while m:
            wiki_data = m.group(1) + m.group(2)
            m = regEx.match(wiki_data)
            wiki_data = wiki_data.replace("'", "")
            translator = Translator()
            wiki_data1 = translator.translate(wiki_data, src='en', dest='pt').text
            speaker.Speak(wiki_data1)
            speaker.Speak('Aguardando suas ordem Senhorita!')
    except wikipedia.exceptions.DisambiguationError as e:
        speaker.Speak('Você pode por gentileza ser mais específica?.')
        print("Você pode por gentileza ser mais específica?.; {0}".format(e))