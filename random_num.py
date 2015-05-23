import random

def num_guess():
	print("Guess a number between 1 and 100 inclusive.")
	randNum = random.randint(1,100)
	counter = 0 
	while True:
		numGuess = int(input("> "))
		counter += 1
		if numGuess == randNum:
			print("Congrats, you got the answer correct in {} guess(es)!".format(counter))
			break
		elif numGuess < randNum:
			print("Your guess was too low. Please try again")
			continue
		elif numGuess > randNum:
			print("Your guess was too high. Please try again")
			continue

num_guess()
