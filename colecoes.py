"""
Exemplos de uso das diferente coleções
"""
class Colecoes:
    def listas(self):
        #lista flexivel
        lista_flexivel = [123, 3.14, "texto", True]
        # ordenada
        posicao_dois = lista_flexivel[1]
        ultima_posicao = lista_flexivel[-1]
        print(lista_flexivel[-1] == lista_flexivel[3])
        print(f"segunda posição {posicao_dois} - ùtimo item: {ultima_posicao}")
        #mutavel
        print(f"lista inteira: {lista_flexivel}")
        lista_flexivel.remove(3.14)
        lista_flexivel.append("novo item")
        print(f"lista apos remocao: {lista_flexivel}")
        # lista aninhada
        matriz = [2, 4, 6],
        ["dois", "quatro", "seis"],
        [2.4, 4.6, 6.2]
        print(f"matriz: \n{matriz}")

    def tuplas(self):
        tupla_numeros = (1, 2, 4, 6, 12, 18)
        nova_tupla = tupla_numeros * 2
        print(f"tupla números: {tupla_numeros} - nova tupla: {nova_tupla}")

    def conjuntos(self):
        conjuntos_numeros = {1, 1, 2, 2, 3, 3, 4, 4}
        print(f"conjunto de números: {conjuntos_numeros}")
        conjunto_a = {'cadeira', 'mesa', 'computador', 'quadro'}
        conjunto_b = {'apagador', 'computador'}
        uniao = conjunto_a.union(conjunto_b)
        interseccao = conjunto_a.intersection(conjunto_b)
        diferenca = conjunto_a.difference(conjunto_b)
        print(f'uniao: {uniao} \n intersecção {interseccao} \n diferença {diferenca}')

    def dicionarios(self):
        #todo dicionario possui um conjunto de chave e um valor
        dict = {'chave': 'valor', 'atributo': 'valor', 'coluna': 'valor'}
        print(f"valor na chave atributo: {dict('atributo')}")
        funcionario = {'nome': 'Maria', 'cargo': 'psicologa', 'setor': 'RH'}
        print(f"funcionario \n dados: {funcionario}")
        print(f"o nome do funcionario é {funcionario['nome']}")
        #dicionario
        funcionario['cargo'] = 'Recruadora'
        funcionario['idade'] = 25
        print(f"dados apos alteração: {funcionario}")
        candidato = {'nome': {'primeiro': 'Maria', 'sobrenome': 'Silva'}, 'funcoes': ['dev', 'tester', 'devops'], 'idade': 25}
        print(f"dados do candidato: {candidato['nome']['sobrenome']}")

if __name__ == "__main__":
    instancia = Colecoes()
    instancia.listas()
    print("-"*30)
    instancia.tuplas()
    print("-"*30)
    instancia.conjuntos()