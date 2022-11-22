# -*- utf8 -*

usuario = input("digite um numero inteiro: ")
if usuario.isdigit():
	usuario = int(usuario)
	if usuario % 2 == 0:
		print(f"{usuario} par")
	else:
		print(f"{usuario} impar")			
else:
	print("isso nao pe um numero inteiro")	
qtd_num = len(usuario)
print(usuario, qtd_num, type(qtd_num))
if qtd_num =(2,4,6,8,10):
	print("o numero é par")
else qtd_num =(1,3,5,7,,9):
	print("o numero é impar")
'''
'''

adm = input("digite a hora: ")
adm = int(usuario)
hora = len(usuario)

if hora = (0,1,2,3,4,5,6,7,8,9,10,11):
	print("bom dia")
else hora = (12,13,14,15,16,17):	
	print("boa terde")
else hora = (18,19,20,21,22,23):
	print("boa noite")

'''
'''

pessoa = input("digite seu nome: ")	
qtd_caract = len(pessoa)

print(pessoa, qtd_caract, type(qtd_caract))

if qtd_caract <= 4:
	print("seu nome é curto")
else qtd_caract >=7:
	print("seu nome é grande")
else qtd_caract = 5,6:
	print("seu nome é normal")
'''
'''