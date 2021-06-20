def hesapmak():
    import islem
    print("------------------------------------------------------")
    print("             Hesap Makinesine Hoşgeldiniz             ")
    print("------------------------------------------------------")
    print("                 Geri dönmek için: q                  ")
    print("------------------------------------------------------")
    print("       Toplama:+  Çıkarma:-  Çarpma:*  Bölme:/        ")
    print("------------------------------------------------------")
    while True:
        islemx=input("İşlem seçiniz:")
        print("------------------------------------------------------")
        if(islemx=="+"):
            print("İşlemi bitirmek için = işareti koyunuz!")
            print("------------------------------------------------------")
            islem.toplama()
        elif(islemx=="-"):
            print("İşlemi bitirmek için = işareti koyunuz!")
            print("------------------------------------------------------")
            islem.cikarma()
        elif(islemx=="*"):
            print("İşlemi bitirmek için = işareti koyunuz!")
            print("------------------------------------------------------")
            islem.carpma()
        elif(islemx=="/"):
            print("İşlemi bitirmek için = işareti koyunuz!")
            print("------------------------------------------------------")
            islem.bolme()
        elif(islemx=="q" or islemx=="Q"):
            print("Geri dönülüyor...")
            break
        elif(not islemx=="+" or islemx=="-" or islemx=="*" or islemx=="/"):
            print("      Toplama:+   Çıkarma:-   Çarpma:*   Bölme:/      ")
            print("------------------------------------------------------")
            print("Bir şey oldu.")
            print("Lütfen bir işlem giriniz!")
            print("------------------------------------------------------")