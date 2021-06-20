def ucgencevre():
    try:
        while True:
            print("Geri dönmek için: q")
            k=input("1. Kenarı giriniz:")
            if(k=="q" or k=="Q"):
                print("Geri gidiliyor...")
                print("------------------------------------------------------")
                break
            elif(not k=="q" or k=="Q"):
                l=input("2. Kenarı giriniz:")
                if(l=="q" or l=="Q"):
                    print("Geri gidiliyor...")
                    print("------------------------------------------------------")
                    break
                elif(not l=="q" or l=="Q"):
                    m=input("3. Kenarı giriniz:")
                    if(m=="q" or m=="Q"):
                        print("Geri gidiliyor...")
                        print("------------------------------------------------------")
                        break
            if(k=="=" or l=="=" or m=="="):
                print("------------------------------------------------------")
                print("Cevap:",n)
                print("------------------------------------------------------")
            elif(not k=="q" or l=="q" or m=="q" or k=="Q" or l=="Q" or m=="Q"):
                k=float(k)
                l=float(l)
                m=float(m)
                n=(k+l+m)
                print("------------------------------------------------------")
                print("Cevap:",n)
                print("------------------------------------------------------")
    except ValueError:
        print("Bir şey oldu.")
        print("Lütfen sayısal bir değer giriniz!")
    """Bu fonksiyon kullanıcının girdiği üçgenin 3 kenarını toplayarak üçgenin çevresini bulur."""

def karecevre():
    try:
        while True:
            print("Geri dönmek için: q")
            k=input("Kenar giriniz:")
            if(k=="="):
                print("------------------------------------------------------")
                print("Cevap:",karecevresi)
                print("------------------------------------------------------")
            elif(not k=="q" or k=="Q"):
                k=float(k)
                karecevresi=k*4
                print("------------------------------------------------------")
                print("Cevap:",karecevresi)
                print("------------------------------------------------------")
            elif(k=="q" or k=="Q"):
                print("Geri gidiliyor...")
                print("------------------------------------------------------")
                break
    except ValueError:
        print("Bir şey oldu.")
        print("Lütfen sayısal bir değer giriniz!")
    """Bu fonksiyon kullanıcının girdiği karenin bir kenarını, karenin kenar sayısı olan 4 ile çarparak karenin çevresini bulur."""

def dikdcevre():
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
                    print("Dikdörtgenin çevresi:",dikdcevre)
                    print("------------------------------------------------------")
            elif(not k=="q" or l=="q" or k=="Q" or l=="Q"):
                k=float(k)
                l=float(l)
                if(k>l):
                    dikdcevre=2*(k+l)
                    print("------------------------------------------------------")
                    print("Cevap:",dikdcevre)
                    print("------------------------------------------------------")
                elif(k==l or k<l):
                    print("------------------------------------------------------")
                    print("Dikdörtgenin dört kenarı birbirine eşit veya kısa kenar uzun girilemez!!!")
                    print("------------------------------------------------------")
    except ValueError:
        print("Bir şey oldu.")
        print("Lütfen sayısal bir değer giriniz!")
    """Bu fonksiyon kullanıcının girdiği dikdörtgenin uzun ve kısa kenarını toplayıp iki ile çarparak dikdörtgenin çevresini bulur."""
