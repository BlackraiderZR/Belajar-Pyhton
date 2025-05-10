# Belajar Bahasa Pemograman Python

# Assignment adalah menetapkan dan mengisi sautu nilai ke variabel

# Single Assigemnt
nama = "Alwanu Zaky Raihan"
alamat = "Colomadu, Karanganyar"
kelas = 10

print(nama)
print(alamat)
print(kelas)

print(f"Halo perkenalkan nama saya {nama} sekarang saya kelas {kelas} dan saya tinggal di {alamat}")

# Multi Assignment
NamaSaya, Kabupaten, Sekolah, Tahun_Lahir = "Alwanu Zaky Raihan", "Karanganyar", "SMK n 9 Surakarta", 2008

print(NamaSaya)
print(Kabupaten)
print(Sekolah)
print(Tahun_Lahir)

print(f"Halo saya {NamaSaya} bersekolah di {Sekolah}, namun domisili saya di Kabupaten {Kabupaten} dan saya lahir di tahun {Tahun_Lahir}.")

Tahun, Tahun_Lahir, Nomor_Absen = 2025, 2008, 6
print(Tahun, Tahun_Lahir, Nomor_Absen)

'''
Convention Name variabel
1. snake_case = untuk Variabel dan Fungsi
2. camelCase = Tidak di rekomendasi di Python, kecuali terpaksa
3. PascalCase = untuk class 
4. UPPER_CASE = untuk nilai Konstanta ( tetap )
'''

# snake_case

nama_saya = "Alwwanu Zaky Raihan"
kota_saya = "Karanganyar"
status_saya = "pelajar"

# camelCase

namaSaya = "Alwanu Zaky Raihan"
kelasSaya = 10

# PascalCase

class Biodata:
  def __init__(self, nama, umur, alamat):
    self.nama = nama
    self.umur = umur
    self.alamat = alamat
    
  def perkenalan(self):
    print(f"Halo perkenalkan nama saya {self.nama} umur saya sekarang {self.umur} dengan alamat saya di {self.alamat}")
    
# assignt nilai class
biodata1 = Biodata("Alwanu Zaky Raihan", 10, "Colomadu, Karanganyar")
biodata2 = Biodata("Muhammas Rafli", 12, "Colomadu, Karanganyar")
  
biodata1.perkenalan()

# UPPER_CASE

PHI = 3.14
RATE_CONVERT = 2


# Dynamic Typing

nama = "Zaky"
print(type(nama))
nama = 10
print(type(nama))

# Memory Addres = Lokasi di memori komputer suatu nilai atau data 

nama = "Alwanu Zaky Raihan"
print(id(nama)) # akan muncul id lokasi 

a = 5 
b = a
# akan cetak id lokasi yang sama karena objek nya sama
print(id(a)) 
print(id(b)) 
