def ucgenalan():
    try:
        while True:
            print("Geri dönmek için: q")
            k=input("Üçgenin taban kenarını giriniz:")
            if(k=="q" or k=="Q"):
                print("Geri gidiliyor...")
                print("------------------------------------------------------")
                break
            elif(not k=="q" or k=="Q"):
                l=input("Üçgenin yüksekliği giriniz:")
                if(l=="q" or l=="Q"):
                    print("Geri gidiliyor...")
                    print("------------------------------------------------------")
                    break
            if(k=="=" or l=="="):
                print("------------------------------------------------------")
                print("Cevap:",ucgenalani)
                print("------------------------------------------------------")
            elif(not k=="q" or l=="q"or k=="Q" or l=="Q"):
                k=float(k)
                l=float(l)
                ucgenalani=k*l/2
                print("------------------------------------------------------")
                print("Cevap:",ucgenalani)
                print("------------------------------------------------------")
    except ValueError:
        print("Bir şey oldu.")
        print("Lütfen sayısal bir değer giriniz!")
    """Bu fonksiyon kullanıcının girdiği üçgenin alt tabanı ve yüksekliğini çarpıp ikiye bölerek üçgenin alanını bulur."""
    
def karealan():
    try:
        while True:
            print("Geri dönmek için: q")
            k=input("Kenar giriniz:")
            if(k=="="):
                print("------------------------------------------------------")
                print("Cevap:",karealani)
                print("------------------------------------------------------")
            elif(not k=="q" or k=="Q"):
                k=float(k)
                karealani=k*k
                print("------------------------------------------------------")
                print("Cevap:",karealani)
                print("------------------------------------------------------")
            elif(k=="q" or k=="Q"):
                print("Geri gidiliyor...")
                print("------------------------------------------------------")
                break
    except ValueError:
        print("Bir şey oldu.")
        print("Lütfen sayısal bir değer giriniz!")
    """Bu fonksiyon kullanıcının girdiği karenin bir kenarıyla kendisini çarparak karenin alanını bulur."""

def dikdalan():
    try:
        while True:
            print("Geri dönmek için: q")
            k=input("Uzun kenarı giriniz:")
            if(k=="q" or k=="Q"):
                print("Geri gidiliyor...")
                print("------------------------------------------------------")
                break
            elif(not k=="q" or k=="Q"):
                l=input("Kısa kenarı giriniz:")
                if(l=="q" or l=="Q"):
                    print("Geri gidiliyor...")
                    print("------------------------------------------------------")
                    break
            if(k=="=" or l=="="):
                    print("------------------------------------------------------")
                    print("Dikdörtgenin çevresi:",dikdalani)
                    print("------------------------------------------------------")
            elif(not k=="q" or l=="q" or k=="Q" or l=="Q"):
                k=float(k)
                l=float(l)
                if(k>l):
                    dikdalani=(k*l)
                    print("------------------------------------------------------")
                    print("Cevap:",dikdalani)
                    print("------------------------------------------------------")
                elif(k==l or k<l):
                    print("------------------------------------------------------")
                    print("Dikdörtgenin dört kenarı birbirine eşit veya kısa kenar uzun girilemez!!!")
                    print("------------------------------------------------------")
    except ValueError:
        print("Bir şey oldu.")
        print("Lütfen sayısal bir değer giriniz!")
    """Bu fonksiyon kullanıcının girdiği dikdörtgenin uzun ve kısa kenarını birbirleri ile çarparak dikdörtgenin alanını bulur."""