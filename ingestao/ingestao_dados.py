"""
Ingestão de dados em arquivo (csv) e bancos relacionais (mysql) e nosql (elasticsearch)
"""
from faker import Faker
import random

def gerar_dados_funcionarios(num_funcionarios):
    """
    Gera uma lista de funcionarios contendo dados falsos de funcionarios
    """
    fake = Faker('pt_BR') # Usando o local brasileiro
    departamentos = ['TI', 'Recursos Humanos', 'Vendas', 'Markenting', 'Financeiro']
    escolaridades = ['Ensino Fundamental', 'Ensino Médio', 'Graduação', 'Pós-Graduação']
    funcionarios = []
    for i in range(1, num_funcionarios + 1):
        data_nascimento = fake.date_of_birth(minimum_age=18, maximum_age=60).strftime('%d/%m/%Y')
        funcionario = {
            'id': i,
            'cpf': fake.cpf(),
            'nome': fake.name(),
            'data_nascimento': data_nascimento,
            'departamento': random.choice(departamentos),
            'escolaridade': random.choice(escolaridades),
            'cidade': fake.city()
        }
        funcionarios.append(funcionario)
    return funcionarios

if __name__ == '__main__':
    NUM_FUNCIONARIOS = 100
    NOME_ARQUIVO_CSV = 'funcionarios.csv'
    NOME_TABELA = 'funcionarios'
    NOME_INDICE = 'funcionarios_index'

    # 1. Gerar os dados (Mock)
    funcionarios_mock = gerar_dados_funcionarios(NUM_FUNCIONARIOS)
    print(funcionarios_mock)