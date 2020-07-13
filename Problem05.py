# 2520, kalanlar olmadan 1'den 10'a kadar olan sayıların her birine bölünebilen en küçük sayıdır.
# 1'den 20'ye kadar olan tüm sayılarla eşit olarak bölünebilen en küçük pozitif sayı nedir?
cevap=0
sayi=1
while cevap==0:
    bolunebildigi_sayi_sayisi=0
    for i in range(1,21,1):
        if sayi%i==0:
            bolunebildigi_sayi_sayisi+=1
        else:
            break
    if bolunebildigi_sayi_sayisi==20:
        cevap=sayi
        sayi+=1
print(cevap)
