if __name__=='__main__':
	a = [5,9,3]
	b = [8,2,6]
	
	print(a)
	print(b)
	a.sort()
	print(a)
	print(a+b)
	a.extend(b)
	print(a)