# -*- coding: utf-8 -*-
"""лаба1

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ef2VBuGG2rB2LGFByX2ZQ_edslREYphC
"""

a =  5 #1
b = int(input('b'))
print(a*b)



a = int(input('a')) #2
b = int(input('b'))
s = (a+b)**2
print(s)

a = 15 #3
b = 10
c = int(input('c'))
print((a+b)/c)

a = int(input('a'))#4
b = int(input('b'))
c = a**2+2*a*b+b**2
print(c)

a = int(input())#5
b = int(input())
c = int(input()) 
p1 = a+b+c
p2 = (a + b + c)/2
s = (p2 * (p2 - a) * (p2 - b) * (p2 - c)) ** 0.5
print(p1, s)

a = int(input()) #6
b = int(input())
print(((a**3+14)/5)*b)

a = int(input()) #7
n = int(input())
s = pow(a, 2)
d = s//n
print(d)

sec = int(input('Колличество секунд')) # 1 повышенная сложность
d = sec // 86400
h = sec//3600
m = sec // 60
print(d,h,m)

n = int(input("Введите число n: ")) # 2 повышенная сложность
zam = str(n)
a1 = zam + zam
a2 = zam + zam + zam
zam = n + int(a1) + int(a2)
print("Вывод:", zam)
