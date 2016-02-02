import random


maxScore = 100;
gameScore = 0;
roundScore = 0;

maxrounds = 5;
roundCounter = 0;

fullDeck = [["Ace", "Two", "Three", "Four", "Five", "Six", \
	 "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King"], \
	[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]];

deck = [["Ace", "Two", "Three", "Four", "Five", "Six", \
	 "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King"], \
	[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]];

card1 = 0;
card2 = 0;


def newGame():
##Reset the variables for a clear start of a new game
	gameScore = maxScore;
	roundScore = 0;
	roundCounter = 0;
	deck = fullDeck;
	
##Draw the first two cards and remove them from the deck
	draw1 = random.randint(1,13)
	card1 = deck[1][draw1]
	del deck[1][draw1]
	
	draw2 = random.randint(1,12)
	card2 = deck[1][draw2]
	del deck[1][draw2]
	
	roundScore = card1 + card2;
	
	print ("You have drawn: " + deck[0][draw1] + " and " + deck[0][draw2])
	print ("Your current score is: " + str(roundScore)) 
	decision = input("Do you want to draw another card?(Otherwise round will end) [y/n]")
	
	while True:
		if decision == "y" or decision == "Y":
			draw = random.randint(1,11)
			card3 = deck[1][draw]
			del deck[1][draw]
			roundScore += card3
			print ("You have drawn: " + deck[0][draw])
			print ("Your current score is: " +str(roundScore))
			
			
		
	return
	
newGame();	
