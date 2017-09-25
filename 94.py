import time
import random


playit = input('do you want to play it?')
while playit == 'y':
	c = input('input a character:')
	i = random.randint(0,2**32)%100
	print('input your number:')
	start = time.clock()
	a = time.time()
	guess = int(input('input your number:'))
	while guess != i:
		if guess >i:
			print('please input a smaller number')
			guess = int(input('input your number'))
		else:
			print('please input a bigger number')
			guess = int(input('input your number'))
	end = time.clock()
	b = time.time()
	var = (end-start)/18.2
	print(var)
	if var<15:
		print('how clever')
	if var<25:
		print('how normal')		
	if var<15:
		print('how stupid')		
	print('congratulations')
	print('the num you guess is %d'%i)
	playit= input('do you wantto play it')
			