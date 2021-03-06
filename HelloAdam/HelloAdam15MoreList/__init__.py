#  Copyright (c) 2020. Adam Arthur Faizal
from sys import copyright

print("====== MORE LIST ======\n")  # Beberapa method yang bisa digunakan untuk memanipulasi List
Barang = ["Meja", "Kursi", "Lemari", "Kulkas", "Tas"]
print(Barang)

# Method untuk menambah data kedalam list
print('\n--- Method untuk menambah data kedalam list ---')
Barang.append("Mobil")  # Menambah member list di indeks terakhir, tapi hanya terbatas pada satu member saja
print(Barang)
Barang.extend("Motor")  # Menambah member list yang di pisah per huruf
print(Barang)
Barang.insert(3, "Mobil")  # Menambah/menyisipkan member list di indeks tertentu
print(Barang)

# Method untuk menghitung anggota list
print('\n--- Method untuk menghitung anggota list ---')
hitung = Barang.count("Mobil")  # Menghitung berapa jumlah mobil di dalam list
print("Jumlah mobil adalah", hitung)
panjanglist = len(Barang)   # Menghitung panjang list
print("Jumlah barang adalah", panjanglist)

# Method untuk menghapus data didalam list
print('\n--- Method untuk menghapus data didalam list ---')
Barang.pop(1)   # Menghapus data berdasarkan indeks list
print(Barang)
Barang.remove("Lemari")     # Menghapus data berdasarkan nama member list
print(Barang)
# Barang.clear()     # Menghapus keseluruhan anggota
# print(Barang)

# Method lainnya
print('\n--- Method lainnya ---')
Daftar = [2, 1, 3, 5, 4]
print(Daftar)
print(Daftar.index(2))      # Untuk mengetahui posisi elemen suatu list
print(max(Daftar))          # Untuk mengetahui nilai maksimal dari suatu list
print(min(Daftar))          # Untuk mengetaui nilai minimal dari suatu list
Daftar.sort()   # Mengurutkan list
print(Daftar)
Daftar.reverse()    # Reverse list
print(Daftar)


daftarbaru = Daftar.copy()  # Mengcopy list kedalam suatu variabel
daftarbaru2 = Daftar[:]     # Mengcopy list kedalam suatu variabel
daftarbaru.append(0)
daftarbaru2.append(-1)
print(daftarbaru)
print(daftarbaru2)
print(Daftar)

print('\n')
print(copyright)
# by Mbah Putih Mulyosugito
