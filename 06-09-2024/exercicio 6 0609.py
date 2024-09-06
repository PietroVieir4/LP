'''
Vinicius, Pietro V e Rafael A
Exercicio 6
'''

lista1=[]
lista2=[]
lista3=[]

for i in range (3):
    user1=int(input(f"insira o {i+1}° numero"))
    lista1.append(user1)
for j in range (3):
    user2=int(input(f"insira o {j+4}° numero"))
    lista2.append(user2)
for f in range (3):
    user3=int(input(f"insira o {f+7}° numero"))
    lista3.append(user3)

matriz=[lista1, lista2, lista3]

def verifica_somas_linhas(matriz):
    resultados = []
    for i, linha in enumerate(matriz):
        soma_linha = sum(linha)
        if soma_linha > 15:
            resultados.append((i, soma_linha, True))
        else:
            resultados.append((i, soma_linha, False))
    return resultados


resultados = verifica_somas_linhas(matriz)
for i, soma, maior_que_15 in resultados:
    status = "maior que 15" if maior_que_15 else "não maior que 15"
    print(f"Soma da linha {i}: {soma} - {status}")
