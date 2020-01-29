# -*- coding: utf-8 -*-

def palindrome2(word):
	reversed_word = word[::-1]

	if reversed_word == word:
		return True

	return False


def palindrome(word):
	reversed_letters = []

	for letter in word:
		reversed_letters.insert(0, letter) #Agrega un nuevo elemento a la secuencia

	reversed_word = ''.join(reversed_letters) #Join recibe una secuencia de caracteres

	if reversed_word == word:
		return True

	return False



if __name__ == '__main__':
	word = str(input('Escribi una palabra: '))
	
	result = palindrome2(word)
	if result is True:
		print('{} sí es un palindromo'.format(word))
	else:
		print('{} no es un palindromo.'.format(word))