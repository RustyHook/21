import random

#There are two types of scores: the game score and the round score
#The game score will begin at 100, and the game will last for five rounds
maxScore = 100
gameScore = 0
roundScore = 0

maxRounds = 5 
roundCounter = 0 

#Card values and their names(for displaying purposes)
deck = [["Ace", "Two", "Three", "Four", "Five", "Six", \
	 "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King"], \
	[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]] 

cardCount = 12 

card1 = 0 
card2 = 0 

choice = ""
decision = ""

def newGame():
##Reset the variables for a clear start of a new game
	gameScore = 100 
	roundCounter = 0 
	
			
	#while True:
	#	choice = input(": ").lower
	#	if choice == "n":
	#		print ("")
	#		print ("Good Luck!!!")
	#		print ("")
	#		break
	#	elif choice == "Q" or choice == "q":
	#		roundCounter = 5 
	#		break
	#	


	while roundCounter < maxRounds:
		roundScore = 0  
		deck = [["Ace", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King"], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]] 
		cardCount = 12 
		print ("~~~~~~~~~~~~~~~~~~~~~~~~")
		print ("")
		print ("Game score: " + str(gameScore) + " Round: " + str(roundCounter+1) + "/5  | press Q to exit")
		print ("")

	##Draw the first two cards and remove them from the deck
		draw1 = random.randint(1,cardCount)
		card1 = deck[1][draw1]
		del deck[1][draw1]
		cardCount -= 1	

		draw2 = random.randint(1,cardCount)
		card2 = deck[1][draw2]
		del deck[1][draw2]
		cardCount -= 1
		
		roundScore = card1 + card2 
		
		print ("You have drawn: ")
		print (deck[0][draw1])
		del deck[0][draw1]

		print (deck[0][draw2])
		del deck[0][draw2]
		print ("")
		print ("Your current score is: " + str(roundScore)) 


	##Let user decide if he wants another card, til he busts or decides to stop
		
		while True:
			print ("")
			decision = input("Do you want to draw another card?(Otherwise round will end) [y/n]").lower()
			if decision == "y":
				draw = random.randint(1,cardCount)
				card = deck[1][draw]
				del deck[1][draw]
				cardCount -= 1
				roundScore += card
				print ("")
				
				print ("You have drawn: " + deck[0][draw])
				del deck[0][draw]
				print ("")
				print ("Your current score is: " +str(roundScore))
				
				if roundScore > 21:
					print ("")
					print ("You bust!!! -21pts")
					gameScore -= 21
					break
				elif roundScore == 21:
					print ("")
					print ("Blackjack!!! Perfect!!! -0pts")
					break 
				
			elif decision == "n":
				gameScore -= 21-roundScore
				print ("")
				print ("Round " + str(roundCounter+1) + " is over! Your current game score is: " + str(gameScore))
				print ("")
				break
			elif decision == "q" or decision == "Q":
				print ("Good Bye ^_^ ")
				roundCounter = 99
				break
		roundCounter += 1 
	print ("~~~~~~~~~~~~~~~~~~~~~~~~")

	if choice != "q" and choice != "Q" and roundCounter != 99:
		print ("Your final score is: " + str(gameScore))

	if gameScore >= 90 and gameScore < 100:
		print ("Your rank: A")
	elif gameScore >= 80 and gameScore < 90:
		print ("Your rank: B")
	elif gameScore >= 70 and gameScore < 80:
		print ("Your rank: C")
	elif gameScore >= 60 and gameScore < 70:
		print ("Your rank: D")
	elif gameScore >= 50 and gameScore < 60:
		print ("Your rank: F")
	elif gameScore == 100:
		print ("Godspeed!")
	else:
		print ("Git gud!!!")
	
	return

print ("Welcome to 21 !!!")
print ("~~~~~~~~~~~~~~~~~~~~~~~~")
	
newGame() 

while True:
	if choice == "Q" or choice == "q" or decision == "q" or decision == "Q":
		break	
	print ("")

	new_game = input("Do you want to play another one? [Y/N]")
	if new_game == "Y" or new_game == "y":
		newGame() 
	elif new_game == "N" or new_game == "n":
		print ("Good Bye ^_^")
		break 	
