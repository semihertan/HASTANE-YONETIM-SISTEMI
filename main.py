import pandas as pd
from Personel import Personel
from Doktor import Doktor
from Hemsire import Hemsire
from Hasta import Hasta

def main():
    try:
        personel1 = Personel(101, "Nilgün", "Ertan", "Bilgi İşlem", 17500)
        personel2 = Personel(102, "Hasan", "Kaya", "İnsan Kaynakları", 19000)

        doktor1 = Doktor(215, "Faik", "Duman", "Kardiyoloji", 85000, "Kardiyolog", 10, "Acıbadem Hastanesi")
        doktor2 = Doktor(312, "Zeynep", "Dirik", "Nöroloji", 76000, "Nörolog", 8, "Bakırköy Devlet Hastanesi")
        doktor3 = Doktor(146, "Semih", "Ertan", "Göz Hastalıkları", 98700, "Oftalmolog", 12, "Gülhane Eğitim ve Araştırma Hastanesi")

        hemsire1 = Hemsire(245, "Fatma", "Demir", "Yoğun Bakım", 25600, 40, "Sertifikalı Yoğun Bakım", "İzmir Şehir Hastanesi")
        hemsire2 = Hemsire(296, "Mustafa", "Yılmaz", "Cerrahi", 24750, 36, "Acil Tıp", "Başakşehir Devlet Hastanesi")
        hemsire3 = Hemsire(133, "Seda", "Şimşek", "Acil", 28000, 55, "Acil Tıp", "Özel Ataköy Hastanesi")

        hasta1 = Hasta(301, "Emirhan", "Oğuz", "2004-05-15", "Ateş", "İlaç Kullanımı")
        hasta2 = Hasta(302, "Mehmet", "Kara", "1995-10-20", "Baş Ağrısı", "Dinlenme")
        hasta3 = Hasta(303, "Yusuf", "Çetin", "1997-06-07", "Grip", "Dinlenme")

        pd.set_option('display.max_columns', None)
        pd.set_option('display.max_rows', None)
        pd.set_option('display.width', None)
        pd.set_option('display.max_colwidth', None)

        data = []
        for obj in [personel1, personel2, doktor1, doktor2, doktor3, hemsire1, hemsire2, hemsire3, hasta1, hasta2, hasta3]:
            data.append(obj.to_dict())

        df = pd.DataFrame(data).fillna(0)
        print(df)

        while True:
            print("\nYapmak istediğiniz işlemi seçin:")
            print("1. Maaşı 7000 TL üzeri olan personelleri yazdır")
            print("2. Doğum tarihi 1990 ve sonrası olan hastaları yazdır")
            print("3. Ad, soyad, departman, maaş, uzmanlık, deneyim yılı, hastalık, tedavi bilgilerini içeren yeni bir DataFrame oluştur")
            print("4. 5 yıldan fazla deneyime sahip doktorların sayısını bul ve yazdır")
            print("5. Doktorların maaşını arttırma")
            print("6. Uzmanlık alanlarına göre doktorlar ve sayıları")
            print("7. Hasta adına göre sıralanmış DataFrame")
            print("8. Tedavi süresi gösterme")
            print("9. Çıkış")

            secim = input("Seçiminiz (1-8): ")

            if secim == '1':
                maas_7000_ustu = df[df['maas'] > 7000]
                print("\nMAAŞI 7000 TL ÜZERİ OLAN PERSONELLER:")
                print(maas_7000_ustu)

            elif secim == '2':
                df['dogum_tarihi'] = pd.to_datetime(df['dogum_tarihi'], errors='coerce')
                dogum_tarihi_1990_sonrasi = df[(df['dogum_tarihi'] >= '1990-01-01') & (df['dogum_tarihi'] != 0)]
                print("\nDOĞUM TARİHİ 1990 VE SONRASI OLAN HASTALAR:")
                print(dogum_tarihi_1990_sonrasi)

            elif secim == '3':
                selected_columns_df = df[['ad', 'soyad', 'departman', 'maas', 'uzmanlik', 'deneyim_yili', 'hastalik', 'tedavi']]
                print("\nYENİ DATAFRAME:")
                print(selected_columns_df)

            elif secim == '4':
                doktor_df = df[df['uzmanlik'] != 0]
                deneyim_5_yil_ustu = doktor_df[doktor_df['deneyim_yili'] > 5]
                print(f"\n5 YILDAN FAZLA DENEYİME SAHİP DOKTOR SAYISI: {len(deneyim_5_yil_ustu)}")

            elif secim == '5':
                doktorlar = [doktor1, doktor2, doktor3]
                oran = float(input("Maaş artış oranını yüzde olarak girin: "))
                for doktor in doktorlar:
                    doktor.maas_arttir(oran)
                    print(f"{doktor.get_ad()}: {doktor.maas}")
                    
            elif secim == '6':
                doktor_df = df[df['uzmanlik'] != 0]
                uzmanlik_gruplari = doktor_df.groupby('uzmanlik').size()
                print("\nUZMANLIK ALANLARINA GÖRE DOKTOR SAYILARI")
                print(uzmanlik_gruplari)

            elif secim == '7':
                hasta_df = df[df['hastalik'] != 0].sort_values(by='ad')
                print("\n**HASTA ADINA GÖRE SIRALANMIŞ DATAFRAME**")
                print(hasta_df)

            elif secim == '8':
                for hasta in[hasta1, hasta2, hasta3]:
                    print(f"AD: {hasta.get_ad()} SOYAD: {hasta.get_soyad()} Hastalık: {hasta.get_hastalik()}, Tedavi: {hasta.get_tedavi()}, Tedavi Süresi: {hasta.tedavi_suresi_hesapla()} gün")

            elif secim == '9':
                print("Programdan çıkılıyor.")
                break

            else:
                print("Geçersiz seçim. Lütfen 1 ile 8 arasında bir değer girin.")

    except Exception as e:
        print(f"Bir hata oluştu: {e}")

if __name__ == "__main__":
    main()
