a = int(input("Podaj pierwsza liczbe: "))
b = int(input("Podaj druga liczbe: "))
print('Wejscie', a, ', ', b)
if a > b:
    (a,b)=(b,a)
while a <= b:
    if a % 2 == 1:
        a+=1
        continue
    print(a, end=' ')
    a += 1
