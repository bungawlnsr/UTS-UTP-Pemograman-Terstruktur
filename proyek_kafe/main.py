"""File utama: menjalankan alur program pesanan kafe."""
from kafe import Pesanan, DaftarPesanan
from kafe import fileio, processing

FILE_DATA = "data_pesanan.txt"
FILE_LAPORAN = "laporan_penjualan.txt"

# Data awal; sengaja ada 3 baris rusak untuk menguji penanganan error
DATA_AWAL = [
    "Latte;25000;2;Kopi;Oat milk",
    "Americano;20000;3;Kopi;-",
    "Roti Bakar;15000;1;Makanan;Cokelat",
    "Matcha;28000;abc;Non-Kopi;-",       # jumlah bukan angka
    "Croissant;-18000;2;Makanan;-",      # harga negatif
    ";22000;1;Kopi;-",                   # nama menu kosong
    "Latte;25000;3;Kopi;-",
    "Nasi Goreng;35000;2;Makanan;Telur",
]


def main():
    # 1. Buat file data pertama kali (mode x)
    fileio.buat_file_data(FILE_DATA, DATA_AWAL)

    # 2. Tambah pesanan baru (mode a), memakai **kwargs dan keyword argument
    fileio.tambah_pesanan(FILE_DATA, Pesanan("Es Teh", 8000, 4, kategori="Non-Kopi", topping="Lemon"))

    # 3. Baca data (mode r), baris rusak dilewati
    dp = DaftarPesanan()
    for p in fileio.baca_data(FILE_DATA):
        dp.tambah(p)

    # 4. Olah data dan tulis laporan (mode w)
    teks = processing.buat_laporan(dp.data, minimal=50000)
    fileio.tulis_laporan(FILE_LAPORAN, teks)

    # 5. Tampilkan laporan di layar
    print(teks)


if __name__ == "__main__":
    main()
