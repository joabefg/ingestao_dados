"""
Ingestão de dados em arquivo (csv) e banco de dados realacionais (mysql) e noqsl (elasticsearch)
"""
from faker import Faker
import random
def gerar_dados_funcionarios(num_funcionarios):
    """
    Gerar uma lista de dicionários contendo dados falsos de funcionários
    """
    fake = Faker('pt_br') # Usando o lacale brasileiro
    departamentos = ['TI', 'Recursos Humanos', 'Vendas', 'Marketing', 'Finaceiro']
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

    #1. Gerar os dados (Mock)
    funcionarios_mock = gerar_dados_funcionarios(NUM_FUNCIONARIOS)
    print(funcionarios_mock)