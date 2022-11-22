# -*- utf-8 -*-

nome = 'calebe'
idade = 18 
altura =1.80
peso = 70
imc = peso / (altura ** 2)

print(f'{nome} tem {idade} de idade e seu imc é {imc:.2f}')
# o 'F' antes de tudo significa = fstring = serve para formatar o print
# os :.2 serve para escolher ate quantas casas mostrar 
print('{} tem {} de idade e seu imc é {} '. format(nome, idade, imc))
print('{0} tem {1} de idade e seu imc é {2} '. format(nome, idade, imc))
#posso colocar letra ou numeros para simbolosar os dados entre {}.

