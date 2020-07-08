# İlk yüz doğal sayının karelerinin toplamı ile toplamın karesi arasındaki farkı bulun.

kareler = []
toplam = 0
toplam2 = 0

# 1-200 arası sayıların karesi
for index in range(101):
    kareler.append(index**2)

print(kareler)

# 1-200 arası sayıların karelerinin toplamı
for index in kareler:
    toplam += index

print('Toplam :',toplam)

# 1-200 arası sayıların toplamı
for index in range(101):
    toplam2 += index

print('Toplam:',toplam2)

# 1-200 arası toplanan sayıların karesi
print(toplam2**2)

print('Arlarındaki Fark :',(toplam2**2) - (toplam))