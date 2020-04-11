import random
import scoreboard

def runGame():

	sb = scoreboard.Scoreboard()

	while True:
		if(continuePlaying()):
			newMatch(sb)
			sb.printScoreboard()
		else:
			break


def continuePlaying():
	print('Would you like to play Rock, Paper, Sissors? Y or N')
	answer = input().upper().strip()
	if (answer == 'Y'):
		return True
	elif (answer == 'N'):
		return False
	else:
		continuePlaying()

def newMatch(scoreboard):
	cpu_choice = cpuPicker()
	print('Let\'s play! Rock, Paper, Sissors... Shoot!')
	my_choice = input().strip().upper()
	matchResult(my_choice, cpu_choice, scoreboard)

def cpuPicker():
	cpu_num = random.randint(0, 2)
	
	if cpu_num == 0:
		cpu_choice = 'ROCK'
	elif cpu_num == 1:
		cpu_choice = 'PAPER'
	elif cpu_num == 2:
		cpu_choice = 'SISSORS'

	return cpu_choice

def matchResult(my_choice, cpu_choice, scoreboard):
	print(my_choice + ' versus ' + cpu_choice)
	if(my_choice == cpu_choice):
		print('It\'s a draw!')
		scoreboard.addTie()
	elif (
		((my_choice == 'ROCK') and (cpu_choice == 'SISSORS')) or
		((my_choice == 'PAPER') and (cpu_choice == 'ROCK')) or
		((my_choice == 'SISSORS') and (cpu_choice == 'PAPER'))
		):
		print('You win this time!')
		scoreboard.addWin()
	elif (
		((my_choice == 'ROCK') and (cpu_choice == 'PAPER')) or
		((my_choice == 'PAPER') and (cpu_choice == 'SISSORS')) or
		((my_choice == 'SISSORS') and (cpu_choice == 'ROCK'))
		):
		print('You lose!')
		scoreboard.addLoss()
	else: 
		print('Invalid selection, try again')

