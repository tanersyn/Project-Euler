# 10'un altındaki asallar sayıların toplamı 2 + 3 + 5 + 7 = 17 olduğuna göre 
# 2 Milyonun altındaki asal sayıların toplamı nedir?  
toplam = 0
for sayi in range(1,2000000):
    if sayi > 1:
       for i in range(2,sayi):
           if (sayi % i) == 0:
               break
       else:
           toplam += sayi
print("Toplam :",toplam)