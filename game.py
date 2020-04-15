import random


words_list = ('автострада', 'бензин', 'инопланетянин', 'самолет', 'библиотека',
             'шайба', 'олимпиада')

secret_word = random.choice(words_list)


gamer_world = ['*'] * len(secret_word)

errors_counter = 0

while True:
	letter = input('Input your letter: ')
	if len(letter) != 1:
		continue
	if letter in secret_word:
		for idx, symbol in enumerate(secret_word):
			# print(idx, symbol)
			if symbol == letter:
				gamer_world[idx] = letter
		if '*' not in gamer_world:
			print('You win!!!')
			break
	else:
		errors_counter += 1
		print(f'Errors number: {errors_counter}')
		if errors_counter == 8:
			print('You Lose:(')
			break
	print(''.join(gamer_world))