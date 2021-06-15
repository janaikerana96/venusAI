import smtplib
import win32com.client 
import speech_recognition as sr

speaker = win32com.client.Dispatch("SAPI.SpVoice")

def enviar_email():
    speaker.Speak("Digite o email do destinatário, por favor.")
    print("Digite o email do destinatario")
    contacto = input()
    print("Venus entendeu:" + contacto + "'")  
    if contacto:
            speaker.Speak("Pode dizer a mensagem, Senhorita!")
            r = sr.Recognizer()
            with sr.Microphone() as source:
                r.adjust_for_ambient_noise(source)
                print("Vênus anotando:")
                audio = r.listen(source)
            try:        
                anotar = r.recognize_google(audio, language='pt-BR').lower().replace("'", "")
                print("Venus entendeu:" + anotar + "'")          
                conn = smtplib.SMTP('smtp.gmail.com', 587)
                type(conn)
                conn.ehlo()
                conn.starttls()
                conn.login("janaikerana@gmail.com", 'emachine')
                conn.sendmail('janaikerana@gmail.com', contacto, anotar)
                conn.quit()
                speaker.Speak('Email enviado com sucesso!')
                speaker.Speak('Aguardando próxima ordem.')
            except:
                speaker.Speak('Não foi possivél fazer a conexão. Tente mais tarde senhorita.')
    
