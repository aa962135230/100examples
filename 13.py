
a = []

for i in range(1,10):
	for j in range(0,10):
		for k in range(0,10):
			if i*100+j*10+k == i*i*i+j*j*j+k*k*k:
				
				a.append(i*100+j*10+k)
				
print(a)