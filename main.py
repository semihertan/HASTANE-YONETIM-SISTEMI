import pandas as pd
from Personel import Personel
from Doktor import Doktor
from Hemsire import Hemsire
from Hasta import Hasta

def main():
    try:
        personel1 = Personel(101, "Ahmet", "Yılmaz", "Bilgi İşlem", 5000)
        personel2 = Personel(102, "Ayşe", "Kaya", "İnsan Kaynakları", 6000)

        # Doktor nesnelerini oluşturma
        doktor1 = Doktor(101, "Ahmet", "Yılmaz", "Kardiyoloji", 15000, "Kardiyolog", 10, "Acıbadem Hastanesi")
        doktor2 = Doktor(102, "Ayşe", "Kaya", "Nöroloji", 16000, "Nörolog", 8, "Memorial Hastanesi")

        # Hemşire nesnelerini oluşturma
        hemsire1 = Hemsire(201, "Fatma", "Demir", "Yoğun Bakım", 8000, 40, "Sertifikalı Yoğun Bakım", "Özel Hastane")
        hemsire2 = Hemsire(202, "Mustafa", "Yılmaz", "Cerrahi", 8500, 36, "Acil Tıp", "Devlet Hastanesi")

        # Hasta nesnelerini oluşturma
        hasta1 = Hasta(301, "Ali", "Yılmaz", "1980-05-15", "Ateş", "İlaç Kullanımı")
        hasta2 = Hasta(302, "Mehmet", "Kara", "1975-10-20", "Baş Ağrısı", "Dinlenme")

        # Nesneleri yazdırma
        print("Oluşturulan Personeller:")
        print("Personel 1:")
        print(personel1)
        print("\nPersonel 2:")
        print(personel2)

        print("Doktorlar:")
        print("Doktor 1:")
        print(doktor1)
        print("\nDoktor 2:")
        print(doktor2)

        print("\nHemşireler:")
        print("Hemşire 1:")
        print(hemsire1)
        print("\nHemşire 2:")
        print(hemsire2)

        print("\nHastalar:")
        print("Hasta 1:")
        print(hasta1)
        print("\nHasta 2:")
        print(hasta2)


        data = []
        for obj in [personel1, personel2, doktor1, doktor2, hemsire1, hemsire2, hasta1, hasta2]:
            data.append(vars(obj))

        df = pd.DataFrame(data)
        print(df)

    except Exception as e:
        print(f"Bir hata oluştu: {e}")


if __name__ == "__main__":
    main()
