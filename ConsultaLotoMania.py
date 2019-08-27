import datetime, time
import os
import requests
from bs4 import BeautifulSoup
from datetime import date
import os.path
import time, sys
import sqlite3
from datetime import datetime
import platform
import json
from ftplib import FTP
import fileinput





def LotoMania():
    now = datetime.now()
    n1 = ""
    n2 = ""
    n3 = ""
    n4 = ""
    n5 = ""
    n6 = ""
    n7 = ""
    n8 = ""
    n9 = ""
    n10 = ""
    n11 = ""
    n12 = ""
    n13 = ""
    n14 = ""
    n15 = ""
    n16 = ""
    n17 = ""
    n18 = ""
    n19 = ""
    n20 = ""

    page = requests.get('https://www.sorteonline.com.br/lotomania/resultados')

    soup = BeautifulSoup(page.text, 'html.parser')


    data = soup.find(class_='color header-resultados__datasorteio')
    data = str(data.contents[0])



    concurso = soup.find(class_='color header-resultados__nro-concurso')
    concurso = str(concurso.contents[0])



    artist_name_list = soup.find(class_='result result-default center')
    artist_name_list_items = artist_name_list.find_all('li')

    horaAtual = now.strftime('%H:%M')
    dataAtual = now.strftime('%d/%m/%Y')



    #Use .contents to pull out the <a> tag’s children
    a = 0
    for artist_name in artist_name_list_items:
        #numerosMega = str(artist_name.contents[a])
        
        if(a == 0):
            n1 = str(artist_name.contents[0])
           
        if(a == 1):
            n2 = str(artist_name.contents[0])
        if(a == 2):
            n3 = str(artist_name.contents[0])
        if(a == 3):
            n4 = str(artist_name.contents[0])
        if(a == 4):
            n5 = str(artist_name.contents[0])
        if (a == 5):
            n6 = str(artist_name.contents[0])
        if (a == 6):
            n7 = str(artist_name.contents[0])
        if (a == 7):
            n8 = str(artist_name.contents[0])
        if (a == 8):
            n9 = str(artist_name.contents[0])
        if (a == 9):
            n10 = str(artist_name.contents[0])
        if (a == 10):
            n11 = str(artist_name.contents[0])
        if (a == 11):
            n12 = str(artist_name.contents[0])
        if (a == 12):
            n13 = str(artist_name.contents[0])
        if (a == 13):
            n14 = str(artist_name.contents[0])
        if (a == 14):
            n15 = str(artist_name.contents[0])
        if (a == 15):
            n16 = str(artist_name.contents[0])
        if (a == 16):
            n17 = str(artist_name.contents[0])
        if (a == 17):
            n18 = str(artist_name.contents[0])
        if (a == 18):
            n19 = str(artist_name.contents[0])
        if (a == 19):
            n20 = str(artist_name.contents[0])

        a = a + 1

    print("Data Consulta: ", dataAtual, "Hora Consulta: ", horaAtual)
    print("Concurso: ", concurso)
    print("Data do sorteio: ", data)
    print("Nº: ", n1, "Nº: ",n2, "Nº: ",n3, "Nº: ",n4, "Nº: ",n5, "Nº: ",n6, "Nº: ",n7, "Nº: ",n8, "Nº: ",n9, "Nº: ",n10, "Nº: ",n11, "Nº: ",n12, "Nº: ",n13, "Nº: ",n14, "Nº: ",n15, "Nº: ",n16, "Nº: ",n17, "Nº: ",n18, "Nº: ",n19, "Nº: ",n20)


    def escrever_json(lista):
        with open('LotoMania.json', 'w') as f:
            json.dump(lista, f)


    def carregar_json(arquivo):
        with open('LotoMania.json', 'r') as f:
            return json.load(f)



    minha_lista = {"Jogo":"Lotomania","Concurso":concurso,"Data":data, "n1":n1, "n2":n2,"n3":n3,"n4":n4,"n5":n5,"n6":n6,"n7":n7,"n8":n8,"n9":n9,"n10":n10,"n11":n11,"n12":n12,"n13":n13,"n14":n14,"n15":n15,"n16":n16,"n17":n17,"n18":n18,"n19":n19,"n20":n20,"Data da Consulta":dataAtual,"Hora da Consulta":horaAtual}
    escrever_json(minha_lista)

    print(carregar_json('LotoMania.json'))

