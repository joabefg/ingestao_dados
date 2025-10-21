"""
Ingestão de dados em arquivo (csv)
e bancos relacionais (mysql) e no sql (elasticsearch)  
"""
from faker import Faker
import random

def gerar_dados_fucionarios(num_fucionarios):
    """ 
    Gera uma lista de dicionarios contendo dados falsos de fucionarios
    """
    fake = Faker('pt_BR')#usando o locale brasileiro
    depatarmentos = ['TI', 'Recursos Humanos', 'Vendas', 'Marketing', 'Financeiro']
    escolaridades =['Ensino funamental', ' Ensino medio', 'Graduaçao', 'pos_Graduaçao']
    fucionarios = [ ]
    for i  in range(1, num_fucionarios + 1 ):
        data_nascimento = fake.date_of_birth(minimum_age=18 , maximum_age=60).strftime('%d/%m/%Y')
        fucionario = {
            'id': i,
            'cpf': fake.cpf(),
            'nome': fake.name(),
            'data_nascimento': data_nascimento,
            'departamento': random.choice(depatarmentos),
            'escolaridade': random.choice(escolaridades),
            'cidade': fake.city()
        }
        fucionarios.append(fucionario)
    return fucionarios

if __name__ == '__main__':
    NUM_FUCIONARIOS = 100
    NOME_ARQUIVO_CSV = ' fucionarios.csv'   
    NOME_TABELA = 'fucionarios'
    NOME_INDICE = 'fucionarios_index'

    #1. gerar os dados( mock)
    fucionarios_mock = gerar_dados_fucionarios(NUM_FUCIONARIOS)
    print(fucionarios_mock)