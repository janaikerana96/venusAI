# coding=utf-8
import win32com.client 
import random

speaker = win32com.client.Dispatch("SAPI.SpVoice")


def venus():
    messages = ['Estou aqui janai.',
               'Ao seu dispor',
               'Sim?, Precisa de alguma coisa?']
    speaker.Speak(random.choice(messages))


def quem_e_voce():
    messages = ['Eu sou a vênus, sua assistente pessoal.',
               'Venus, não disse antes? ',
               'Eu sou a Vênus.']
    speaker.Speak(random.choice(messages))

def obrigada_venus():
    messages = ['De nada senhorita.',
               'é um prazer ajudar',
               'Sempre as ordens']
    speaker.Speak(random.choice(messages))
    
def como_eu_estou():
    respostas =['Tu estás muito gira!', 
                'Meus joelhos ficam fracos quando te vejo.',
                'Tu estás linda!', 
                'Tu és a pessoa mas doce que já conheci!']
    speaker.Speak(random.choice(respostas))


def quem_programou():
    messages = ['Janai Kerana.',
               'Senhorita Janai.',
               'Eu fui programada pela Janai.']
    speaker.Speak(random.choice(messages))
    
def linguagem_programacao():
    messages = ['Eu fui escrita em python.',
               'Estou sendo escrita em python.',
               'Em python.']
    speaker.Speak(random.choice(messages))
    
def nao_falei():
    messages = ['Okay',
               'Esta bem. Pensei que ouvi algo. Qual quer coisa é só chamar.',
               'Ficarei calada.']
    speaker.Speak(random.choice(messages))
    
def undefined():
    speaker.Speak('Não consigo perceber! Repita por favor')