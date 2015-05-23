import random

def num_guess():
	print("Guess a number between 1 and 100 inclusive.")
	randNum = random.randint(1,100)
	counter = 0 
	while True:
		try:
			numGuess = int(input("> "))
		except:
			print("Please enter an integer.")
			break
		counter += 1
		if numGuess < 1 or numGuess > 100:
			print('Please enter a valid number between 1 and 100 inclusive.')
			break
		elif numGuess == randNum:
			print("Congrats, you guessed the number {} correctly in {} guess(es)!".format(randNum, counter))
			break
		elif numGuess < randNum:
			print("Your guess was too low. Please try again!")
			continue
		elif numGuess > randNum:
			print("Your guess was too high. Please try again!")
			continue

num_guess()
