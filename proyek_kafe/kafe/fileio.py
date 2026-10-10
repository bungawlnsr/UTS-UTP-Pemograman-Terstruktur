"""Modul fileio: membaca, menulis, dan menambah data pada file."""
from .models import Pesanan
from .validasi import DataTidakValidError


def buat_file_data(nama_file, baris_awal):
    """Membuat file data pertama kali (mode 'x': gagal jika sudah ada,
    sehingga data lama tidak tertimpa)."""
    try:
        with open(nama_file, "x") as file:
            for baris in baris_awal:
                file.write(baris + "\n")
        return True
    except FileExistsError:
        print(f"Info: file {nama_file} sudah ada, tidak dibuat ulang")
        return False


def tambah_pesanan(nama_file, pesanan):
    """Menambah satu pesanan di akhir file (mode 'a': data lama aman)."""
    with open(nama_file, "a") as file:
        file.write(pesanan.ke_baris() + "\n")


def baca_data(nama_file):
    """Membaca file baris demi baris (mode 'r'). Baris rusak dilewati."""
    hasil = []
    try:
        with open(nama_file, "r") as file:
            for no, baris in enumerate(file, start=1):  # pembacaan iteratif
                baris = baris.strip()
                if not baris:
                    continue  # lewati baris kosong
                try:
                    bagian = baris.split(";")
                    menu, harga, jumlah = bagian[0], int(bagian[1]), int(bagian[2])
                    kategori = bagian[3] if len(bagian) > 3 else "-"
                    topping = bagian[4] if len(bagian) > 4 else "-"
                    hasil.append(Pesanan(menu, harga, jumlah_kategori=kategori, topping=topping))
                except (ValueError, IndexError, DataTidakValidError) as e:
                    # Baris rusak dilewati, program tetap lanjut
                    print(f"Baris {no} dilewati ({e})")
    except FileNotFoundError:
        print(f"Error: file {nama_file} belum ada. Buat dulu dengan mode 'x'.")
    return hasil


def tulis_laporan(nama_file, teks):
    """Menulis laporan ke file (mode 'w': laporan lama diganti)."""
    with open(nama_file, "w") as file:
        file.write(teks)


if __name__ == "__main__":
    # Pengujian lokal: file yang tidak ada
    print(baca_data("tidak_ada.txt"))
