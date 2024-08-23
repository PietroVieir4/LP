'''
Pietro V. Rafael A. e Vinicius
Exercicio 5 Contando Caracteres em uma String
'''
palavra = "programação"
contagem = {}
for caractere in palavra:   
    if caractere in contagem:
        contagem[caractere] += 1    
    else:
        contagem[caractere] = 1
for caractere, quantidade in contagem.items():
    print(f"'{caractere}': {quantidade}")
