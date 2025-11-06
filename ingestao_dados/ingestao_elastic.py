import elasticsearch
import requests
import time

url_BASE = "https://www.googleapis.com/books/v1/volumes"
URL_REQUISICAO = f"{url_BASE}?q=intitle:o Senhhor dos Anéis"
ELASTIC_HOST = "http://localhost:9200"
ELASTIC_INDEX = "livros"

try:
    resposta = requests.get(URL_REQUISICAO)
    dados_json = resposta.json()
except Exception as e:
    print(f"Erro ao realizar requisição: {e}")
print(dados_json)    
for item in dados_json['items']:
    titulo = item.get('volumeInfo', {}).get('title', 'Título não disponível')
    print(titulo)

    industry_ids = item.get('volumeInfo', {}).get('industryIdentifiers', [])
    for identificador in industry_ids:
        if identificador.get('type') == 'ISBN_13':
            isbn_13 = identificador.get('identifier')
            print(f"ISBN-13: {isbn_13}")
        if identificador.get('type') == 'ISBN_10':
            isbn_10 = identificador.get('identifier')
            print(f"ISBN-10: {isbn_10}")

    elastic = elasticsearch.Elasticsearch(ELASTIC_HOST)

    if not elastic.ping():
        raise ValueError("Conexão com Elasticsearch falhou")
    
    documento = {
        'titulo': titulo,
        'isbn_13': isbn_13,
        'isbn_10': isbn_10,
        'timestamp': int(time.time())
    }

    response = elastic.index(index=ELASTIC_INDEX, document=documento)
    print(f"Dados salvos com sucesso no elasticsearch. indice: {ELASTIC_HOST}")