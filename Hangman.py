import random	# for getting random word in txt file

# display() function does most of the work of the program
def display():

	# Opens the text file of words and picks a random word for the hangman game then closes it
	f = open('hangmanWords.py', 'r')
	lines = f.read().splitlines()
	completeWord = random.choice(lines)
	f.close()
	
	# misses variable is a string that appends and displays wrong guesses
	# word is a list which displays correct gueses so far
	# repeat is a boolean which checks for duplicate guesses 
	# finished is a boolean which ends the program when the word is complete
	misses = ""
	word = ['_','_','_','_','_','_','_']
	repeat = False
	finished = False
	
	# While loop for getting user input and printing the display
	while (len(misses) < 6 and finished == False):
	
		letter = input("Enter next character (A-Z), or 0 (zero) to exit: ")
		letter = letter.lower()
		repeat = False
		
		# for loops to check whether input was already guessed
		for l in word:
			if l == letter:
				repeat = True
		for l in misses:
			if l == letter:
				repeat = True
			
		# If user enters '0' break out of while loop which ends the program
		if (letter == '0'):
			break
		
		# If user made an invalid input
		elif (repeat == True or len(letter) != 1 or letter.isalpha() == False):
			print("INVALID INPUT")
	
		# If user makes a wrong guess
		elif(checkWord(letter,completeWord) == False):
			misses += letter
			print("Wrong")
			
		# If user makes a correct guess
		else:
			for i in range(7):
				if (completeWord[i] == letter):
					word[i] = letter
			print("Correct")
			
		# Print display based on how many wrong guesses
		if (len(misses) == 0):
			print("\n  |-----|   Word:", end=" ")
			for letter in word:
				print(letter, end=" ")
			print("\n  |	|\n  	|   Misses:" + misses)
			print("  	|\n  	|\n  	|\n  	|")
			print("---------")
			
		elif (len(misses) == 1):
			print("\n  |-----|   Word:", end=" ")
			for letter in word:
				print(letter, end=" ")
			print("\n  |	|\n  O	|   Misses:" + misses)
			print("  	|\n  	|\n  	|\n  	|")
			print("---------")
			
		elif (len(misses) == 2):
			print("\n  |-----|   Word:", end=" ")
			for letter in word:
				print(letter, end=" ")
			print("\n  |	|\n  O	|   Misses:" + misses)
			print("  |	|\n  |	|\n  	|\n  	|")
			print("---------")
			
		elif (len(misses) == 3):
			print("\n  |-----|   Word:", end=" ")
			for letter in word:
				print(letter, end=" ")
			print("\n  |	|\n  O	|   Misses:" + misses)
			print(" \|	|\n  |	|\n  	|\n  	|")
			print("---------")
			
		elif (len(misses) == 4):
			print("\n  |-----|   Word:", end=" ")
			for letter in word:
				print(letter, end=" ")
			print("\n  |	|\n  O	|   Misses:" + misses)
			print(" \|/	|\n  |	|\n  	|\n  	|")
			print("---------")
			
		elif (len(misses) == 5):
			print("\n  |-----|   Word:", end=" ")
			for letter in word:
				print(letter, end=" ")
			print("\n  |	|\n  O	|   Misses:" + misses)
			print(" \|/	|\n  |	|\n / 	|\n  	|")
			print("---------")
			
		# If there are 6 wrong guesses then the game is lost and continuePlaying() function is called
		elif (len(misses) == 6):
			print("\n  |-----|   Word:", end=" ")
			for letter in word:
				print(letter, end=" ")
			print("\n  |	|\n  O	|   Misses:" + misses)
			print(" \|/	|\n  |	|\n / \	|\n  	|")
			print("---------")
			print("You lose - out of moves")
			continuePlaying()
		
		# Checks if word has been guessed and calls continuePlaying() function if it has	
		t = ""
		for letter in word:
			t = t + letter
		if (completeWord == t):
			print("Congratulations - you win!")
			continuePlaying()
			finished = True
			
			
# continuePlaying() function asks the user whether he wants to play another game.
# If user enters 'y', the main() function is called to restart the program.
# If user enters 'n' the program ends
def continuePlaying():
	x = input("Would you like to continue playing?(Y/N): ")
	if x.lower() == 'y':
		main()
		
	
# checkWord function takes two arguments. One is a letter and the other is  a word
# The function checks whether the letter is contained in the word and returns true or false.
def checkWord(letter,word):
	for x in word:
		if letter == x:
			return True
	return False

# main() function welcomes the user and calls the display() function
def main():
	print("Welcome to Hangman!\n")
	display()
	
	
if __name__ == "__main__":
	main()