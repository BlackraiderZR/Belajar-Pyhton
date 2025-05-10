# Materi Operator Aritmatika

# Operator Aritmatika = Operasi Matematika dasar
'''
1. Penjumlahan ( + )
2. Penguranhan ( - )
3. Perkalian ( * ) symbol bintang
4. Pembagian ( / ) symbol slash , pembagian dengan hasil float
5. Modulus ( % ) symbol persen = untuk Operasi Aritmatika sisa bagi 
6. Eksponen ( ** ) symbol 2 bintang = untuk perpangkatan bilangan angka 
7. Floor Division ( // ) symbol 2 slash = untuk pembagian bulat , mengambil nilai ke bawah
'''

# Nilai Variabel dasar
a = 15
b = 5 
c = 8 

#   Operator  Aritmatika

# Pertambahan ( +  )
hasil = a+b 
print(f"Hasil {a} + {b}  = {hasil}")

#  Pengurangan (  - )
hasil = c-b
print(f"Hasil {c} - {b} = {hasil}")

# Perkalian ( * )
hasil = b*hasil # nilai variabel hasil tsrakhir : 3 , jadi 5 × 3
print(f"Hasil {b} × 3 = {hasil}")

# Pembagian ( / )
hasil = hasil/b # nilai hasil = 15
print(f"Hasil 15 : {b} = {hasil}") 
print(type(hasil)) # Type data menjadi float

# Modulus ( % )  
hasil = c%hasil # nilai hasil = 3
print(f"Hasil {c} % 3 = {hasil}")

# Eksponen perpangkatan ( ** )
hasil = hasil**5 # nilai hasil = 2
print(f"Hasil 2⁵ adalah {hasil}")

# Floor Division ( // ) atau Pembagian Bulat kebawah
hasil = hasil//b # nilai hasil = 32 dari perpangkatan sebelumnya
print(f"Hasil 32 // {b} = {hasil} ")
print(type(hasil)) # apabila pembagian ada sisa maka data type menjadi Float, namun jika tidak ada sisa bagi akan menjadi Integer

# Operator Priority ( Prioritas Operator ) / Operational Precedence

'''
Operator Priority :
1. () = tanda kurung
2. ** = perpangkatan
3. +x, -x = Unary Plus / Minus ( next materi )
4. *, /, //, % = perkalian, pembagian, Floor Division, dan Modulus
5. +, - = Penjumlahan, dan Pengurangan
'''

hasil = (b*2)+b**2-a%c//2
print("======[Operator Priority]=======")
print(f"( {b}×2 ) + {b}² - {a} % {c} // 2") # pertanyaan
print("10 + 25 - 7 // 2") # Proses perhintungan #1
print("10 + 25 - 3,5") # Proses perhintungan #2
print("35 - 3") # Proses perhintungan #3
print(f"( {b}×2 ) + {b}² - {a} % {c} // 2 = {hasil}") # hasil