person = {"li":18,"wang":50,"zhang":20,"sun":22}
m = 'li'

for key in person.keys():
	if person[key]>person[m]:
		m = key
		
print('%s age is :%d'%(m,person[m]))