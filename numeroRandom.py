# -*- coding: utf-8 -*-
import random

def run():
	numero_maximo = int(input("Ingresa Numero maximo: "))

	number_found = False
	random_number = random.randint(0, 20) #Crea un numero aleatorio entre 0 y 20

	while not number_found:
		number = int(input('Intenta un numero: '))

		if number == random_number:
			print('Encontraste el numero era el: ' + str(random_number))
			number_found = True
		elif number > random_number:
			print('El numero es mas chico')
		else: 
			print('El numero es mas grande')

if __name__ == '__main__':
	run()