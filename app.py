# Aplikasi Konversi Mata Uang 

# Import Modul
import sys
from modules.termcolor import colored, cprint
from modules import rupiah

# Banner Judul Aplikasi
print(colored("=" * 43, "yellow"))
print(
    colored(
        "✋Selamat Datang di PyVert - Kelompok 8 😊 \n  Aplikasi Konversi Mata Uang Sederhana",
        "blue",
    )
)

# List Konversi Mata Uang
print(colored("=" * 43, "yellow"))
print("1. Dolar ke Rupiah")
print("2. Rupiah ke Dolar")
print("3. Euro ke Rupiah")
print("4. Rupiah ke Euro")
print("5. Riyal (Arab) ke Rupiah")
print("6. Rupiah ke Riyal (Arab)")
print("7. Tutup Aplikasi")
print(colored("=" * 20, "yellow"))

# Deklarasi Variable Pilihan Konversi Pengguna
pilihanUser = int(input("Masukan Pilihan: "))

# Logika Proses Konversi
def proses():

    # Dollar ke Rupiah
    if pilihanUser == 1:
        def dollar_ke_rupiah():
            dollar = float(input("Masukan Nominal Dollar : "))
            dollarRupiah = dollar * 15000
            print(f"Jadi {dollar} Dollar bernilai {rupiah.formatrupiah(int(dollarRupiah))}")
        dollar_ke_rupiah()

    # Rupiah ke Dollar
    elif pilihanUser == 2:
        def rupiah_ke_dollar():
            rupiah = float(input("Masukan Nominal Rupiah : "))
            rupiahDollar = rupiah / float(15000)
            print(f"Jadi {rupiah} Rupiah bernilai {round(rupiahDollar, 2)} Dollar")
        rupiah_ke_dollar()

    # Euro ke Rupiah
    elif pilihanUser == 3:
        def euro_ke_rupiah():
            euro = float(input("Masukan Nominal Euro : "))
            euroRupiah = euro * 16616
            print(f"Jadi {euro} Euro bernilai {rupiah.formatrupiah(int(euroRupiah))}")
        euro_ke_rupiah()

    # Rupiah ke Euro
    elif pilihanUser == 4:
        def rupiah_ke_euro():
            rupiah = float(input("Masukan Nominal Rupiah : "))
            rupiahEuro = rupiah / 16616  # Memperbaiki perhitungan di sini
            print(f"Jadi {rupiah} Rupiah bernilai {round(rupiahEuro, 2)} Euro")
        rupiah_ke_euro()

    # Riyal ke Rupiah
    elif pilihanUser == 5:
        def riyal_ke_rupiah():
            riyal = float(input("Masukan Nominal Riyal : "))
            riyalRupiah = riyal * 3817
            print(f"Jadi {riyal} Riyal bernilai {rupiah.formatrupiah(int(riyalRupiah))}")
        riyal_ke_rupiah()

    # Rupiah ke Riyal
    elif pilihanUser == 6:
        def rupiah_ke_riyal():
            rupiah = float(input("Masukan Nominal Rupiah : "))
            rupiahRiyal = rupiah / float(3817)
            print(f"Jadi {rupiah} Rupiah bernilai {round(rupiahRiyal, 2)} Riyal")
        rupiah_ke_riyal()

    # Berhenti
    elif pilihanUser == 7:
        # Jika tidak, maka tampilkan terima kasih dan keluar aplikasi
        print(
            colored("Baik, Terima Kasih telah menggunakan aplikasi kami :) ", "green")
        )
        exit()


# Menjalankan Proses Konversi
proses()

# Perulangan untuk mengulangi konversi
while input("Ulangi Konversi? [Y/T] ... ") == "Y":

    # Jika pengguna menginput "Y" maka lakukan Proses Konversi lagi.
    print("====================")
    proses()
    print("====================")

# Jika tidak, maka tampilkan terima kasih dan keluar aplikasi
print(colored("Baik, Terima Kasih telah menggunakan aplikasi kami :) ", "green"))
