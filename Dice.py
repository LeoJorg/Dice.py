import random

def Dice():
	primary_dice = round(random.random() * 6)
	return primary_dice

print(''' 
8888888b. d8b                 
888  "Y88bY8P                 
888    888                    
888    888888 .d8888b .d88b.  
888    888888d88P"   d8P  Y8b 
888    888888888     88888888 
888  .d88P888Y88b.   Y8b.     
8888888P" 888 "Y8888P "Y8888

By LeoJorg.
''')

turns = [1, 2, 3]

def main(main_input):
	if main_input=='1':
		print(f'o dado caiu em {dice}')
	if main_input=='2':
		print(''' 
		Esse programa e um simulador de dado simples.
		rode o dado e um numero aleatorio de 0 a 6 ira sair.
		''')
	if main_input=='3':
		print('Ate mais... ;)')
		exit()
while True:
	dice = Dice()
	print('''
Para rodar o dado, digite 1.
Para a discricao, digite 2.
Para sair, digite 3 ou ctrl+c.
	''')
	dice_input = input()
	main(dice_input)
