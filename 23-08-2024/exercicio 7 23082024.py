'''
Pietro V. Rafael A. e Vinicius
Exercicio 7 filtrando palavras curta
'''
palavras = {"python", "c", "java", "javascript", "go"}
for palavra in palavras:
    if len(palavra) < 5:
        print (palavra)
