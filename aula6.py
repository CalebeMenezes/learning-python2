# -*- utf-8 -*-
'''
vairaveis = iniciar com letra , pode conter numeros ,separa _, letras minusculas
'''

nome = "calebe" # valor de atribuição
idade = 18
altura = 1.80
é_maior = idade == 18 # nomne composto separa com _;
data_atual = 2020
peso = 70
imc = 21.60 # peso / (altura ** 2)
# variaveis nao podem começar com numeros

print('nome', nome, sep='--')
print('idade', idade, sep='--')
print('altura', altura, sep='--')
print('é_maior', é_maior, sep='--')

print(idade * altura)
print(data_atual / (idade * altura))
print(nome, 'tem', idade, 'de idade e seu imc', imc)