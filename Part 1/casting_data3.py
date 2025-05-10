# Materi Casting Data

# Casting Data = mengubah tipe data suatu nilai menjadi tipe data yang lain secara sengaja

# INTEGER
print("=====[INTEGER]=====")

# buat data awal ( integer )
data_int = 10
print("Nilai data_int adalah", data_int, type(data_int))

# Casting data 
# Integer to Float
data_float = float(data_int) 
print("Nilai Integer jadi Float", data_float, type(data_float))

# Integer to String 
data_str = str(data_int) 
print("Nilai Integer jadi String", data_str, type(data_str))

# Integer to Boolean
data_bool = bool(data_int) 
print("Nilai Integer jadi Boolean", data_bool, type(data_bool)) # apabila data_int selain angka 0 akan true

print("=====[FLOAT]=====")

# buat data awal ( float )
data_float = 5.5
print("Nilai data_float adalah", data_float, type(data_float))

# Float to Integer
data_int = float(data_float)
print("Nilai Float menjadi Integer", data_int, type(data_int))

# Float to String
data_str = str(data_float)
print("Nilai Float menjadi String", data_str, type(data_str))

# Float to Boolean 
data_bool = bool(data_float)
print("Nilai Float menjadi Boolean", data_bool, type(data_bool)) # jika angka selain 0 akan menghasilkan true

print("=====[String]=====")

# buat data awal ( string )
print("Nilai data_str adalah", data_str, type(data_str))
data_str = "0" # Ini Type String namun berupa menjadi tesk

# String to Integer
data_int = int(data_str) 
print("Nilai String menjadi Integer", data_int, type(data_int)) # Apabila data_str bukan berupa berisi Angka, hasilnya error

# String to Float
data_float = float(data_str)
print("Nilai String menjadi float", data_float, type(data_float)) # # Apabila data_str bukan berupa berisi Angka, hasilnya error

# String to Boolean
data_bool = bool(data_str)
print("Hasil String menjadi Boolean", data_bool, type(data_bool)) # Apabila nilai data_str tidak ada nilai ( kosong ) , maka akan menghasilkan nilai False

print("=====[Boolean]=====")

# buat data awal ( Boolean )
data_bool = True # True or False
print("Nilai data_bool adalah", data_bool, type(data_bool))

# Boolean to Integer
data_int = int(data_bool)
print("Hasil Boolean menjadi Integer", data_int, type(data_int)) # Apabila nilai data_bool True akan menghasilkan angka 1 , namun jika False akan menghasilkan angka 0

# Boolean to float
data_float = float(data_bool)
print("Hasil Boolean menjadi float", data_float, type(data_float)) # Apabila nilai data_bool True akan menghasilkan angka 1 , namun jika False akan menghasilkan angka 0

# Boolean to String
data_str = str(data_bool)
print("Hasil Boolean menjadi string", data_str, type(data_str))
