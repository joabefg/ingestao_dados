from airflow.models.dag import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG(
    dag_id='hello_world_dag',
    start_date=datetime(2025, 10, 30),
    schedule_interval='@daily',
    catchup=False,
    default_args={ 'owner': 'airflow' }
) as dag:
# Tarefa 01: Imprimir olá Mundo
    hello_task = BashOperator(
        task_id='imprimir_hello',
        bash_command='echo "Airflow funcionando! olá mundo!"'
    )
# Tarefa 02: Imprimir data de hoje
    date_task = BashOperator(
        task_id='imprimir_data',
        bash_command='echo "A data de execução é {{ds}}"'
    )


