# 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800 ve indekslerinin toplamı ; 3 + 6 + 2 + 8 + 8 + 0 + 0
# Buna göre 100! sayısının indekslerinin toplamı nedir?

sayı = 100
sonuc = 1
for index in range(1,101):
    sonuc *= index

sonuc = str(sonuc)
toplam = 0
for rakam in sonuc:
    toplam += int(rakam)

print('Elemanlarının Toplamı :',toplam)