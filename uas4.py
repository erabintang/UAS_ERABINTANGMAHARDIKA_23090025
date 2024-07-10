class Buah:
    def __init__(self, nama, warna, rasa):
        self.nama = nama
        self.warna = warna
        self.rasa = rasa

    def setNama(self, nama):
        self.nama = nama

    def setWarna(self, warna):
        self.warna = warna

    def setRasa(self, rasa):
        self.rasa = rasa

    def information(self):
        return f"Buah {self.nama} memiliki warna {self.warna} dan rasanya {self.rasa}."

class Mangga(Buah):
    def __init__(self, nama, warna, rasa, vitamin):
        super().__init__(nama, warna, rasa)
        self.vitamin = vitamin

    def setVitamin(self, vitamin):
        self.vitamin = vitamin

    def information(self):
        buah_info = super().information()
        return f"{buah_info} Mangga mengandung vitamin {self.vitamin}."

buah1 = Buah("mangga", "Merah", "Manis")
print(buah1.information())

mangga1 = Mangga("mangga Harumanis", "Hijau", "Manis", "C dan A")
print(mangga1.information())