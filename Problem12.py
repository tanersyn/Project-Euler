"""Üçgensel sayı dizileri ardışık doğal sayıların toplanmasıyla üretilir. Örneğin 7. üçgensel sayı 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28’dir. İlk 10 üçgensel sayı şöyledir:
1, 3, 6, 10, 15, 21, 28, 36, 45, 55, …
Şimdi ilk 7 üçgensel sayının bölenlerini listeleyelim:
1: 1
3: 1,3
6: 1,2,3,6
10: 1,2,5,10
15: 1,3,5,15
21: 1,3,7,21
28: 1,2,4,7,14,28
Burada 28 sayısının, 5 taneden fazla bölene sahip ilk üçgensel sayı olduğunu görüyoruz.
Peki 500’den fazla bölene sahip ilk üçgensel sayı kaçtır?"""
 
import math
import time
baslangıc = time.time()
def bolen_sayisi(x):
    bolen = 1    
    for i in range(2,int(math.sqrt(x)+1)):
        if(x % i == 0):
            bolen += 1
    return bolen * 2

n = 1
while True:
    sayi = (n*(n + 1))/2
    if bolen_sayisi(sayi) > 500:
        print("Sonuc: ",int(sayi))
        break
    n += 1
bitis = time.time()
print(round((bitis - baslangıc),2),"saniye surdu")