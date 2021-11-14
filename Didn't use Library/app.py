# Aplikasi Konversi Mata Uang - Kelompok 8

#  Class Warna Teks
class warna:
    BIRU   = '\033[94m'
    KUNING = '\033[93m'
    MERAH  = '\033[91m'
    HIJAU  = '\033[92m'

# Membuat Format RP/Rupiah
def formatrupiah(uang):
    y = str(uang)
    if len(y) <= 3:
        return 'Rp ' + y
    else:
        p = y[-3:]
        q = y[:-3]
        return formatrupiah(q) + '.' + p
    print("Rp", formatrupiah(q), ".", p)

# Banner Judul Aplikasi
print(f"{warna.BIRU}=" * 43)
print(f"{warna.KUNING}✋ Selamat Datang di PyVert - Kelompok 8 😊 \n   Aplikasi Konversi Mata Uang Sederhana{warna.BIRU}")

# List Konversi
print(f"{warna.BIRU}=" * 43)
print("1. Dolar ke Rupiah")
print("2. Rupiah ke Dolar")
print("3. Euro ke Rupiah")
print("4. Rupiah ke Euro")
print("5. Riyal (Arab) ke Rupiah")
print("6. Rupiah ke Riyal (Arab)")
print("7. Tutup Aplikasi")
print(f"{warna.BIRU}=" * 20)

# Deklarasi Variable Pilihan Konversi Pengguna
pilihanUser = int(input(f"{warna.KUNING} Masukan Pilihan: "))

# Logika Proses Konversi
def proses():

    # Dollar ke Rupiah
    if ( pilihanUser == 1 ):
        def dollar_ke_rupiah():
           dollar = int(input(f"{warna.KUNING} Masukan Nominal Dollar : "))
           dollarRupiah = dollar * 15000 
           print("Jadi", dollar, "Dollar bernilai", formatrupiah(dollarRupiah))
        dollar_ke_rupiah()

    # Rupiah ke Dollar  
    elif ( pilihanUser == 2 ): 
        def rupiah_ke_dollar():
           rupiah = int(input(f"{warna.KUNING} Masukan Nominal Rupiah : "))
           rupiahDollar = rupiah / float(15000) 
           print("Jadi", rupiah, "Rupiah bernilai", round(rupiahDollar, 2))
        rupiah_ke_dollar()

    # Euro ke Rupiah
    elif ( pilihanUser == 3 ):
        def euro_ke_rupiah():
           euro = int(input(f"{warna.KUNING} Masukan Nominal Euro : "))
           euroRupiah = euro * 16616 
           return formatrupiah(euroRupiah)
        print(euro_ke_rupiah())

    # Rupiah ke Euro
    elif ( pilihanUser == 4 ):
        def rupiah_ke_euro():
           rupiah = int(input(f"{warna.KUNING} Masukan Nominal Rupiah : "))
           rupiahEuro = rupiah / float(16616) 
           return rupiahEuro
        print(round(rupiah_ke_euro(), 2))

    # Riyal ke Rupiah
    elif ( pilihanUser == 5 ):
        def riyal_ke_rupiah():
           riyal = int(input(f"{warna.KUNING} Masukan Nominal Riyal : "))
           riyalRupiah = riyal * 3817 
           return formatrupiah(riyalRupiah)
        print(riyal_ke_rupiah())


    # Rupiah ke Riyal
    elif ( pilihanUser == 6 ):
        def rupiah_ke_riyal():
           rupiah = int(input(f"{warna.KUNING} Masukan Nominal Rupiah : "))
           rupiahRiyal = rupiah / float(3817) 
           return rupiahRiyal
        print(round(rupiah_ke_riyal(), 2))

    # Berhenti
    elif( pilihanUser == 7):
        # Jika tidak, maka tampilkan terima kasih dan keluar aplikasi
        print(f"{warna.HIJAU} Baik, Terima Kasih telah menggunakan aplikasi kami :)")
        exit()
        
# Menjalankan Proses
proses()

# Perulangan untuk mengulangi konversi
print("=" * 20)
while(input(f"{warna.MERAH}Ulangi Konversi? [Y/T] ... ") == "Y"):

    # Jika pengguna menginput "Y" maka lakukan Proses Konversi lagi.
    print("=" * 20)
    proses()
    print("=" * 20)

# Jika tidak, maka tampilkan terima kasih dan keluar aplikasi
print(f"{warna.HIJAU} Baik, Terima Kasih telah menggunakan aplikasi kami")
