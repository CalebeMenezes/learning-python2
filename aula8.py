# -*- utf-8 -*-

'''
entrada de dados 
'''

#input("qual o seu nome?") # input serve para pegar os dados do usuarios
nome = input("qual o seu nome?") # o que o usuario escrever vai ser a variavel
print(f"o usuario digitou {nome} e o tipo da variavel é" f"{type(nome)}")
# qualquer coisa que o usuario digitar no codigo 'input' vai ser 'str'
idade = input("qual a sua idade? ")

print(f'{nome} tem {idade} anos')

#ano_nascimento = 2020 - idade # se deixar assim vai dar erro , temos que formatar o tipo
ano_nascimento = 2020 - int(idade)

numero_1 = int(input('digite um numero: '))
numero_2 = int(input('digite outro numero : '))

print(numero_1 + numero_2)
print(numero_1 **  numero_2)