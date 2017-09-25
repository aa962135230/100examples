n = 1
while n<=7:
	a = int(input('your num is :'))
	while a<1 or a>50:
		a = int(input('your num is :'))
	print(a*'*')
	n += 1