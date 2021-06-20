def alancevremak():
    import alan
    import cevre
    print("------------------------------------------------------")
    print("                 Alan ve Çevre Hesabı                 ")
    print("------------------------------------------------------")
    print("                   Alan:1, Çevre:2                    ")
    print("------------------------------------------------------")
    print("                    Çıkış için:q                      ")
    print("------------------------------------------------------")
    while True:
        islem=input("İşlem seçiniz:")
        print("------------------------------------------------------")
        if(islem=="1"):
            while True:
                print("Hesaplamak için üçgen, dikdörtgen ya da kare yazınız")
                print("Geri dönmek için: q")
                print("------------------------------------------------------")
                cisim=input("Seçim yapınız:")
                print("------------------------------------------------------")
                if(cisim=="ÜÇGEN" or cisim=="üjgen" or cisim=="üçgen" or cisim=="Üçgen" or cisim=="çgen" or cisim=="ügen" or cisim=="üçen" or cisim=="üçgn" or cisim=="üçge"):
                    alan.ucgenalan()
                elif(cisim=="KARE" or cisim=="kare" or cisim=="Kare" or cisim=="are" or cisim=="kre" or cisim=="kae" or cisim=="kar"):
                    alan.karealan()
                elif(cisim=="DİKDÖRTGEN" or cisim=="dikdörtgen" or cisim=="Dikdörtgen" or cisim=="ikdörtgen" or cisim=="dkdörtgen" or cisim=="didörtgen" or cisim=="dikörtgen" or cisim=="dikdrtgen" or cisim=="dikdötgen" or cisim=="dikdörgen" or cisim=="dikdörten" or cisim=="dikdörtgn" or cisim=="dikdörtge"):
                    alan.dikdalan()
                if(cisim=="q" or cisim=="Q"):
                    print("Geri dönülüyor...")
                    break
        
        elif(islem=="2"):
            while True:
                print("Hesaplama için üçgen, dikdörtgen ya da kare yazınız")
                print("Geri dönmek için: q")
                print("------------------------------------------------------")
                cisim=input("Seçim yapınız:")
                print("------------------------------------------------------")
                if(cisim=="ÜÇGEN" or cisim=="üjgen" or cisim=="üçgen" or cisim=="Üçgen" or cisim=="çgen" or cisim=="ügen" or cisim=="üçen" or cisim=="üçgn" or cisim=="üçge"):
                    cevre.ucgencevre()
                elif(cisim=="KARE" or cisim=="kare" or cisim=="Kare" or cisim=="are" or cisim=="kre" or cisim=="kae" or cisim=="kar"):
                    cevre.karecevre()
                elif(cisim=="DİKDÖRTGEN" or cisim=="dikdörtgen" or cisim=="Dikdörtgen" or cisim=="ikdörtgen" or cisim=="dkdörtgen" or cisim=="didörtgen" or cisim=="dikörtgen" or cisim=="dikdrtgen" or cisim=="dikdötgen" or cisim=="dikdörgen" or cisim=="dikdörten" or cisim=="dikdörtgn" or cisim=="dikdörtge"):    
                    cevre.dikdcevre()
                elif(cisim=="q" or cisim=="Q"):
                    break
        elif(islem=="q" or islem=="Q"):
            print("Geri dönülüyor...")
            break
        elif(not islem=="2" or islem=="1"):
            print("                 Alan:1       Çevre:2                 ")
            print("------------------------------------------------------")
            print("Bir şey oldu.")
            print("Lütfen bir işlem giriniz!")
            print("------------------------------------------------------")
