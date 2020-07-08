# Fibonacci Serisinde 4 milyonu aşmayacak şekilde oluşan çift sayıların toplamını bulan program
def hesapla():

    cevap = 0
    x = 1
    y = 2

    while (x < 4000000):
        if (x % 2 == 0):
            cevap += x

        x,y = y, x+y

    return print('Fibonacci Serisi İçerisindeki Çift Sayıların Toplamı :',cevap)

if __name__ == "__main__":
	print(hesapla())