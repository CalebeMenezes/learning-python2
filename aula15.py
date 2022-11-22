# -*- utf-8 -*-
'''
formatando valores com modificadores 

:s - texto (string)
:d - inteiros (int)
:f - numeros de ponto flutuante (float)
:. (numero)f - quantidade de casas decimais (float)
;(caractere)(> ou < ou ^)(quantidade)(tipo- s, d ou f)
> - esquerda
< - direita
^ - centro
'''
num1 = 10
num2 = 3
divisao = num1 / num2
print("{:.2f}".format(divisao))

num_1 = 1
print(f'{num_1:0>10}')

num_2 = 1150
print(f'{num_2:0^10}')

print(f'{num_2:.2f}')

print(f'{num_2:0>10.2f}')

nome = "calebe"
print( 50-len(nome) / 2)
#print(f'{nome:#^50}')
#sobrenome = "menezes"
#ome_formatado = '{1}'.format(nome, sobrenome)
#pritn(nome_formatado)


print(nome.lower())# tudo minusculo
print(nome.upper())# tudo maiusculo 
print(nome.title())# primeira letra maiuscula

