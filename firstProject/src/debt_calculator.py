class DebtCalculator(accounts):
	"""docstring for DebtCalculator"""
	def __init__(self, accounts):
		super DebtCalculator, self.__init__()
		self.accounts = accounts
		

	def printAccounts(accounts):
		print()
		print('Chase Sapphire: ' + sapphire)
		print('Chase Freedom: ' + freedom)

	def creditCardPayoff(amount, payment, interestRate):
		print('Balance: ' + str(amount)) 
		print('Payment: ' + str(payment))
		print('Interest Rate: ' + str(interestRate))

		month = 0



		while amount > 0:
			month += 1
			print()
			print('Month number: ' + str(month))
			print()
			interestCharge = (interestRate / 12 * amount)
			print('Interest Charge: ' + str(interestCharge))
			amount = amount + interestCharge
			amount = amount - payment
			print('Remaining Balance: ' + str(amount))

		
