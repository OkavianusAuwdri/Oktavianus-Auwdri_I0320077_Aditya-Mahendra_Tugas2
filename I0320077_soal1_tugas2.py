#Menghitung Luas persegi panjang
print("Menghitung Luas Persegi Panjang")
Panjang = float(input('Masukan nilai panjang = '))
Lebar = float(input('Masukan nilai lebar = '))
Luas_PersegiPanjang = Panjang * Lebar
print("Luas Persegi Panjang = " ,Luas_PersegiPanjang, '\n')

#Menghitung Luas Lingkaran
print("Menghitung Luas Lingkaran")
r = float(input("Masukan nilai jari - jari = "))
Luas_Lingkaran = 3.14 * (r**2)
print("Luas Lingkaran = ", Luas_Lingkaran, '\n')

#Menghitung Luas Permukaan Kubus
print("Menghitung Luas Permukaan Kubus")
s = float(input("Masukan panjang sisi kubus = "))
LuasPermukaan_Kubus = 6 * (s**2)
print("Luas Permukaan Kubus = ", LuasPermukaan_Kubus, '\n')

#Menghitung Konversi Suhu Celcius ke Fahrenheit
print("Menghitung Konversi Suhu Celcius ke Fahrenheit")
C = float(input("Masukan Suhu (Celcius) = "))
F = (C * 9/5) + 32
print("Suhu dalam Celcius = ", C)
print("Konversi Suhu Celcius ke Fahrenheit = ", F, '\n')

#Menhitung Konversi Suhu Reamur ke Kelvin
print("Menghitung Konversi Suhu Reamur ke Kelvin")
R = float(input("Masukan Suhu (Reamur) = "))
K = (R * 5/4) + 273
print("Suhu dalam Reamur = ", R )
print("Konversi Suhu Reamur ke Kelvin = ", K)

