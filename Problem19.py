import datetime

baslangıc_tarihi = 1901
bitis_tarihi = 2001
pazar = 0

for sene in range(baslangıc_tarihi,bitis_tarihi): # Senelerde döngü
    for ay in range(1,13): # Aylarda döngü
        tarih = datetime.datetime(sene,ay,1) # tarih değişkeni sene 1901 ,ay 1, gün ise 1 aldık
        gun = (tarih.strftime("%A")) # datetime modülü ile "strftime("%A")" ile tarih değişkenin hangi güne ait olduğunu bulduk
        if gun == "Sunday":  # Gün değişkeni artık pazara eşitse koşul sağlanır
            pazar = pazar + 1 # Pazarları saydırdık
            print(tarih) # Hangi seneden hangi ayda ayın 1'i pazara denk geliyorsa yazdır
print(pazar)