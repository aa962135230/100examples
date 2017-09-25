a = '122'
c = 0

for i in range(1,4):
	c = c + (8**(i-1))*int(a[4-i-1])
	
print(c)