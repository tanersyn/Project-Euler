"""Aşağıdaki tekrarlama dizisi pozitif tam sayılar için tanımlanmıştır:
n → n/2 (n çift)
n → 3n + 1 (n tek)
Yukarıdaki kuralı uygulayarak ve 13’ten başlayarak aşağıdaki diziyi üretiriz:
13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
13’ten başlayıp 1’de sonlanan bu dizinin 10 adet terim içerdiği görülebilir. Henüz kanıtlanmış olmasa da(Collatz Problemi), bütün başlangıç sayılarının 1’de sonuçlanacağı sanılmaktadır.
Bir milyonun altındaki hangi başlangıç sayısı, en uzun zinciri üretir?
NOT: Zincir bir kere başladıktan sonra terimlerin 1 milyonun üzerine çıkabilmesi mümkündür."""

import time
def calculate(x):
    if (x % 2 == 0):
        return (x /2)
    else:
        return ((3 * x) + 1)
def steps(x):
    step = 1
    while True:
        x = calculate(x)
        step += 1
        if (x == 1):
            return step

max_steps = 0
champ_number = 0

start = time.time()
for number in range(1,1000001):
    temporary_variable = steps(number)
    if(temporary_variable > max_steps):
        max_steps = temporary_variable
        champ_number = number
finish = time.time()
print("The number which produce longest:",champ_number)
print("The longest chain:",max_steps)
print("Program has finished :",str(finish - start))