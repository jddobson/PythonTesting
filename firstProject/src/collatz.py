def run():
	val = int(input())

	while(val > 1):
		val = compute(val)

def compute(value):
	if(isEven(value)):
		value = value // 2
		print(value)
		return value
	else:
		value = 3 * value + 1
		print(value)
		return value

def isEven(value):
	if(value % 2 == 0):
		return True
	else: 
		return False