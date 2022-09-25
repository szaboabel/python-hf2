import math
#1
'''
n = int(input("n= "))
m = int(input("m= "))
if m != 0:
    if n%m==0:
        print("osztoja")
    else:
        print("nem osztoja")


#2
r = float(input("r= "))
kerulet = 2*r*math.pi
terulet = math.pi*r**2
print(f"A kerület=  {kerulet}")
print(f"A terület= {terulet}")



#3
n = int(input("n= "))
a = int(input("a= "))
b = int(input("b= "))

if a > n > b or a < n < b:
    print(f"{n} {a} és {b} között van")
elif n > a and b or n < a and b:
    print(f"{n} nincs {a} és {b} között")

#4
jegy = int(input("jegy: "))
if jegy == 5:
    print("jeles")
if jegy == 4:
    print("jó")
if jegy == 3:
    print("közepes")
if jegy == 2:
    print("elégséges")
if jegy == 1:
    print("elégtelen")
else: print("a jegy nem valid")  


#5
nap = str(input("Milyen nap van ma? "))
if nap == "hétfő":
    print("A hét 1. napja")
if nap == "kedd":
    print("A hét 2. napja")
if nap == "szerda":
    print("A hét 3. napja")
if nap == "csütörtök":
    print("A hét 4. napja")
if nap == "péntek":
    print("A hét 5. napja")
if nap == "szombat":
    print("A hét 6. napja")
if nap == "vasárnap":
    print("A hét 7. napja")

#6
befogo1 = int(input("befogo1= "))
befogo2 = int(input("befogo2= "))
atfogo_negyzet = befogo1**2 + befogo2**2

if atfogo_negyzet == befogo1**2 + befogo2**2:
    print("derékszögű")

#7
a = int(input("a= "))
b = int(input("b= "))
c = int(input("c= "))

if a-b<c:
    print("szerkeszthető")
else: print("nem szerkeszthető")


#8
a=float(input("a= "))
b=float(input("b= "))
c=float(input("c= "))
D=b**2-4*a*c

if D>0:
    print("2 gyök")
if D==0:
    print("1 gyök")
if D<0:
    print("nincs gyöke")


#9
ev=int(input("évszám: "))
if ev==0:
    print("nem valid évszám")
if ev != 0:
    if ev%4 == 0:
        print("ez az év szökőév")
    if ev%100 == 0:
        print("ez az év szökőév")
    if ev%4 != 0:
        print("ez az év nem szökőév")
'''


#10
n = int(input("n= "))
print(len(str(n)))