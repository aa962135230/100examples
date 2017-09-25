a=100
b=209
c=150


def swap(e,f):
	return f,e
	
if a>b:
	a,b = swap(a,b)
if b>c:
	b,c = swap(b,c)
if a>c:
	a,c = swap(a,c)
	
	
print(a,b,c)