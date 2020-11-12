# 2 üzeri 15 = 32768 ve sonucun elemanları toplamı; 3 + 2 + 7 + 6 + 8 = 26 ise
# 2 üzeri 1000 sayısının elemanları toplamı kaçtır? 

sayi=pow(2,1000)
sayi=str(sayi)
toplam=0
for rakam in sayi:
    toplam+=int(rakam)
print("Toplam:",toplam)