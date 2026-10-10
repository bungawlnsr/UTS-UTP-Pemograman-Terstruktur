# Proyek Mandiri: Menu Kafe & Pesanan

## Struktur
```
proyek_kafe/
├── main.py                 # file utama
├── data_pesanan.txt        # data (dibuat mode 'x')
├── laporan_penjualan.txt   # laporan (ditulis mode 'w')
└── kafe/                   # package
    ├── __init__.py
    ├── models.py           # class Pesanan, DaftarPesanan
    ├── fileio.py           # baca / tulis / tambah file
    ├── processing.py       # perhitungan dan analisis
    ├── validasi.py         # validasi + exception buatan sendiri
    └── testing.py          # unittest (15 pengujian)
```

## Cara menjalankan
- Program   : `python main.py`
- Pengujian : `python -m unittest kafe.testing -v`

## Tabel Refactoring

| No | Sebelum (belum diperbaiki) | Sesudah (diperbaiki) | Teknik | Alasan |
|----|----------------------------|----------------------|--------|--------|
| 1 | Perhitungan omzet dan pencetakan laporan ditulis langsung di `main.py` dalam satu blok panjang | Dipindah ke fungsi `buat_laporan()` di `processing.py` | Extract function | Kode lebih pendek, bisa diuji terpisah, main.py hanya mengatur alur |
| 2 | Pengecekan `harga < 0`, `jumlah < 1`, nama kosong ditulis berulang di setiap tempat pesanan dibuat | Satu fungsi `validasi_pesanan()` di `validasi.py`, dipanggil dari `Pesanan.__init__` | Remove duplicate code | Aturan validasi ada di satu tempat, perubahan aturan cukup sekali |
| 3 | Variabel `m`, `h`, `j`, `d` untuk menu, harga, jumlah, daftar | Diganti `menu`, `harga`, `jumlah`, `daftar` | Rename variable | Kode mudah dibaca tanpa komentar tambahan |
| 4 | Angka batas pesanan besar `50000` ditulis langsung di fungsi (magic number) | Menjadi parameter `minimal=50000` (keyword argument) | Replace magic number with parameter | Batas bisa diubah per pemanggilan tanpa mengedit isi fungsi |
| 5 | Pesanan berupa list/tuple tanpa nama field (`p[1]` untuk harga) | Menjadi class `Pesanan` dengan atribut `harga`, `jumlah`, dll. | Replace data with class | Akses data lebih jelas dan aman |
