#Mengonversi suhu dari fahrenheit ke celcius Exercise 2.4

#menampilkan informasi program

print("Konversi suhu (Fahrenheit ke Celcius)")

#input suhu dalam fahrenheit
F = float(input("Masukan suhu(fahrenheit): "))

#melakukan konversi suhu ke celcius
C = 5 * (F-32) / 9

#menampilkan hasil konversi ke layar
print("Fahrenheit: ", F)
print("Celcius: ", C)