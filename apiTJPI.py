from tjpiLibrary import folhaGeral
from fastapi import FastAPI, Query

app = FastAPI()

@app.get("/geral/")
async def read_item(
    ano: int = Query(2023, description="Ano da Folha de Pagamento"), 
    mes: int = Query(1, description="Mês da Folha de Pagamento 1=Janeiro, 2=Fevereiro, 3=Março ..."), 
    page: int = Query(1, description="Paginação da Folha de pagamento 1=Primeira página, 2=Segunda página ..."),
    ):

    folhaRef = folhaGeral(mes, ano, page)

    return {
        "folhaGeral":folhaRef[0],
        "quantidadePaginas":folhaRef[1],
        "ano":ano,
        "mes":mes
        }