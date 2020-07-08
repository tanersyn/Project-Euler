#Asal sayıları sırasıyla yazarsak; 2,3,5,7,11 ve 13. Burada 6. indeksteki eleman 13 tür
#Buna göre 10 001. asal eleman nedir?
 
asallar = []
toplam = 0

for sayi in range(1,104745):
    if sayi > 1:
        for i in range(2,sayi):
            if (sayi % i) == 0:
                break
        else:
            asallar.append(sayi)

sonuç_listesi=asallar[::-1]
index = len(asallar)
print('İndex :',index)
print('Sonuç :',sonuç_listesi[0])
#print('Arasındaki asallar:',asallar) --> Aralarındaki asal sayıları görmek istersek
#104745 sayısı deneyerek bulunabilir