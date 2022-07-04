import random
from wsgiref.validate import InputWrapper

while True:
	choices = ["rock", "paper", "scissors"]

	computer = random.choice(choices)
	player = None

	while player not in choices:
		player = input("rock, paper or scissors? ").lower()

	if player == computer:
		print("player: ",player)
		print("computer: ",computer)
		print("Tie!")

	elif player == "rock":
		if computer == "paper":
			print("player: ",player)
			print("computer: ",computer)
			print("You Lose!")
		if computer == "scissors":
			print("player: ",player)
			print("computer: ",computer)
			print("You Win!")

	elif player == "paper":
		if computer == "rock":
			print("player: ",player)
			print("computer: ",computer)
			print("You win!")
		if computer == "scissors":
			print("player: ",player)
			print("computer: ",computer)
			print("You lose!")

	elif player == "scissors":
		if computer == "paper":
			print("player: ",player)
			print("computer: ",computer)
			print("You Win!")
		if computer == "rock":
			print("player: ",player)
			print("computer: ",computer)
			print("You Lose!")
	play_again = input("play again? (y/n)")

	if play_again != "y":
		break
print("Gg")