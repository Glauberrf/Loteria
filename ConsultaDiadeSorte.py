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





def DiadeSorte():
    now = datetime.now()
    n1 = ""
    n2 = ""
    n3 = ""
    n4 = ""
    n5 = ""
    n6 = ""
    n7 = ""
    mes = ""


    page = requests.get('https://www.sorteonline.com.br/dia-de-sorte/resultados')

    soup = BeautifulSoup(page.text, 'html.parser')


    data = soup.find(class_='color header-resultados__datasorteio')

    data = str(data.contents[0])

    res = BeautifulSoup(page.text, "html.parser")
    tags = res.findAll("div", {"class": "time-coracao"})
    #print("Tag",tags)
    for tag in tags:
        print(tag.getText())
        mes = tag.getText()
        mes = mes.replace(' ', '')#Retirar o espaco em branco da String



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





        a = a + 1

    print("Data Consulta: ", dataAtual, "Hora Consulta: ", horaAtual)
    print("Concurso: ", concurso)
    print("Data do sorteio: ", data)
    print("Nº: ", n1, "Nº: ",n2, "Nº: ",n3, "Nº: ",n4, "Nº: ",n5, "Nº: ",n6, "Nº: ",n7, "Mes: ",mes)


    def escrever_json(lista):
        with open('DiadeSorte.json', 'w') as f:
            json.dump(lista, f)


    def carregar_json(arquivo):
        with open('DiadeSorte.json', 'r') as f:
            return json.load(f)



    minha_lista = {"Jogo":"Dia de Sorte","Concurso":concurso,"Data":data, "n1":n1, "n2":n2,"n3":n3,"n4":n4,"n5":n5,"n6":n6,"n7":n7,"Mes":mes,"Data da Consulta":dataAtual,"Hora da Consulta":horaAtual}
    escrever_json(minha_lista)

    print(carregar_json('DiadeSorte.json'))

