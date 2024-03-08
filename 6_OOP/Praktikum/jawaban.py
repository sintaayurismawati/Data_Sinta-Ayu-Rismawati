# PRIORITAS 1
class Pelanggan:
    def __init__(self, nama, usia, id_pelanggan):
        self.__nama = nama
        self.__usia = usia
        self.__id_pelanggan = id_pelanggan

    def getNama(self):
        return self.__nama
    
    def getUsia(self):
        return self.__usia
    
    def getIdPelanggan(self):
        return self.__id_pelanggan

    def tampilkanInfo(self):
        return "Nama : " + self.__nama + "\nUsia : " + str(self.__usia) + "\nID Pelanggan : " + self.__id_pelanggan
    
    def setNama(self, nama):
        self.__nama = nama
        return self.__nama
    
    def setUsia(self, usia):
        self.__usia = usia
        return self.__usia
    
    def setIdPelanggan(self, idPelanggan):
        self.__id_pelanggan = idPelanggan
        return self.__id_pelanggan
    
class Pelatih :
    def __init__(self, nama, spesifikasi, tahunPengalaman):
        self.__nama = nama
        self.__spesifikasi = spesifikasi
        self.__tahunPengalaman = tahunPengalaman

    def getNama(self):
        return self.__nama
    
    def getSpesifikasi(self):
        return self.__spesifikasi
    
    def getTahunPengalaman(self):
        return self.__tahunPengalaman
    
    def tampilkanInfo(self):
        return "Nama : " + self.__nama + "\nSpesifikasi : " + self.__spesifikasi + "\nTahun Pengalaman : " + str(self.__tahunPengalaman)
    
    def setNama(self, nama):
        self.__nama = nama
        return self.__nama
    
    def setSpesifikasi(self, spesifikasi):
        self.__spesifikasi = spesifikasi
        return self.__spesifikasi
    
    def setTahunPengalaman(self, tahunPengalaman):
        self.__tahunPengalaman = tahunPengalaman
        return self.__tahunPengalaman
    
class KelasLatihan(Pelatih):
    def __init__(self, nama, spesifikasi, tahunPengalaman, jenisLatihan, jadwal):
        super().__init__(nama, spesifikasi, tahunPengalaman)
        self.__jenisLatihan = jenisLatihan
        self.__jadwal = jadwal
        self.__terpesan = False

    def pesanKelas(self):
        if not self.__terpesan:
            self.__terpesan = True
            return f"Kelas {self.__jenisLatihan} berhasil dipesan."
        else:
            return f"Kelas {self.__jenisLatihan} sudah dipesan sebelumnya."

    def batalkanKelas(self):
        if self.__terpesan:
            self.__terpesan = False
            return f"Kelas {self.__jenisLatihan} berhasil dibatalkan."
        else:
            return f"Anda belum memesan kelas {self.__jenisLatihan}."

    def tampilkanInfo(self):
        return super().tampilkanInfo() + "\nJenis Latihan : " + self.__jenisLatihan + "\nJadwal : " + self.__jadwal + "\nTerpesan : " + str(self.__terpesan)

# DEMONSTRASI
pelanggan1 = Pelanggan("Sinta", 20, "RF1906")
pelanggan2 = Pelanggan("Ayu", 21, "RF2003")
pelatihBadminton = Pelatih("Rakha", "Pro Atlet", 5)
pelatihVolly = Pelatih("Qilla", "Juara Nasional", 7)
kelasBadminton = KelasLatihan("Rakha", "Pro Atlet", 5, "Badminton", "Senin, Selasa")
kelasVolly = KelasLatihan("Qilla", "Juara Nasional", 7, "Volly", "Sabtu, Minggu")

print("Daftar Pelanggan")
print("------------------")
print(pelanggan1.tampilkanInfo())
print("")
print(pelanggan2.tampilkanInfo())
print("============================")
print("Daftar Pelatih")
print("------------------")
print(pelatihBadminton.tampilkanInfo())
print("")
print(pelatihVolly.tampilkanInfo())
print("============================")
print("Informasi Kelas Kebugaran")
print("------------------")
print(kelasBadminton.tampilkanInfo())
print("")
print(kelasVolly.tampilkanInfo())

# PRIORITAS 2
class Yoga(KelasLatihan):
    def __init__(self, nama, spesifikasi, tahunPengalaman, jenisLatihan, jadwal, tingkatKesulitan):
        super().__init__(nama, spesifikasi, tahunPengalaman, jenisLatihan, jadwal)
        self.__tingkatKesulitan = tingkatKesulitan

    def aturPosisiYoga(self, posisi):
        self.__tingkatKesulitan = posisi
        return self.__tingkatKesulitan
    
    def pesanKelas(self):
        return super().pesanKelas() + ", Jadwal : " + self._KelasLatihan__jadwal
    
    def batalkanKelas(self):
        return super().batalkanKelas() 
        
    def tampilkanInfo(self):
        return super().tampilkanInfo() + "\nTingkat Kesulitan : " + self.__tingkatKesulitan
    
class AngkatBeban(KelasLatihan):
    def __init__(self, nama, spesifikasi, tahunPengalaman, jenisLatihan, jadwal, beratMaksimun):
        super().__init__(nama, spesifikasi, tahunPengalaman, jenisLatihan, jadwal)
        self.__beratMaksimun = beratMaksimun

    def aturBeratBeban(self, berat) :
        self.__beratMaksimun = berat
        return self.__beratMaksimun        
    
    def pesanKelas(self):
        return super().pesanKelas() + ", Jadwal : " + self._KelasLatihan__jadwal
    
    def batalkanKelas(self):
        return super().batalkanKelas() 
        
    def tampilkanInfo(self):
        return super().tampilkanInfo() + "\nBerat Maksimum : " + str(self.__beratMaksimun) + " Kg"

# DEMONSTRASI
daftarKelas = [
    Yoga("Lina", "Instruktur berbakat", 3, "Yoga", "Everyday", "high"),
    AngkatBeban("Cintya", "Kuat", 4, "Angkat beban" ,"Selasa, Rabu", "midle")
]
print("============================")
print("Informasi Kelas Latihan Tambahan")
print("------------------")
for kelas_latihan in daftarKelas:
    print(kelas_latihan.tampilkanInfo())
    print("")

print("============================")
yoga1 = Yoga("Nasywa", "Instruktur berbakat", 3, "Yoga", "Everyday", "high")
print(yoga1.tampilkanInfo())
print(".")
yoga1.aturPosisiYoga("hard")
print(yoga1.tampilkanInfo())
print("============================")
angkatBeban1 = AngkatBeban("Zahira", "Kuat", 4, "Angkat beban" ,"Selasa, Rabu", "midle")
print(angkatBeban1.tampilkanInfo())
print(".")
angkatBeban1.aturBeratBeban(8)
print(angkatBeban1.tampilkanInfo())
print("................................................................")

# Eksplorasi (Demonstrasi)
yoga1.pesanKelas()
print(yoga1.tampilkanInfo())
print(".................")
yoga1.batalkanKelas()
print(yoga1.tampilkanInfo())
print(":::::::::::::::::::::::::::::::::::::::::::")
angkatBeban1.pesanKelas()
print(angkatBeban1.tampilkanInfo())
print(".................")
angkatBeban1.batalkanKelas()
print(angkatBeban1.tampilkanInfo())