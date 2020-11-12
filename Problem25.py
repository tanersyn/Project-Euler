"""
İlk 3 basamaklı fibonacci sayısı 12. sıradadır.
İlk 1000 basamaklı fibonacci sayısı kaçıncı sıradır? 
"""
a = 1
b = 1
step = 2
while True:
    a,b = b,a + b
    step += 1
    if(len(str(b)) == 1000):
        print("Sayi:",b)
        print("İndex:",step)
        break