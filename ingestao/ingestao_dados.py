"""
Ingestâo de dados em arquivo (csv)
e bancos relacionais (mysql) e nosql (elasticsearch)
"""
from faker import Faker
import random

def gerar_dados_funcionarios(num_funcionarios):
    """
    Gera uma lista de dicionários contendo dados falsos de funcionários
    """
    fake = Faker('pt_BR') # Usando o locale brasileiro
    departamentos = ['TI', 'Recursos Humanos', 'Vendas', 'Marketing', 'Financeiro']
    escolaridades = ['Ensino Fundamental', 'Ensino Médio', 'Graduaçâo', 'Pós-Graduaçâo']
    funcionarios = []
    for i in range(1, num_funcionarios + 1):
        data_nascimento = fake.date_of_birth(minimum_age=18, maximum_age=60).strftime('%d/%m/%Y')
        funcionario = {
            'id': i,
            'cpf': fake.cpf(),
            'nome': fake.name(),
            'data_nascimento': data_nascimento,
            'departamento': random.choice(departamentos),
            'escolaridades': random.choice(escolaridades),
            'cidade': fake.city()
        }
        funcionarios.append(funcionario)
    return funcionarios 

if __name__ == '__main__':
    NUM_FUNCIONARIOS = 100 
    NOME_ARQUIVO_CSV = 'funcionarios.csv'
    NOME_TABELA = 'funcionarios'
    NOME_INDICE = 'funcionarios_index'

    # 1. Gerar od dados (mock)
    funcionarios_mock = gerar_dados_funcionarios(NUM_FUNCIONARIOS)
    print(funcionarios_mock)