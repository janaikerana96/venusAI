# coding=utf-8
import winstats
import win32com.client
# optional
import locale
locale.setlocale(locale.LC_ALL, '')
fmt = lambda n: locale.format('%d', n, True)
meminfo = winstats.get_mem_info()

speaker = win32com.client.Dispatch("SAPI.SpVoice")

def estado_do_computador():
    speaker.Speak(" Estado da Memoria do PC:")
    speaker.Speak('Usada: %s%%' % fmt(meminfo.MemoryLoad))   
    speaker.Speak(" Performace do PC:")
    usage = winstats.get_perf_data(r'\Processor(_Total)\% Processor Time', fmts='double', delay=100)
    speaker.Speak('CPU: %.02f %%' % usage)
    speaker.Speak('Aguardando suas ordem Senhorita!')
    
 