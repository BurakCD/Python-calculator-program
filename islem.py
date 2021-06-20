def toplama():
	toplam=0
	try:
		while True:
			a=input("Bir sayı giriniz:")
			if(a=="="):
				print("------------------------------------------------------")
				print("Cevap:",toplam)
				print("------------------------------------------------------")
				break
			elif(not a=="q" or a=="Q"):
				a=float(a)
				toplam+=a
				print("------------------------------------------------------")
				print("Sonuç:",toplam)
				print("------------------------------------------------------")
			elif(a=="q" or a=="Q"):
				print("Geri dönülüyor...")
				break
	except ValueError:
		print("Bir şey oldu.")
		print("Lütfen sayısal bir değer giriniz!")
""" Bu fonksiyon kullanıcıdan sürekli bir sayı ister ve her sayı girişinde bir önceki sayıyla yeni girilen 
sayıyı toplar ve her adımı gösterir, ta ki "=" işareti girilip cevap istenene kadar."""

def cikarma():
	try:
		while True:
			cikarma=input("Çıkarma yapılacak sayıyı giriniz:")
			if(not cikarma=="q"):
				cikarma=float(cikarma)
			elif(cikarma=="q" or cikarma=="Q"):
				print("Geri dönülüyor...")
				break
			while True:
				a=input("Çıkarılacak sayıyı giriniz:")
				if(a=="="):
					print("------------------------------------------------------")
					print("Cevap:",cikarma)
					print("------------------------------------------------------")
					break
				elif(not a=="q" or a=="Q"):
					a=float(a)
					cikarma-=a
					print("------------------------------------------------------")
					print("Sonuç:",cikarma)
					print("------------------------------------------------------")
				elif(a=="q" or a=="Q"):
					print("Geri dönülüyor...")
					break
			break
	except ValueError:
		print("Bir şey oldu.")
		print("Lütfen sayısal bir değer giriniz!")
"""Bu fonksiyon kullanıcıdan içinden çıkarma yapılacak bir sayı ve istendiği kadar çıkarılacak sayı ister. Her sayı girişinde
bir önceki sayıdan yeni girilen sayıyı çıkarır ve her adımı gösterir, ta ki "=" işareti girilip cevap istenene kadar."""

def carpma():
	carpim=1
	try:
		while True:
			a=input("Çarpılacak sayıyı giriniz:")
			if(a=="="):
				print("------------------------------------------------------")
				print("Cevap:",carpim)
				print("------------------------------------------------------")
				break
			elif(not a=="q" or a=="Q"):
				a=float(a)
				carpim*=a
				print("------------------------------------------------------")
				print("Sonuç:",carpim)
				print("------------------------------------------------------")
			elif(a=="q" or a=="Q"):
				print("Geri dönülüyor...")
				break
	except ValueError:
		print("Bir şey oldu.")
		print("Lütfen sayısal bir değer giriniz!")
"""Bu fonksiyon kullanıcıdan birbirleri ile çarpılmasını istediği sayılar ister ve bu sayıları "=" işareti
 girilene kadar sürekli çarpar ve her adımı gösterir."""

def bolme():
	try:
		while True:
			bolum=input("bölünecek sayıyı giriniz:")
			if(not bolum=="q" or bolum=="Q"):
				bolum=float(bolum)
			elif(bolum=="q" or bolum=="Q"):
				print("Geri dönülüyor...")
				break
			while True:
				a=input("Bölecek sayıyı giriniz:")
				if(a=="="):
					print("------------------------------------------------------")
					print("Cevap:",bolum)
					print("------------------------------------------------------")
					break
				elif(not a=="q" or a=="Q"):
					a=float(a)
					bolum/=a
					print("------------------------------------------------------")
					print("Sonuç:",bolum)
					print("------------------------------------------------------")
				elif(a=="q" or a=="Q"):
					print("Geri gidiliyor...")
					break
			break
	except ValueError:
		print("Bir şey oldu.")
		print("Lütfen sayısal bir değer giriniz!")
"""Bu fonksiyon kullanıcının bölünmesini istediği sayıyı yine kullanıcının girdiği sayılara 
böler ve her adımı gösterir, ta ki "=" işareti girilip cevap isteninceye kadar."""