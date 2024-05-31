import pandas as pd
from Personel import Personel
from Doktor import Doktor
from Hemsire import Hemsire
from Hasta import Hasta

def main():
    try:
        personel1 = Personel(101, "Nilgün", "Ertan", "Bilgi İşlem", 17500)
        personel2 = Personel(102, "Hasan", "Kaya", "İnsan Kaynakları", 19000)

        # Doktor nesnelerini oluşturma
        doktor1 = Doktor(215, "Faik", "Duman", "Kardiyoloji", 85000, "Kardiyolog", 10, "Acıbadem Hastanesi")
        doktor2 = Doktor(312, "Zeynep", "Dirik", "Nöroloji", 76000, "Nörolog", 8, "Bakırköy Devlet Hastanesi")
        doktor3 = Doktor(146, "Semih", "Ertan", "Göz Hastalıkları", 98700, "Oftalmolog", 12, "Gülhane Eğitim ve Araştırma Hastanesi")

        # Hemşire nesnelerini oluşturma
        hemsire1 = Hemsire(245, "Fatma", "Demir", "Yoğun Bakım", 25600, 40, "Sertifikalı Yoğun Bakım", "İzmir Şehir Hastanesi")
        hemsire2 = Hemsire(296, "Mustafa", "Yılmaz", "Cerrahi", 24750, 36, "Acil Tıp", "Başakşehir Devlet Hastanesi")
        hemsire3 = Hemsire(133, "Seda", "Şimşek", "Acil", 28000, 55, "Acil Tıp", "Özel Ataköy Hastanesi")

        # Hasta nesnelerini oluşturma
        hasta1 = Hasta(301, "Emirhan", "Oğuz", "2004-05-15", "Ateş", "İlaç Kullanımı")
        hasta2 = Hasta(302, "Mehmet", "Kara", "1995-10-20", "Baş Ağrısı", "Dinlenme")
        hasta3 = Hasta(303, "Yusuf", "Çetin", "1997-06-07", "Grip", "Dinlenme")

        # Nesneleri yazdırma
        print("--------------------------------------PERSONELLER----------------------------------------\n")
        print("Personel 1:")
        print(personel1)
        print("\nPersonel 2:")
        print(personel2)


        print("\n----------------------------------------DOKTORLAR----------------------------------------\n")
        print("Doktor 1:")
        print(doktor1)
        print("\nDoktor 2:")
        print(doktor2)
        print("\nDoktor 3:")
        print(doktor3)


        print("\n---------------------------------------HEMŞİRELER----------------------------------------\n")
        print("Hemşire 1:")
        print(hemsire1)
        print("\nHemşire 2:")
        print(hemsire2)
        print("\nHemşire 3:")
        print(hemsire3)

        print("\n----------------------------------------HASTALAR-----------------------------------------\n")
        print("Hasta 1:")
        print(hasta1)
        print("\nHasta 2:")
        print(hasta2)
        print("\nHasta 3:")
        print(hasta3)
        print("\n")


        pd.set_option('display.max_columns', None)  # Tüm sütunları göster
        pd.set_option('display.max_rows', None)  # Tüm satırları göster
        pd.set_option('display.width', None)  # Genişliği otomatik ayarla
        pd.set_option('display.max_colwidth', None)

        data = []
        for obj in [personel1, personel2, doktor1, doktor2, doktor3, hemsire1, hemsire2, hemsire3, hasta1, hasta2, hasta3]:
            data.append(obj.to_dict())

        df = pd.DataFrame(data).fillna(0)
        print(df)

        # Seçilen sütunlar
        selected_columns_df = df[['ad', 'soyad', 'departman', 'maas', 'uzmanlik', 'deneyim_yili', 'hastalik', 'tedavi']]
        print("\n**ÖZEL DATAFRAME**")
        print(selected_columns_df)

        # Maaşı 7000 TL üzeri olan personelleri bulup yazdırma
        maas_7000_ustu = df[df['maas'] > 7000]
        print("\nMAAŞI 7000 TL ÜZERİ OLAN PERSONELLER:")
        print(maas_7000_ustu)

        # Doğum tarihi 1990 ve sonrası olan hastaları bulup yazdırma
        df['dogum_tarihi'] = pd.to_datetime(df['dogum_tarihi'], errors='coerce')
        dogum_tarihi_1990_sonrasi = df[(df['dogum_tarihi'] >= '1990-01-01') & (df['dogum_tarihi'] != 0)]
        print("\n**DOĞUM TARİHİ 1990 VE SONRASI OLAN HASTALAR**")
        print(dogum_tarihi_1990_sonrasi)

        # Hasta adına göre alfabetik sıralanan dataframe
        hasta_df = df[df['hastalik'] != 0].sort_values(by='ad')
        print("\n**HASTA ADINA GÖRE SIRALANMIŞ DATAFRAME**")
        print(hasta_df)

        # 5 yıldan fazla deneyime sahip doktorların sayısını bulma ve yazdırma
        doktor_df = df[df['uzmanlik'] != 0]
        deneyim_5_yil_ustu = doktor_df[doktor_df['deneyim_yili'] > 5]
        print(f"\n5 YILDAN FAZLA DENEYİME SAHİP DOKTOR SAYISI: {len(deneyim_5_yil_ustu)}")

        # Uzmanlık alanlarına göre gruplandırarak toplam sayıyı hesaplama
        uzmanlik_gruplari = deneyim_5_yil_ustu.groupby('uzmanlik').size().reset_index(name='sayisi')
        print("\nUZMANLIK ALANLARINA GÖRE DOKTOR SAYILARI")
        print(uzmanlik_gruplari)

    except Exception as e:
        print(f"Bir hata oluştu: {e}")

if __name__ == "__main__":
    main()
