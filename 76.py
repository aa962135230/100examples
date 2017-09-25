if __name__ =='__main__':
	x = int(input('please input your number'))
	sum = 0
	if x%2 == 0:
		for i in range(2,x+1,2):
			sum += 1/i
			
	elif x%2==1:
		for i in range(1,x//2+1):
			sum += 1/(i*2+1)
	else:
		print('you\'re wrong')
		
	print(sum)