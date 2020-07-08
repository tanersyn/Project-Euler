# 10' un altında 3 VEYA 5'in katları olan tüm doğal sayıları listelersek [3,5,6,9] ve toplamları 23 olur.
# 1000'in altındaki 3 VEYA 5'in tüm katlarının toplamlarını bul

toplam = 0

for index in range(1000):
    if (index % 3 == 0 or index % 5 == 0):
        toplam += index

print('Toplam:',toplam)