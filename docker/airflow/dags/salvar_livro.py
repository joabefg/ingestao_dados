import pendulum
import requests
import json
from airflow.models.dag import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.postgres.hooks.postgres import PostgresHook

POSTGRES_CONN_ID = "postgres_conn"
BOOK_ISBN = "9781449339739"

def buscar_livro_api(isbn):
    url = f"https://www.googleapis.com/books/v1/volumes?q=isbn:{isbn}"
    response = requests.get(url)
    data = response.json()

    volume = data['items'][0]['volumeInfo']
    titulo = volume.get('title', 'N/A')
    autores = ', '.join(volume.get('authors', ['Autor Desconhecido']))

    for identifier in volume.get('industryIdentifiers', []):
        if identifier['type'] == 'ISBN_10':
            isbn_10 = identifier['identifier']
        elif identifier['type'] == 'ISBN_13':
            isbn_13 = identifier['identifier']

    livro_info = {
        "isbn_10": isbn_10,
        "isbn_13": isbn_13,
        "titulo": titulo,
        "autor": autores
    }

    print(f"Dados extraídos: {titulo}")
    return livro_info

def salvar_no_postgres(**context):
    livro_info = context['ti'].xcom_pull(task_ids='fetch_book_details')
    isbn_10 = livro_info['isbn_10']
    isbn_13 = livro_info['isbn_13']
    titulo = livro_info['titulo'].replace("'", "''")
    autor = livro_info['autor'].replace("'", "''")

    pg_hook = PostgresHook(postgres_conn_id=POSTGRES_CONN_ID)

    sql_criacao = f"""
    CREATE TABLE IF NOT EXISTS public.livros_api (
        isbn_13 VARCHAR(20) PRIMARY KEY, 
        isbn_10 VARCHAR(20),
        titulo VARCHAR(100),
        autor VARCHAR(100),
        data_insercao TIMESTAMP DEFAULT NOW()
    )
    """

    pg_hook.run(sql_criacao)
    SQL_insercao = f"""
        INSERT INTO public.livros_api
        VALUES ('{isbn_13}', '{isbn_10}', '{titulo}', '{autor}')
    """
    pg_hook.run(SQL_insercao)
    print("Dados inseridos com sucesso!")

with DAG(
    dag_id='books_from_googleapis_to_postgres',
    start_date=pendulum.datetime(2025, 11, 4, tz="UTC"),
    schedule_interval='@daily',
    catchup=False,
    tags=['apis', 'postgresql', 'googleapi'],
)as dag:
    # Tarefa 01: Buscar dados da API
    fetch_task = PythonOperator(
        task_id='fetch_book_details',
        python_callable=buscar_livro_api,
        op_kwargs={'isbn': BOOK_ISBN}
    )
    # Tarefa 02: Salvar no banco de dados
    save_task = PythonOperator(
        task_id='save_to_database',
        python_callable=salvar_no_postgres
    )

# Ordem de Execução (Dependecias)
fetch_task >> save_task