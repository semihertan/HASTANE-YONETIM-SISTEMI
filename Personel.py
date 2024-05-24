class Personel:
    def __init__(self, personel_no, ad, soyad, departman, maas):
        self.__personel_no = personel_no
        self.__ad = ad
        self.__soyad = soyad
        self.__departman = departman
        self.__maas = maas

    #get fonk.
    def get_personel_no(self):
        return self.__personel_no

    def get_ad(self):
        return self.__ad

    def get_soyad(self):
        return self.__soyad

    def get_departman(self):
        return self.__departman

    def get_maas(self):
        return self.__maas

    #set fonk.
    def set_personel_no(self, personel_no):
        self.__personel_no = personel_no

    def set_ad(self, ad):
        self.__ad = ad

    def set_soyad(self, soyad):
        self.__soyad = soyad

    def set_departman(self, departman):
        self.__departman = departman

    def set_maas(self, maas):
        self.__maas = maas

    def __str__(self):
        return (f"PERSONEL NO: {self.__personel_no}\n"
                f"AD: {self.__ad}\n"
                f"SOYAD: {self.__soyad}\n"
                f"DEPARTMAN: {self.__departman}\n"
                f"MAAŞ: {self.__maas}")