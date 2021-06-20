import time
import hesapmak
import alancevremak
print("------------------------------------------------------")
print("           Hesap Makinesine Hoş Geldiniz!             ")
print("------------------------------------------------------")
print("Basit Hesap Makinesi:1 Alan ve Çevre Hesap Makinesi:2 ")
print("                     Çıkış için: q                    ")
print("------------------------------------------------------")
while True:
    makine=input("Hesap makinesi seçiniz:")
    if(makine=="1"):
        hesapmak.hesapmak()
    elif(makine=="2"):
        alancevremak.alancevremak()
    elif(makine=="q" or makine=="Q"):
        print("Çıkış yapılıyor...")
        time.sleep(1)
        break
    elif(not makine=="1" or makine=="2"):
    	print("------------------------------------------------------")
    	print("Bir şey oldu.")
    	print("Lütfen 1 ya da 2 yazınız!")
    	print("------------------------------------------------------")
    	
