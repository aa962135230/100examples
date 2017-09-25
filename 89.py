a = '1234'
c = []

for i in range(4):
	b = int(a[i])
	b += 5
	b = b%10
	c.append(b)
	
for i in range(2):
	c[i],c[3-i]=c[3-i],c[i]

print(c[0]*1000+c[1]*100+c[2]*10+c[3])