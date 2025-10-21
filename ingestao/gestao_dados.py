"""
Ingestão de dados em arquivo (csv)
e Bancos relacionais (mysql) e nosql (elasticsearch)
"""
from faker import Faker
import random

def gerar_dados_funcionarios(num_funcionarios):
    """
    Gera uma lista de dicionarios contendo dados falsos de funcionarios
    """
    fake = Faker('pt_BR') #usando o locale brasileiro
    departamentos = ['TI', 'Recursos Humanos', 'vendas', 'Marketing', 'Financeiro']
    escolaridades = ['Ensino fundamental', 'Ensino Médio', 'Graduação', 'pós-Graduação']
    funcionarios = []
    for  i in range(1, num_funcionarios + 1):
        data_nascimento = fake.date_of_birth(minimum_age=18, maximum_age=60).strftime('%d/%m/%Y')
        funcionario ={
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

    # 1. Gerar dados (mock)
    funcionarios_mock = gerar_dados_funcionarios(NUM_FUNCIONARIOS)
    print(funcionarios_mock)