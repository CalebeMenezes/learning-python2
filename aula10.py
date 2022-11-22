# -*- utf-8 -*-

'''
operadores relacionais 
==  igualdede
> maior que
>= maior que ou igual a
< menor que 
<= menor que ou igual a 
!= diferente

'''
nome = input('qual o seu nome?')
idade = input('qual sua idade?')
idade_menor = 20 
idade_maior = 20


idade = int(idade)

if idade >= idade_menor and idade <= idade_maior:
	print(f'{nome} pode pegar emprestimo.')
else:
	print(f'{nome} não pode pegar emprestimo.')