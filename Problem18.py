"""
Aşağıdaki üçgenin üstünden başlayıp aşağıdaki satırdaki bitişik sayılara geçerek,üstten alta doğru maksimum toplam 23 olur.
											    3
		   						   			   7 4
		  						  			  2 4 6
								 			 8 5 9 3
Yani ; 3 + 7 + 4 + 9 = 23 elde edilir.
Bu bilgiye göre aşağıdaki üçgenin üstten alta doğru maksimum toplamını bulun;
												75
											  95 64
											 17 47 82
										    18 35 87 10
										   20 04 82 47 65
									  	  19 01 23 75 03 34
									     88 02 77 73 07 63 67
								        99 65 04 28 06 16 70 92
								       41 41 26 56 83 40 80 70 33
                       		          41 48 72 33 47 32 37 16 94 29
							         53 71 44 65 25 43 91 52 97 51 14
						            70 11 33 28 77 73 17 78 39 68 17 57
						           91 71 52 38 17 14 91 43 58 50 27 29 48
					              63 66 04 68 89 53 67 30 73 16 69 87 40 31
					             04 62 98 27 23 09 70 98 73 93 38 53 60 04 23								
"""

sayi = """75
95 64
17 47 82
18 35 87 10
20 4 82 47 65
19 1 23 75 3 34
88 2 77 73 7 63 67
99 65 4 28 6 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 4 68 89 53 67 30 73 16 69 87 40 31
4 62 98 27 23 9 70 98 73 93 38 53 60 4 23"""
# Boşluklarına göre ayırdık
sutunlar = sayi.split("\n")
liste = list()
# Ayırdığımız her sayıyı listeye attık
for sutun in sutunlar: 
	sayilar = sutun.split(" ")
	liste.append(sayilar)
# Listedeki her sayıyı int hale getirdik artık üçgen tamamen tamsayı biçiminde
for i in range(0,len(liste)):# i boyunu dönmesini sağlıyor
	for j in range(0,i+1):# j indeks 
		liste[i][j] = int(liste[i][j])# Listenin her bir i. ve j. elemanını int biçimine getir
# Ucgen formunun alt kısmından gelerek en büyük toplamı bulmaya yarar
for i in range(len(liste)-1,-1,-1):# Listenin boyu kadar dön,-1'e kadar(yani 0. indeksi dahil et),tersten gittiği için -1
	for j in range(0,i):# İndeksin boyu kadar dön
		liste[i-1][j] += max(liste[i][j],liste[i][j+1]) 
print("Dizinin Gidişatı: ",liste)
print("Sonuç :",liste[0])# Listenin 0. indeksi çünkü tüm toplamların maksimumu orada bulunuyor.