from datetime import datetime as dtime
import requests
import pandas as pd
from bs4 import BeautifulSoup
import asyncio


def folhaGeral(mes = 1,ano = 2020, page = 1):
    
    try:
        meses = {1:"Janeiro",2:"Fevereiro",3:"Março",4:"Abril",5:"Maio",6:"Junho",7:"Julho",8:"Agosto",9:"Setembro",10:"Outubro",11:"Novembro",12:"Dezembro"}

        nomeMes = meses[mes]

        urlbase = "http://transparencia.tjpi.jus.br/folhas/geral?page=#PG#&q%5Bano_eq%5D=#ANO#&q%5Bmes_eq%5D=#MES#&q%5Bmvps_vinculo_in%5D="
        url = urlbase.replace("#PG#",str(page)).replace("#ANO#",str(ano)).replace("#MES",str(mes)) 

        page = requests.get(url)

        soup =  BeautifulSoup(page.content, "html.parser")  
        paginacao = soup.find_all("a",class_="page-link")[-1]["href"]
        totalPaginas = int(paginacao[(paginacao.find("=")+1):paginacao.find("&")])

        nome_colunas = ["Nome", "Lotação", "Cargo", "RP (I)", "VP (II)", "Sub", "Ind (III)", "VE (IV)", "GD (V)", "TC", "PP (VI)", "IR (VII)", "DD (VIII)", "RTC (IX)", "TD (X)", "RL (XI)", "ROO (XII)", "Diárias (XIII)"]
        numero_colunas = len(nome_colunas)
        nome_colunas.append("Mês")
        nome_colunas.append("Ano")
        nome_colunas.append("Referência")
        nome_colunas.append("Id") 
        resultado = []
        valores = soup.select("tbody tr")
        for linha in list(valores):    
                celulas = linha.find_all("td") 
                if len(celulas) == numero_colunas:  
                    lista = [celula.get_text().strip() for celula in celulas]
                    matricula = celulas[0].a["href"]
                    matricula = matricula[(matricula.find("/",1)+1):matricula.find("?")]          
                    lista.append(nomeMes+"/"+str(ano))
                    lista.append(matricula)
                    for valores in range(3,18):
                        lista[valores] = float(lista[valores].replace("R$ ","").replace(".","").replace(",","."))
                    resultado.append(lista)
        
        dfResultado = pd.DataFrame(resultado,columns=["Nome","Lotacao","Cargo","RP","VP","SUB","IND","VE","GD","TC","PP","IR","DD","RTC","TD","RL","ROO","Diarias","Referencia","Id"])
        
        return dfResultado.to_dict(orient="records"), totalPaginas
    except:
        return "Erro", 0