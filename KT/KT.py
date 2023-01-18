from random import *

#1
print("1 Ülesanne")
a='(\_/)'
b="(o o)"
c="/ | \*"
n = input("Number 1 kuni 9 ")
while n.isdigit()==False or (int(n)==0 or int(n)>9):
    n=input("Vale! Number 1 kuni 9! ")
n=int(n)
for i in range(1,int(n)+1):
    print(a * n, end=" ")
    print("\n")
    print(b * n, end=" ")
    print("\n")
    print(c * n, end=" ")
    print("\n")
#2
print("2 Ülesanne")
a=0
L = input("Number 1 kuni 14 ")
while L.isdigit()==False or (int(L)==0 or int(L)>14):
    L=input("Vale! Number 1 kuni 14! ")
for i in range(0,int(L)+1):
    a+=i
    print(a)
print()

#3
print("3 Ülesanne")
x = randint(1,100)
for i in range(1,11):
    num=input("Number 1 kuni 100 ")
    while num.isdigit()==False or int(num)>100:
        num=input("Vale! Number 1 kuni 100 ")
    num=int(num)
    if num>x:
        print("Peidetud arv on väiksem!")
    elif num<x:
        print("Peidetud number on rohkem!")
    else:
        print("Õigesti!")
        break
if i==10:
    print(f"Sa ei suutnud! Arv oli - {x}")
print()

#4
print("4 Ülesanne")
b=0
a = input("Kirjutage number ").replace("-","",1)
while a.isdigit()==False:
    a = input("Vale! Kirjutage number ")
a=int(a)
while a > 0:
    number = a % 10
    a = a // 10
    b = b * 10
    b +=number 
print("Ümberpööratud arv", b)
print()

#5
x=1
x1=0
print("5 Ülesanne")
a = input("Kirjutage number ")
while a.isdigit()==False:
    a = input("Vale! Kirjutage number ")
a=int(a)
while a>0:
    n = a % 10
    a = a // 10
    x*=n
    x1+=n
print(f"Summa - {x1}, Arvude korrutis - {x}")