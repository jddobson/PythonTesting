class Scoreboard:

	def __init__(self):
		self.wins = 0
		self.losses = 0
		self.ties = 0

	def addWin(self):
		self.wins += 1

	def addLoss(self):
		self.losses += 1

	def addTie(self):
		self.ties += 1

	def printScoreboard(self):
		print('Your current record is:')
		print('Wins: ' + str(self.wins))
		print('Losses: ' + str(self.losses))
		print('Ties: ' + str(self.ties))
