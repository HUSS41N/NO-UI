from random import randint
from sys import exit
randomnumber = randint(1,3)

print('ROCKkkk, PAPERrrr, SCISSORrr')
wins = 0
losses = 0
ties = 0
while True:
	print('RECORD')
	print(f'{wins}-Wins,{losses}-Losses,{ties}-Ties')
	print('Enter your Move (r)ock (p)aper (s)cissor (q)uit')
	playerinput = input()

	if playerinput == 'q':
		print('Okay BYE!!!!')
		exit()

	if playerinput == 'r' and randomnumber == 1:
		print('ROCK versuss ROCK' )
		print('Its a Tie')
		ties += 1
	elif playerinput == 'r' and randomnumber == 2:
		print('ROCK versuss PAPER' )
		print('COMPUTER WON')
		losses += 1
	elif playerinput == 'r' and randomnumber == 3:
		print('ROCK versuss SCISSOR' )
		print('Player won')
		wins += 1

	elif playerinput == 'p' and randomnumber == 1:
		print('PAPER versuss ROCK')
		print('Player WON')
		wins += 1
	elif playerinput == 'p' and randomnumber == 2:
		print('PAPER versuss PAPER')
		print('Its a Tie')
		ties += 1
	elif playerinput == 'p' and randomnumber == 3:
		print('PAPER versuss SCISSOR')
		print('COMPUTER won')
		losses += 1

	elif playerinput == 's' and randomnumber == 1:
		print('SCISSOR versuss ROCK ')
		print('COMPUTER WON')
		losses += 1
	elif playerinput == 's' and randomnumber == 2:
		print('SCISSOR versuss PAPER')
		print('Player WON')
		wins += 1
	elif playerinput == 's' and randomnumber == 3:
		print('SCISSOR versuss SCISSOR')
		print('Its a Tie')
		ties += 1

	elif playerinput != 'r' or playerinput != 's' or playerinput != 'p':
		print('Enter a valid choice')