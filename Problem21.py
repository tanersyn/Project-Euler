"""d(n), n’in tam bölenlerinin toplamı olarak tanımlansın.
a ≠ b iken, eğer d(b) = a ve d(a) = b oluyorsa, a ve b bağdaşık sayı olarak adlandırılır.

Örneğin, 220’nin tam bölenleri 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 ve 110’dur; O zaman d(220) = 284.
284’ün tam bölenleri 1, 2, 4, 71 ve 142 ‘dir; O zaman d(284) = 220.

10000’den küçük tüm bağdaşık sayıların toplamını hesaplayın."""

def d(n):
    bolenler = []
    for i in range(1,n):
        if(n % i == 0):
            bolenler.append(i)
    return sum(bolenler)
liste = []
for i in range (1,10000):  
    a = i
    b = d(a)
    if ((d(a) == b) and (d(b) == a)):
        if(a != b):
            liste.append(a)
            print(a,"ve",b,"Dost Sayılardır")
print("10.000'den Küçük Tüm Bağdaşık Sayıların Toplamı :",sum(liste))