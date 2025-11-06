import elasticsearch
import requests
import time

URL_BASE = "https://www.googleapis.com/books/v1/volumes"
URL_REQUISICAO = f"{URL_BASE}?q=intitle:O Senhor dos Anéis"
ELASTIC_HOST = "http://localhost:9200"
ELASTIC_INDEX = "livros"

try:
    resposta = requests.get(URL_REQUISICAO)
    dados_json = resposta.json()
except Exception as e:
    print(f"Erro ao realizar requisição: {e}")
for item in dados_json['items']:
    titulo = item.get('volumeInfo', {}).get('title', 'título não encontrado')
    print(f"Título: {titulo}")
    # industry_ids = item.get('volumeInfo', {}).get('industryIndentifiers', [])
    industry_ids = item.get('volumeInfo', {}).get('industryIdentifiers', [])
    for identificador in industry_ids:
        if identificador.get('type') == 'ISBN_13':
            isbn_13 = identificador.get('identifier')
            print(f"ISBN 13 {isbn_13}")
        if identificador.get('type') == 'ISBN_10':
            isbn_10 = identificador.get('identifier')
            print(f"ISBN 10 {isbn_10}")

    elastic = elasticsearch.Elasticsearch(ELASTIC_HOST)

    if not elastic.ping():
        raise ValueError("A conexão com o elastic falhou")

    documento = {
        'titulo': titulo,
        'isbn_13': isbn_13,
        'isbn_10': isbn_10,
        'timestamp': int(time.time())
    }

    response = elastic.index(index=ELASTIC_INDEX, document=documento)
    print(f"Dados salvos com sucesso no Elasticsearch. índice: {ELASTIC_INDEX}")
    