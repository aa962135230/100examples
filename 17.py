s = input('请输入你的字符串：')

letters = 0
space = 0
number = 0
other = 0

for x in s:
	if x.isalpha():
		letters += 1
	elif x == ' ':
		space += 1
	elif x.isdigit():
		number += 1
	else:
		other += 1

print('字母的个数为%d' % letters)
print('空格的个数为%d' % space)
print('数字的个数为%d' % number)
print('其他的个数为%d' % other)



