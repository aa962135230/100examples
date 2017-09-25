#!/usr/bin/python3

def prime(n):
    l = []
    while n > 1:
        for i in range(2, n + 1):
            if n % i == 0:
                n = int(n / i)
                l.append(i)
                break    
    return l


s = input("输入一个正整数:")
if s.isdigit() and int(s) > 0:
    print(s, "=", "*".join([str(x) for x in prime(int(s))]))
else:
    print("请输入正确的正整数")