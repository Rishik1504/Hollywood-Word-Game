'''
Created by: Rishik Sood
Date: 25 May 2018
Language: Python3


This is a program that simulates hangman-like game. The program
randomly chooses a movie from the given database. The user has 
to guess the letters in the movie apart from the vowels. User 
has as many turns there are in the word "HOLLYWOOD" (i.e. 9).

Database Credits: http://blog.joelberghoff.com/wp-content/uploads/2015/12/1990-2015-movie-titles.txt
'''

from random import choice

def choose_movie():

	'''
	Reads the database and randomly chooses  and returns 
	a movie for the user to guess.
	'''

	all_movies_file = open("all_movies.txt", 'r')
	all_movies_list = all_movies_file.readlines()
	for i in range(len(all_movies_list)):
		all_movies_list[i] = all_movies_list[i].replace('\n', '')
	all_movies_file.close()
	return list(choice(all_movies_list))

def valid_letter(letter, chosen_letters):

	'''
	Checks the two primary conditions for an input to
	be valid:
	1) The input should only be a letter and not a number/symbol/word.
	2) The input should not be chosen before.
	'''

	if not letter.isalpha() or len(letter) > 1:
		print("Please enter only a letter.")
		return False

	if letter in chosen_letters:
		print ("Please choose another letter.")
		return False

	return True

def initialize_guesses(movie):
	
	'''
	Initializes the initial list that would contain the hidden movie.
	If the letter on the ith index is a not a vowel, then it is
	hiddden until the user guesses it correctly.
	'''

	temp = []
	
	for i in movie:
		if i in 'aeiou ':
			temp.append(i)	
		else:
			temp.append('_')

	return temp

def result(final_guesses, movie):

	'''
	Checks if the user has won or lost the game and returns the 
	result.
	'''

	if ''.join(final_guesses) == ''.join(movie):
		return ''.join(movie)+"\nYou win! :-D"
	else:
		return 'You lose! :-(\n' + "The movie was " + ''.join(movie)

def run(movie):

	'''
	Main loop where the game actually runs.
	''' 

	chosen_letters = {'a', 'e', 'i', 'o', 'u'}
	ctr = 0
	guesses_left = list("HOLLYWOOD")
	guess_list = initialize_guesses(movie)

	while ''.join(guess_list) != ''.join(movie):

		print("--------------------------------------------------------")
		print(''.join(guesses_left))
		if ctr == len(guesses_left):
			break
		print(' '.join(guess_list))

		guess = input("Enter your guess: ").lower()

		if not valid_letter(guess, chosen_letters):
			continue
		else:
			chosen_letters.add(guess)

		if guess not in movie:
			guesses_left[ctr] = guesses_left[ctr] + '\u0336'
			ctr += 1
			continue

		for i in range(len(movie)):
			if guess == movie[i]:
				guess_list[i] = guess

	print(result(guess_list, movie))

if __name__ == "__main__":
	movie = choose_movie()
	run(movie)