from datetime import datetime




def Savelog():
    now = datetime.now()

    horaAtual = now.strftime('%H:%M')
    dataAtual = now.strftime('%d/%m/%Y')
    
    with open("LogConsulta.txt", "a") as arq:
        arq.write("Consulta as: '"+horaAtual+"' de '"+dataAtual+"'\n")
        print("Log salvo")

