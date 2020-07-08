# 13195'in asal çarpanları 5,7,13 ve 29'dur
# 600851475143 sayısının en büyük asal çarpanı nedir?

i = 2
sayı = 600851475143 
liste=[]

while i < sayı:
    
    if sayı % i == 0:

        sayac = 0

        for j in range(2,i):
            if (i % j == 0):
                sayac +=1
                break

        if (sayac != 0):
            print('Asal Değil')
        else:
            print('Asal')

        print(i)
        liste.append(i)

    i += 1