
__adSoyad__ = "Nurullah GÜNGÖR"
__numara__ = "22210201032"

import os;
ogrenciList = [
    #Hızlı Deneme İçin Örnek Kayıtlar
    #{'isim': 'Nurullah', 'numara': 1, 'boy': 175},
    #{'isim': 'Ahmet', 'numara': 2, 'boy': 163},
    #{'isim': 'Mehmet', 'numara': 3, 'boy': 185},
    {'isim': 'Bilal', 'numara': 4, 'boy': 170}
]

while True:
    os.system('cls')
    
    print("1 - Kayıt Ekle")
    print("2 - Kayıt Değiştir")
    print("3 - Kayıt Listele")
    print("4 - Öğrenci Sayısı")
    print("5 - En Büyük Boy")
    print("6 - En Küçük Boy")
    print("7 - Boyların Toplamı")
    print("8 - Boyların Ortalaması")
    print("9 - Çıkış")
    
    secim = input("LÜtfen Yapacağınız İşlemi Seçin: ")

    match secim:
        case "1": # Kayıt Ekleme
            isim = input("isim giriniz : ")
            numara = int(input("numara giriniz: "))
            boy = int(input("boy giriniz(cm): "))           
            ogrenciList.append({"isim": isim, "numara": numara, "boy": boy})
            print("Kayıt Eklendi. \n")
            input("Devam Etmek için bir tuşa basınız..")
        
        case "2": # Kayıt Değiştirme
            ogrenciListIndex = int(input("Değiştirilecek Kayıt İndeksi : "))
            if (ogrenciListIndex < len(ogrenciList) and ogrenciListIndex >= 0) : 
                isim = input("isim giriniz : ")
                numara = int(input("numara giriniz: "))
                boy = int(input("boy giriniz(cm): "))

                ogrenciList[ogrenciListIndex] = {"isim": isim, "numara": numara, "boy": boy}
                print("Kayıt Değiştirildi. \n")

                input("Devam Etmek için bir tuşa basınız..")
            else:
                print("Geçersiz İndex! \n")

                input("Devam Etmek için bir tuşa basınız..")
        
        case "3": # Kayıt Listeleme
            if len(ogrenciList) == 0:
                print("Kayıt Bulunamadı ! \n")

                input("Devam Etmek için bir tuşa basınız..")

            else:
                for ogrenciListIndex, ogrenci in enumerate(ogrenciList):
                    print(f"{ogrenciListIndex}İsim: {ogrenci['isim']}, Numara: {ogrenci['numara']}, Boy: {ogrenci['boy']}")
                print()

                input("Devam Etmek için bir tuşa basınız..")

        case "4": # Öğrenci Sayısı
            print(len(ogrenciList))

            input("Devam Etmek için bir tuşa basınız..")
        
        case "5": # En Büyük Boy
            if len(ogrenciList) > 0:
                enBuyukBoy = max(ogrenciList, key=lambda ogrenci: ogrenci["boy"])
                print(f"""
                En Uzun Öğrenci: 
                İsim   : {enBuyukBoy['isim']}
                Numara : {enBuyukBoy['numara']}
                Boy    : {enBuyukBoy['boy']}""")

                input("Devam Etmek için bir tuşa basınız..")

            else:
                print("Kayıtlı Öğrenci Sayısı 0")

                input("Devam Etmek için bir tuşa basınız..")

        case "6": # En Küçük Boy
            if len(ogrenciList) > 0:
                enKisaBoy = min(ogrenciList, key=lambda ogrenci: ogrenci["boy"])
                print(f"""
                En Kısa Öğrenci: 
                İsim   : {enKisaBoy['isim']}
                Numara : {enKisaBoy['numara']}
                Boy    : {enKisaBoy['boy']}""")

                input("Devam Etmek için bir tuşa basınız..")

            else:
                print("Kayıtlı Öğrenci Sayısı 0")

                input("Devam Etmek için bir tuşa basınız..")

        case "7": # Boyların Toplamı
            if len(ogrenciList) == 0:
                print("Kayıt bulunamadı ! \n")

                input("Devam Etmek için bir tuşa basınız..")

            else:
                topBoy = sum(ogrenci['boy'] for ogrenci in ogrenciList)
                print(f"Öğrencilerin toplam boyu : {topBoy}")

                input("Devam Etmek için bir tuşa basınız..")


        case "8": # Boyların Ortamalası
            # Bütün sayılar toplanır ve indis kadar bölünür.
            if len(ogrenciList) != 0:
                boyToplam = 0
                for ogrenci in ogrenciList:
                    boyToplam += ogrenci['boy']
                ortBoy = boyToplam / len(ogrenciList)
                print(f"Öğrenci Boylarının Ortalaması: {ortBoy}")

                input("Devam Etmek için bir tuşa basınız..")
            else:
                print("Kayıt bulunamadı ! \n")

                input("Devam Etmek için bir tuşa basınız..")
            

        case "9": # Çıkış İşlemi
            os.system('cls')
            quit()
            
        
        case _:
            print("Lütfen belirtilen seçeneklerden birini seçiniz.")
            input("Devam Etmek için bir tuşa basınız..")
    
    