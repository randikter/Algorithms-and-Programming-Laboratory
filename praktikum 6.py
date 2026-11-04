#Program fungsi untuk merata-ratakan nilai sesuai dengan kategori huruf
def rata_rata(b):
    return sum(b) / len(b) if b else 0
a = input("masukkan nilai: ")
b = []
while a in ["A", "A-", "B+", "B", "B-", "C+", "C", "C-", "D", "E"]:
    if a == "A":
        c = 4
    elif a == "A-":
        c = 3.75
    elif a == "B+":
        c = 3.5
    elif a == "B":
        c = 3
    elif a == "B-":
        c = 2.75
    elif a == "C+":
        c = 2.5
    elif a == "C":
        c = 2
    elif a == "C-":
        c = 1.75
    elif a == "D":
        c = 1.5
    elif a == "E":
        c = 1.25
    print("nilai:", c)
    b.append(c)
    a = input("masukkan nilai: ")
d = rata_rata(b)
print("Rata-ratanya adalah: ", d)

#Program menentukan jumlah hari dalam suatu bulan sesuai dengan inputan tahun menggunakan fungsi def
def tahun_kabisat(b):
    return (b % 400 == 0) or (b % 4 == 0 and b % 100 != 0)
def jumlah_hari(a, b):
    if a == 2:
        return 29 if tahun_kabisat(b) else 28
    elif a in (4, 6, 9, 11):
        return 30
    elif 1 <= a <= 12:
        return 31
    return None
print("Program ini akan menentukan jumlah hari dalam bulan tertentu")
print("Masukkan 0 untuk menghentikan program")
a = int(input("masukkan bulan (1-12): "))
while True:
    if a == 0:
        print("Terima kasih sudah menggunakan program saya, sampai berjumpa lagi.")
        break
    elif a == 2:
        b = int(input("masukkan tahun (e.g., 2021): "))
        c = jumlah_hari(a, b)
    else:
        c = jumlah_hari(a, 0)
    if c is None:
        print("Bulan tidak valid. Masukkan angka 1-12.")
    else:
        print(c, "hari dalam sebulan")
    print("Masukkan 0 untuk menghentikan program")
    a = int(input("masukkan bulan (1-12): "))

#Program menampilkan alamat lengkap dengan fungsi def
def data():
    print("=== Masukkan Data Alamat Lengkap ===")
    a = input("Nama Jalan dan No. Rumah  : ")
    b = input("RT / RW (Contoh: 001/005) : ")
    c = input("Kelurahan / Desa          : ")
    d = input("Kecamatan                 : ")
    e = input("Kota / Kabupaten          : ")
    f = input("Provinsi                  : ")
    g = input("Kode Pos                  : ")
    print(f"\n=========================================\n           ALAMAT LENGKAP ANDA           \n=========================================\nJalan {a}, RT/RW {b}\nKel. {c}, Kec. {d}\nKota/Kab. {e}, {f} {g}\n=========================================")
data()
