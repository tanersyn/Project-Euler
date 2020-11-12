"""5 binin üzerinde ismi içeren 46KB’lık names.txt (sağ tıklayın ve ‘Hedefi farklı kaydet…’ ile indirin) dosyasını indirerek, alfabetik olarak sıralayın. Sonrasında isimlerdeki her bir harfin alfabetik sıra numarasını toplayarak, bu değeri ismin listedeki sıra numarasıyla çarpın ve ismin puanını bulun.
Örneğin, liste alfabetik olarak sıralandığında COLIN ismi 938. sırada olacaktır ve harflerinin toplam değeri 3 + 15 + 12 + 9 + 14 = 53 olacaktır. Böylece, COLIN, 938 × 53 = 49714 şeklinde bir puan alacaktır.
Dosyadaki tüm isim skorlarının toplamı nedir?"""
with open("names.txt") as f:# Dosyamızı okuyoruz
    isimler =  f.read()
liste = []
for i in sorted(isimler.split(",")):# Sıralı yazılmış ve virgül ile ayrılmış her satır
    liste.append(i.replace('"',r'')) # Her bir isim '' formatında yazılması amacıyla replace işlemi uyguladık
liste.insert(0,"") #İlk indeks boş ekledik

sonuc = []
for i in range(len(liste)): # for döngüsüyle her bir harfin sayısal değerini buluyoruz
    numbers = []
    letters = liste[i]
    for letter in letters:
        number = ord(letter) - 64
        numbers.append(number)    
    print(numbers)
    print(liste[i])

    toplam = 0
    j = 1
    for j in numbers: 
        toplam = toplam + j 
    print("Toplam :",toplam)
    print("Çarpım :",toplam * i) # Her bir toplamı indeksi ile çarpmamız gerekecek o yüzden i.index ile çarpıyoruz
    sonuc.append(toplam*i)
    print("-----------------------")
print("Sonuc:",sum(sonuc))