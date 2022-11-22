# -*- utf-8 -*-

nome = 'calebe'
idade = 19
altura = 1.80
peso = 70.5
ano_atual = 2020
ano_que_nasci = ano_atual - idade
imc = peso / (altura ** 2)

print(ano_atual - idade)
print('imc é igual a', peso / (altura ** 2))
print(f'{nome} tem {idade} de idade {altura} de altura {peso} de peso seu imc é {imc:.2f} e o ano em que nasceu foi {ano_que_nasci}')
print('{} tem {} de idade sau altura é {} seu peso é {} seu imc é {} e o ano em que nasceu foi {}'. format(nome, idade, altura, peso, imc, ano_que_nasci))

print("my name is {}".format(nome))
print(f"my name is {nome}")