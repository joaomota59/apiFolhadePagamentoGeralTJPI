# API para o Acesso a Folha de Pagamento Geral do TJPI

## Instalação das libs
```pip install -r requirements.txt```

## Inicialização da API
```uvicorn apiTJPI:app --reload```

## Rotas

### Folha de Pagamento Geral
* Acesso 1: http://127.0.0.1:8000/geral?ano=2020&mes=1&page=1
* Acesso 2 / Acesso Alternativo - Via Swagger: http://127.0.0.1:8000/docs

> Parâmetros de entrada da rota </br>
> ano = ano da folha de pagamento Ex: 2020, 2021, 2022, 2023... </br>
> mes = mes da folha de pagamento Ex: 1,2,3,4... </br>Obs: 1 corresponde a Janeiro, 2 a Fevereiro...</br>
> page = responsavel pela paginação da folha de pagamento... Ex: 1,2,3,4...</br>
