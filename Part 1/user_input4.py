# Materi User Input Data

# Input data akan bersifat String
nama_anda = input("Masukan nama anda : ")
print(f"Nama saya adalah {nama_anda}", type(nama_anda)) # akan terlihat data type String

# Penggunaan User Input untuk data type int, float, bool menggunakan casting

# User Input Casting Integer
absen = int(input("Masukan nomor absen anda : "))
print(f"Nama saya adalah {nama_anda} dengan nomor absen {absen}", type(absen))

# User Input Casting Float 
nilai_sms1 = float(input("Masukan nilai Bahasa Jawa Semester 1 : "))
nilai_sms2 = float(input("Masukan nilai Bahasa Jawa Semester 2 : "))
print("Type data nilai_sms1 : ", type(nilai_sms1), "dan Type data nilai_sms2 : ", type(nilai_sms2))

# User Input Casting Boolean ( tambahan casting Integer, jika tidak hssil akam selalu True )
valid_nilai = bool(int(input("Konfirmasi Nilai : (0/1)")))
print("Konfirmasi", valid_nilai, type(valid_nilai))

# Hasil Operator sederhana
number = (nilai_sms1+nilai_sms2)/2
print(f"Rata rata nilai mapel Bahasa Jawa Atas nama {nama_anda} / {absen} : {number}")





























