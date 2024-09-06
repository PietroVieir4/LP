'''
Pietro V. Rafael A. e Vinicius
Exercicio 9 Removendo Duplicadas de uma Lista
'''

lista1 = [1, 2, 2, 3, 4, 4, 5]
lista2 = []
for numero in lista1:
    if numero not in lista2:
        lista2.append(numero)
print (lista2)
