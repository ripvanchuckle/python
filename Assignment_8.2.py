# This is a header for the application
# You should read this header and insert your name and your date below as part of the peer review
# This is a typical part of any program
# Author: Michael Stout
# Creation Date: 21 Sep 2020
# Below is a simple program with 10 issues (some are syntax errors and some are logic errors.  
# You need to identify the issues and correct them.

import random
import time

def displayIntro():
	#print('''You are in a land full of dragons. In front of you,
	print('''
	You are in a land full of dragons. In front of you,
	you see two caves. In one cave, the dragon is friendly
	and will share his treasure with you. The other dragon
	is greedy and hungry, and will eat you on sight.''')
	print()
	# 1 - Correction is merely formatting, to make output look 'nicer'

def chooseCave():
    #cave = ''
	cave = []
	# 2 - need brackets to create an empty list
	while cave != '1' and cave != '2':
	#print('Which cave will you go into? (1 or 2)')
		print("Which cave will you go into? 1 or 2? ")
	# 3 - Remove single quotes and interior parentheses
		cave = input()
	#
	#return caves
	return cave
	# 4- misspelled item

def checkCave(chosenCave):
	print('You approach the cave...')
	#sleep for 2 seconds
	time.sleep(2)
	print('It is dark and spooky...')
	#sleep for 2 seconds
	#time.sleep(3)
	time.sleep(2)
	# 5 - Previous line was to sleep 3 seconds, rather than indicated 2 seconds
	print('A large dragon jumps out in front of you! He opens his jaws and...')
	print()
	#sleep for 2 seconds
	time.sleep(2)
	friendlyCave = random.randint(1, 2)

	#if chosenCave == str(friendlyCave):
	if friendlyCave == 1:
	# 6 - attempting to use "string" when random is for "integer" - fails comparison
		print('Gives you his treasure!')
	else:
		#print 'Gobbles you down in one bite!'
		print('Gobbles you down in one bite!')
		# 7 - added parentheses 

def main():
# 8 - Needed to add to actually allow program to run at beginning
	playAgain = 'yes'
#	while playAgain = 'yes' or playAgain = 'y':
	while playAgain == 'yes' or playAgain == 'y':
	# 9 - Comparison operators were incorrect
		displayIntro()
		#caveNumber = choosecave()
		caveNumber = chooseCave()
		# 10 - Incorrect object name
		checkCave(caveNumber)
    
		print('Do you want to play again? (yes or no)')
		playAgain = input()
		if playAgain == "no":
			#print("Thanks for planing")
			print("Thanks for playing")
			# 11 - Misspelled word...planing instead of playing
main()
# 12 - Complete the 'main' definition

