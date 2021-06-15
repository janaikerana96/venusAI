# coding=utf-8
import yaml, os
from subprocess import call
import speech_recognition as sr
import datetime
import win32com.client 
from cerebro import brain
from playsound import playsound


speaker = win32com.client.Dispatch("SAPI.SpVoice")

profile = open('profile.yaml')
profile_data = yaml.safe_load(profile)
profile.close()


name = profile_data['name']
city_name = profile_data['city_name']
playsound('C:\\Users\\Janai Kerana\\Documents\\Assistente\\Recursos\\init.mp3')
os.startfile('C:\\Users\\Janai Kerana\\Documents\\Assistente\\Recursos\\venus.jar')


speaker.Speak("Seja bem vinda "+ name +". Como posso ajudar?")       


def main():
    r = sr.Recognizer()
    while True:
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            r.energy_threshold = 4500
            print("Vênus ouvindo:")
            audio = r.listen(source)

        try:
            speech_text = r.recognize_google(audio, language='pt-BR').lower().replace("'", "")
            print("Venus entendeu:" + speech_text + "'")
        except sr.UnknownValueError:
            speaker.Speak("Pode repetir, senhorita")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
        brain(name, speech_text)

main()