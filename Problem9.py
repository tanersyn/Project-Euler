# İki sayının karesinin toplamları bir sayının karesine eşit olan sayıları bulunmalı ve 3 sayının toplamı 1000 olmalı.
# Bu üç sayıyı nedir? 
def Bul():
    maksimum = 1000
    for a in range(1,maksimum+1):
        for b in range(a+1,maksimum+1):
            c = maksimum - a - b
            if a * a + b * b == c * c:
                return str(a * b* c)
print(Bul())