b = int(input('input your number:'))
a = 9
n = 1
while(1):
	if a%b==0:
		break
	else:
		a=a*10+9
		n =n + 1
print('%d 9 / %d integer'%(n,b))