import random
import os

def Dice():
	primary_dice = round(random.random() * 6)
	return primary_dice

turns = [1, 2, 3]

def main(main_input):
	os.system('clear')
	if main_input=='1':
		os.system('clear')
		print(f'o dado caiu em {dice}')
	if main_input=='2':
		os.system('clear')
		print(''' 
		Esse programa e um simulador de dado simples.
		rode o dado e um numero aleatorio de 0 a 6 ira sair.
		''')
	if main_input=='3':
		os.system('clear')
		print('Ate mais... ;)')
		exit()

while True:
	print(''' 
8888888b. d8b                                       
888  "Y88bY8P                                       
888    888                                          
888    888888 .d8888b .d88b.       88888b. 888  888 
888    888888d88P"   d8P  Y8b      888 "88b888  888 
888    888888888     88888888      888  888888  888 
888  .d88P888Y88b.   Y8b.       d8b888 d88PY88b 888 
8888888P" 888 "Y8888P "Y8888    Y8P88888P"  "Y88888 
                                   888          888 
                                   888     Y8b d88P 
                                   888      "Y88P"  


By LeoJorg.
	''') 
	dice = Dice()
	print('''
> Para rodar o dado, digite 1.
> Para a discricao, digite 2.
> Para sair, digite 3 ou ctrl+c.
	''')
	dice_input = input()
	main(dice_input)
