import os 
import sys
import yaml
import speech_recognition as sr
import pyttsx3
from GreyMatter import cerebro

engine = pyttsx3.init('sapi5')


def speak(audio):
    print('Computer: ' + audio)
    engine.say(audio)
    engine.runAndWait()

profile = open('profile.yaml')
profile_data = yaml.safe_load(profile)
profile.close()
# Functioning Variables
name = profile_data['name']
city_name = profile_data['city_name']
speak('Bem vinda ' + name + ', Todos os sistemas estão funcionando corretamente. Como posso ajudar?')

def main():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Diga algo!")
        audio = r.listen(source)
        try:
            speech_text = r.recognize_google(audio).lower().replace("'", "")
            print("Venus acha que tu disseste: '" + speech_text + "'")
        except sr.UnknownValueError:
            print("A venus não consegue entender o audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
        cerebro(name, speech_text)
    main()