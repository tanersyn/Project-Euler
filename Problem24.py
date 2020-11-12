

from itertools import permutations

sayilar = permutations([0,1,2,3,4,5,6,7,8,9])
olusturulan_sayilar = []
for sayi in sayilar:
    olusturulan_sayilar.append(sayi)

sonuc = olusturulan_sayilar[999999]
print(sonuc)