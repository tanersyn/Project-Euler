from math import factorial
def fonksiyon(n,k):
    return factorial(n)/(factorial(k)*factorial(n-k))
print ('Kafes yolunun sayısı: '+ str(fonksiyon(40,20)))