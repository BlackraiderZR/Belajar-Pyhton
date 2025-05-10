# Materi Konversi Suhu

'''
Konversi Suhu dengan basis Operator Aritmatika
* Celcius
* Reamur
* Fahrenhit
* Kelvin
'''

# Konversi Suhu Celcius
print("======[Konversi Suhu Celcius]======")
celcius = float(input("Harap masukan Temperatur Suhu Celcius : "))

# Celcius to Reamur 
reamur = (4/5)*celcius

# Celcius to Fahrenhit
fahrenhit = ((9/5)*celcius)+32

# Celcius to Kelvin
kelvin = celcius+273.15

# Output 
print(f"Temperatur Suhu Celcius = {celcius}°C")
print(f"Temperatur Suhu Reamur = {reamur}°R")
print(f"Temperatur Suhu Fahrenhit = {fahrenhit}°F")
print(f"Temperatur Suhu Kelvin = {kelvin}K")

print("======[Konversi Suhu Reamur]======")
reamur = float(input("Harap masukan Temperatur Suhu Reamur : "))

# Reamur to Celcius 
celcius = (5/4)*reamur

# Reamur to fahrenhit
fahrenhit = ((9/4)*reamur)+32

# Reamur to kelvin
kelvin = ((5/4)*reamur)+273.15

# Output
print(f"Temperatur Suhu Reamur = {reamur}°R")
print(f"Temperatur Suhu Celcius = {celcius}°C")
print(f"Temperatur Suhu Fahrenhit = {fahrenhit}°F")
print(f"Temperatur Suhu Kelvin = {kelvin}K")

print("======[Konversi Suhu Fahrenhit]======")
fahrenhit = float(input("Harap masukan Temperatur Suhu Fahrenhit : "))

# Fahrenhit to Celcius
celcius = (5/9)*(fahrenhit-32)

# Fahrenhit to Reamur 
reamur = (4/9)*(fahrenhit-32)

# Fahrenhit to kelvin
kelvin = celcius+273.15

# Output
print(f"Temperatur Suhu Fahrenhit = {fahrenhit}°F")
print(f"Temperatur Suhu Reamur = {reamur}°R")
print(f"Temperatur Suhu Celcius = {celcius}°C")
print(f"Temperatur Suhu Kelvin = {kelvin}K")

print("======[Konversi Suhu Kelvin]======")
kelvin = float(input("Harap masukan Temperatur Suhu Kelvin : "))

# Kelvin to celcius
celcius = kelvin-273.15

# Kelvin to Reamur 
reamur = (4/5)*(kelvin-273.15)

# Kelvin to fahrenhit 
fahrenhit = (celcius*(9/5)) +32

# Output
print(f"Temperatur Suhu Kelvin = {kelvin}K")
print(f"Temperatur Suhu Fahrenhit = {fahrenhit}°F")
print(f"Temperatur Suhu Reamur = {reamur}°R")
print(f"Temperatur Suhu Celcius = {celcius}°C")