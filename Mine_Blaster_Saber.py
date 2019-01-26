#Appetizer: Variables
human_selection = ""
human_name = ""
human_win = 0
computer_selection = ""
computer_name = ""
computer_win = 0
tie = 0
list = (["MINE", "SABER", "BLASTER"])
name_list = (["Han Solo", "Darth  Vader", "Luke Skywalker", "Leia Organa", "Jyn Erso", "Padme Amidala", "Greedo", "Boba Fett", "Captain Phasma", "Aayla Secura"])

#Side Dish: The Setup
import random

print ("Welcome to Star Wars Rock, Paper, Scissors. Otherwise known as: Mine, Saber, Blaster. \n You'll be playing against a random Star Wars character. \nEnter \'QUIT\' to leave the game and remember:\nMINE > SABER \nSABER > BLASTER \nBLASTER > MINE")

human_name = input("What is your name? ")
computer_name = random.choice(name_list)
print ("Hello {0}, you are now playing against {1}. May the Force be with you!".format(human_name, computer_name))

#Main Course: Steak
while human_selection != "QUIT":
	human_selection = input("Choose your weapon: ")
	human_selection = human_selection.upper()
	if (human_selection.isalpha() and human_selection != "") and (human_selection != "QUIT" or human_selection != "quit" or human_selection != "Quit"):
		print ("Your Selection: " + human_selection)
		computer_selection = random.choice(list)
		print ("{0} Selection: ".format(computer_name) + computer_selection)
		if human_selection == computer_selection:
			tie = tie + 1
			print ("It's a tie...fighter!")
			print ("{0}: {1}, {2}: {3}, Tie: {4}".format(human_name, human_win, computer_name, computer_win, tie))
		else:
			if (human_selection == "MINE" and computer_selection == "SABER") or (human_selection == "SABER" and computer_selection == "BLASTER") or (human_selection == "BLASTER" and computer_selection == "MINE"):
				human_win = human_win + 1
				print ("{0} wins!".format(human_name))
				print ("{0}: {1}, {2}: {3}, Tie: {4}".format(human_name, human_win, computer_name, computer_win, tie))
			else:
				computer_win = computer_win + 1
				print ("{0} wins!".format(computer_name))
				print ("{0}: {1}, {2}: {3}, Tie: {4}".format(human_name, human_win, computer_name, computer_win, tie))
	else:
		print ("Invalid selection entered. Please try again you scruffy-looking nerf herder.")