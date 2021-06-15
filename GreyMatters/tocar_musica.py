import webbrowser
import requests
import bs4
import os
import win32com.client


speaker = win32com.client.Dispatch("SAPI.SpVoice")


def musica_no_soundcloud():
    top_url = "https://soundcloud.com/charts/top"
    new_url = "https://soundcloud.com/charts/new"
    track_url = "https://soundcloud.com/search/sounds?q="
    artist_url = "https://soundcloud.com/search/people?q="
    mix_url_end = "&filter.duration=epic"
    
    webbrowser.open("https://soundcloud.com")
    speaker.Speak('Seja bem-vida a plataforma soundcloud')
    # menu
    print()
    print(">>> Python Soundcloud Scraper")
    print()




    # new or top menu
    while True:
        speaker.Speak("Escolha as opções de menu.")
        print(">>> 1 - Procurar Música")
        print(">>> 2 - Procurar artista")
        print(">>> 0 - Sair")
        print()
        choice = int(input(">>> Your choice: "))
        if choice == 0:
            break
        print()

        # search for a track
        if choice == 1:
            name = input("Nome da Música: ")
            print()
            "%20".join(name.split(" "))
            webbrowser.open(track_url + name)
            continue

        # search for an artist
        if choice == 2:
            name = input("Nome do artista: ")
            print()
            "%20".join(name.split(" "))
            webbrowser.open(artist_url + name)
            continue

        if choice == 3:
            name = input("Nome da mix: ")
            print()
            "%20".join(name.split(" "))
            webbrowser.open(track_url + name + mix_url_end)
            continue

        # genre menu
        url = ''
        if choice == 4: url = top_url
        else: url = new_url

        # parse the html with beautiful soup
        request = requests.get(url)
        soup = bs4.BeautifulSoup(request.text, "lxml")
        # print request.text

        genres = soup.select("a[href*=genre]")[2:]
        # print each genre

        genre_links = []

        # print out the available genres
        for index, genre in enumerate(genres):
            print(str(index) + ": " + genre.text)
            genre_links.append(genre.get("href"))

        print()
        
    
    print()
    speaker.Speak("Desligando a plataforma!")
