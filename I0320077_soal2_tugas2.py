nama = "Oktavianus Auwdri"
print("Nama Saya = ", nama)
umur = 19
print("Umur Saya = ", umur, "tahun")
tempat_lahir = "Kota Cirebon"
tanggal_lahir = 5
bulan_lahir = "Oktober"
tahun_lahir = 2001
print("Tempat, Tanggal Lahir =", tempat_lahir, ", ",tanggal_lahir, bulan_lahir, tahun_lahir )
jenis_kelamin = "Laki -Laki"
print("Jenis kelamin = ", jenis_kelamin)
alamat = """Pulasaren Timur, GG.Khohar No 67. RT 003,
RW 0001, Kelurahan Pulasaren, Kecamatan Pekalipan, Kota Cirebon"""
print("Alamat Tinggal = ", alamat)
kode_pos = 45116
print("Kode Pos =", kode_pos)
agama = "Kristen"
print("Agama = ", agama)
tinggi_badan = 165.5
print("Tinggi Badan = ", tinggi_badan)
berat_badan = 50.5
print("Berat Badan = ", berat_badan)
ukuran_sepatu = 40.5
print("Ukuran Sepatu = ", ukuran_sepatu)
hobi = "Basket, Berenang, Main Game"
print("Hobi = ", hobi)
jumlah_saudara = 2
print("Jumlah Saudara =", jumlah_saudara)
tempat_kuliah = "Universitas Sebelas Maret"
print("Tempat Kuliah = ", tempat_kuliah)
program_studi = "Teknik Industri"
print("Program Studi = ", program_studi)
sekolah_SMA = "SMAK Penabur Cirebon"
print("Sekolah saat SMA = ", sekolah_SMA)
makanan_favorit = "Kepiting, Indomie, Nasi Goreng, dan Sate"
print("Makanan Favorit = ", makanan_favorit)
minuman_favorit= "Fruit Tea, Fanta, Thai Tea"
print("Minuman Favorit = ", minuman_favorit, '\n')
#Perhitungan detail Umur
from datetime import datetime
from dateutil import relativedelta
date1 = datetime(2001, 10, 5)
date2 = datetime.today()
diff = relativedelta.relativedelta(date2, date1)
years = diff.years
months = diff.months
days = diff.days
print('Umur saya : {} tahun {} bulan {} hari'.format(years, months, days))