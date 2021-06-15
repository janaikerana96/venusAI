from GreyMatter import conversa

def cerebro(name, speech_text):
    def check_message(check):
        if speech_text == check:
            return True
        else:
            return False
        if check_message('quem es tu'):
            conversa.quem_es_tu()
        else:
            conversa.undefined()