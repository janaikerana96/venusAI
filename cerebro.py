# coding=utf-8
from GreyMatters import desligar, horas, conversa, tempo, wikipedia, navegador, notas,mapa,pesquisargoogle, enviar_email, abrir_pastas,filmes, ler_noticias
from GreyMatters import cartaz, programas, sistema, tocar_musica

def brain(name, speech_text ):
    def check_message(check):
        words_of_message = speech_text.split()
        if set(check).issubset(set(words_of_message)):
            return True
        else:
            return False
         
    #Converas  
    if check_message(['quem','é', 'você']) or check_message(['como', 'é', 'você']) or check_message(['quem', 'és', 'tu']):
        conversa.quem_e_voce()
    elif check_message(['como', 'eu', 'to']) or check_message(['como', 'eu', 'estou']) or check_message(['como','estou']):
        conversa.como_eu_estou()
    elif check_message(['obrigada', 'vênus']) or check_message(['obrigada']) or check_message(['muito','obrigada']):
        conversa.obrigada_venus()
    elif check_message(['vênus']) or check_message(['vênus','estás', 'ai?']):
        conversa.venus()
    elif check_message(['quem','programou','você']) or check_message(['quem','te', 'programou']):
        conversa.quem_programou()
    elif check_message(['em','que','linguagem','você','foi','escrita']) or check_message(['qual','linguangem', 'você', 'é','escrita']) or check_message(['qual','é', 'a', 'tua','linguagem']):
        conversa.linguagem_programacao()
    elif check_message(['não','falei','nada']) or check_message(['não','disse', 'nada']) or check_message(['Cala','a', 'boca']) or check_message(['cala','boca']) or check_message(['podes','calar']) or check_message(['podes','cala']):
        conversa.nao_falei()
            
     #Funcionalidades no Explorer -Windows
    elif check_message(['abrir','documentos']) or check_message(['meus', 'documentos']) or check_message(['meus', 'documento']) or check_message(['abrir','documento']) or check_message(['abrir', 'os','meus','documentos']) or check_message(['abrir','os','documentos']):
        abrir_pastas.abrir_documentos()
    elif check_message(['abrir','transfêrencias']) or check_message(['minhas', 'transferências']) or check_message(['abrir','as','transfêrencias']) or check_message(['transfêrencias']) or check_message(['abrir','as', 'minhas','transfêrencias']):
            abrir_pastas.abrir_transferencias()
    elif check_message(['abrir','músicas']) or check_message(['minhas', 'músicas']) or check_message(['abrir','as','minhas','músicas']) or check_message(['abrir','as','músicas']):
            abrir_pastas.abrir_musicas()
    elif check_message(['abrir','imagens']) or check_message(['minhas', 'imagens']) or check_message(['abrir','as','minhas','imagens']) or check_message(['abrir','as','imagens']):
            abrir_pastas.abrir_imagens()
    elif check_message(['abrir','vídeos']) or check_message(['meus', 'vídeos']) or check_message(['meus','os', 'vídeos']) or check_message(['abrir','os', 'meus','vídeos']) or check_message(['abrir','os','vídeos']) or check_message(['abrir','os','vídeo']) or check_message(['abri','os','vídeos']):
            abrir_pastas.abrir_videos()           

        
    #Funcionalidades adicionais   
    elif check_message(['horas']) or check_message(['que', 'horas', 'sao']) or check_message(['que', 'horas', 'são']) or check_message(['que', 'horas', 'sao']) or check_message(['diga', 'as' 'horas']):
       horas.que_horas_sao()
    elif check_message(['dia']) or check_message(['que', 'dia', 'é', 'hoje']) or check_message([ 'dia', 'de', 'hoje']):
        horas.que_dia_e_hoje()
    elif check_message(['mês']) or check_message(['estamos', 'em', 'que', 'mês']) or  check_message(['em', 'que', 'mês','estamos']):
        horas.mes()
    elif check_message(['ano']) or check_message(['estamos', 'em', 'que', 'ano']):
        horas.ano()
    elif check_message(['como', 'está', 'o','tempo']) or check_message(['tempo']):
        tempo.como_esta_o_tempo()
    elif check_message(['pesquise']):
        wikipedia.pesquise(speech_text)
    elif check_message(['ler','lembrete']) or check_message(['lembretes', 'por', 'favor']) or check_message(['ler', 'o','lembrete']) or check_message(['ler','lembretes']) or check_message(['ler', 'os','lembretes']):
        notas.ler_o_lembrete()
    elif check_message(['enviar','e-mail']) or check_message(['mandar','e-mail']):
        enviar_email.enviar_email()  
    elif check_message(['coloque','um','filme']) or check_message(['colocar','um','filme']) or check_message(['coloca','um','filme']):
        filmes.colocar_um_filme()
    elif check_message(['ler','as','notícias']) or check_message(['notícias','sobre','o',' mundo']) or check_message (['ler','as','notícia']):
        ler_noticias.ler_as_noticias() 
    elif check_message(['filmes','em','cartaz']) or check_message(['em', 'cartaz','no','cinema']):
        cartaz.filmes_em_cartaz()
    elif check_message(['estado','do','computador']) or check_message(['estado','do','sistema']):
        sistema.estado_do_computador()
    elif check_message(['música','no','soundcloud']) or check_message(['música','na','internet']):
        tocar_musica.musica_no_soundcloud()

    
    #Programas
    elif check_message(['abrir','firefox']) or check_message(['firefox']):
        programas.abrir_firefox()
    elif check_message(['abrir','word']) or check_message(['word']) or check_message(['abrir', 'o','word']):
        programas.abrir_word()
    elif check_message(['tocar','música']) or check_message(['coloque','música']) or check_message(['toca','música']) or check_message(['coloca','músicas']):
        programas.abrir_musicas()
    elif check_message(['abrir','antivírus']) or check_message(['antivírus']) or check_message(['anti-virus']):
        programas.abrir_antivirus()
     
        
    #Funcionalidades no navegador
    elif check_message(['localizar','no','mapa']) or check_message(['abrir','o', 'mapa']):
        mapa.mapa() 
    elif check_message(['abrir','jornal']) or check_message(['abrir','o','jornal']) or check_message(['abrir','jornal', 'de','angola']):
        navegador.abrir_jornal_de_angola()
    elif check_message(['pesquisar']) or check_message(['pesquisar','na','google']) or check_message(['procurar','no', 'google']):
        pesquisargoogle.pesqgoo()
    elif check_message(['abre','o','youtube']) or check_message(['abrir','o', 'youtube']):
        navegador.abrir_youtube()
    elif check_message(['abre','o','facebook']) or check_message(['abrir','o', 'facebook']):
        navegador.abrir_facebook()
    elif check_message(['abre','o','google']) or check_message(['abrir','o', 'google']) or check_message(['abrir','a', 'google']):
        navegador.abrir_google()
    elif check_message(['abre','os','filmes','online']) or check_message(['abrir','os', 'filme','online']):
        navegador.filmes_online()
    elif check_message(['abre','as','séries','online']) or check_message(['abrir','as', 'séries','online']):
        navegador.baixar_series()
    elif check_message(['netflix']) or check_message(['abrir','netflix']):
        navegador.abrir_netflix()
 
    
       #Desligar Sistema
    elif check_message(['desligar']) or check_message(['encerrar', 'vênus']):
        desligar.go_to_sleep()
  
    else:
        conversa.undefined()