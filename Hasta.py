class Hasta:
    def __init__(self, hasta_no, ad, soyad, dogum_tarihi, hastalik, tedavi):
        self.__hasta_no = hasta_no
        self.__ad = ad
        self.__soyad = soyad
        self.__dogum_tarihi = dogum_tarihi
        self.__hastalik = hastalik
        self.__tedavi = tedavi

    def get_hasta_no(self):
        return self.__hasta_no

    def get_ad(self):
        return self.__ad

    def get_soyad(self):
        return self.__soyad

    def get_dogum_tarihi(self):
        return self.__dogum_tarihi

    def get_hastalik(self):
        return self.__hastalik

    def get_tedavi(self):
        return self.__tedavi

    #set
    def set_hasta_no(self, hasta_no):
        self.__hasta_no = hasta_no

    def set_ad(self, ad):
        self.__ad = ad

    def set_soyad(self, soyad):
        self.__soyad = soyad

    def set_dogum_tarihi(self, dogum_tarihi):
        self.__dogum_tarihi = dogum_tarihi

    def set_hastalik(self, hastalik):
        self.__hastalik = hastalik

    def set_tedavi(self, tedavi):
        self.__tedavi = tedavi

    def to_dict(self):
        return {
            "personel_no": None,
            "ad": self.get_ad(),
            "soyad": self.get_soyad(),
            "departman": None,
            "maas": None,
            "uzmanlik": None,
            "deneyim_yili": None,
            "hastane": None,
            "calisma_saati": None,
            "sertifika": None,
            "hasta_no": self.get_hasta_no(),
            "dogum_tarihi": self.get_dogum_tarihi(),
            "hastalik": self.get_hastalik(),
            "tedavi": self.get_tedavi()
        }

    def __str__(self):
        return (f"HASTA NO: {self.__hasta_no}\n"
                f"AD: {self.__ad}\n"
                f"SOYAD: {self.__soyad}\n"
                f"DOĞUM TARİHİ: {self.__dogum_tarihi}\n"
                f"HASTAIK: {self.__hastalik}\n"
                f"TEDAVİ: {self.__tedavi}")
