# -*- utf8 -*-
usuario = input("digite seu usuario")
qtd_caracteres = len(usuario)

ptint(usuario, qtd_caracteres, type(qtd_caracteres))
if qtd_caracteres < 6:
	print('você precisa pelo menos 6 caracteres')

else:
	print('você foi cadastrado no sistema')

'''
'''

string1 = input('digite alguma coisa')
string2 = input('digite outra coisa')

ptint(f'a quantidade total de caracteres gigitados foi {len(string1) + len(string2)}')
# len conta a quantidade de caracteres em uma string , não funciona com numeros

