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
import ConsultaMegaSena
import ConsultaQuina
import ConsultaLotoFacil
import ConsultaLotoMania
import ConsultaDiadeSorte
import SaveLog

now = datetime.now()

cronoSec = 1
cronoMin = 1

consultar = False

sistema = platform.system()

if(sistema == "Windows"):
    apagar = "cls"
    pausar = "pause"
if(sistema == "Linux"):
    apagar = "clear"
    pausar =  "read"

                 

while True:
    
    if(cronoSec == 0):
        cronoMin = cronoMin - 1
        cronoSec = 60



    if(cronoMin == 0):
        consultar = True
        cronoMin = 120
        cronoSec = 60   
    time.sleep(1)
    #os.system(apagar)
    cronoSec = cronoSec - 1


    print(50*"-")
    print(10*" ","Consulta sorteio LOTERIAS")
    print(50*"-")
    print ("Tempo para próxima consulta: ", cronoMin, ":",cronoSec)
    print(50 * "-")

    if(consultar == True):
        try:
            ConsultaMegaSena.MegaSena()
        except Exception as e:
            print("type error: " + str(e))
        try:
            ConsultaQuina.Quina()
        except Exception as e:
            print("type error: " + str(e))
        try:
            ConsultaLotoFacil.LotoFacil()
        except Exception as e:
            print("type error: " + str(e))
        try:
            ConsultaLotoMania.LotoMania()
        except Exception as e:
            print("type error: " + str(e))
        try:
            ConsultaDiadeSorte.DiadeSorte()
        except Exception as e:
            print("type error: " + str(e))

        

        localfile1 = "MegaSena.json"
        localfile2 = "Quina.json"
        localfile3 = "LotoFacil.json"
        localfile4 = "LotoMania.json"
        localfile5 = "DiadeSorte.json"

        try:
            ftp = FTP()
            ftp.set_debuglevel(2)
            ftp.connect('loteria.eu5.org', 21)
            ftp.login('loteria.eu5.org', 'gislaine123')
            ftp.cwd('/Loterias')





            fp = open(localfile1, 'rb')
            ftp.storbinary('STOR %s' % os.path.basename(localfile1), fp)
            fp = open(localfile2, 'rb')
            ftp.storbinary('STOR %s' % os.path.basename(localfile2), fp)
            fp = open(localfile3, 'rb')
            ftp.storbinary('STOR %s' % os.path.basename(localfile3), fp)
            fp = open(localfile4, 'rb')
            ftp.storbinary('STOR %s' % os.path.basename(localfile4), fp)
            fp = open(localfile5, 'rb')
            ftp.storbinary('STOR %s' % os.path.basename(localfile5), fp)
            fp.close()
            print ("Os arquivos foram carregados: " + localfile1+" : "+localfile2 +" : "+localfile3+" : "+localfile4+" : "+localfile5)

            consultar = False
            SaveLog.Savelog()

        except Exception as e:
            print("type error: " + str(e))





