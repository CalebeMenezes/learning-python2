# -*- utf8 -*-

num1 = input("digite um numero: ")
num2 = input("digite outro numero: ")

# isnumeric / isdigit / isdecimal
#numeros e positivos (123454321)

'''
if num1.isdigit() and num2.isdigit()
	num1 = int(num1)
	num2 = int(num2)

	print(num1 + num2)
else:
	print("nao pude converter os numeros para realizar contasa")	
'''

try:
	num1 = float(num1)
	num2 = float(num2)

	print(num1 + num2)
except:
	print('error')
	