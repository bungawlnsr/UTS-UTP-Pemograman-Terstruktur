"""Modul testing: pengujian global memakai library unittest."""
import os
import tempfile
import unittest

try:
    # Dijalankan sebagai bagian package (python -m unittest kafe.testing)
    from .models import Pesanan, DaftarPesanan
    from .validasi import DataTidakValidError
    from . import processing, fileio
except ImportError:
    # Dijalankan langsung (tombol Run / python kafe/testing.py)
    import os
    import sys
    sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    from kafe.models import Pesanan, DaftarPesanan
    from kafe.validasi import DataTidakValidError
    from kafe import processing, fileio
    
class TestPesanan(unittest.TestCase):
    def test_subtotal(self):
        self.assertEqual(Pesanan("Latte", 25000, 2).subtotal(), 50000)

    def test_kwargs_atribut(self):
        p = Pesanan("Latte", 25000, 1, kategori="Kopi", topping="Oat milk")
        self.assertEqual(p.kategori, "Kopi")
        self.assertEqual(p.topping, "Oat milk")

    def test_harga_negatif_error(self):
        with self.assertRaises(DataTidakValidError):
            Pesanan("Latte", -100, 1)

    def test_jumlah_nol_error(self):
        with self.assertRaises(DataTidakValidError):
            Pesanan("Latte", 25000, 0)

    def test_menu_kosong_error(self):
        with self.assertRaises(DataTidakValidError):
            Pesanan("  ", 25000, 1)


class TestProcessing(unittest.TestCase):
    def setUp(self):
        self.daftar = [Pesanan("Latte", 25000, 2, kategori="Kopi"),
                       Pesanan("Roti Bakar", 15000, 1, kategori="Makanan"),
                       Pesanan("Latte", 25000, 3, kategori="Kopi")]

    def test_hitung_total_args(self):
        self.assertEqual(processing.hitung_total(1, 2, 3, 4), 10)

    def test_total_omzet(self):
        self.assertEqual(processing.total_omzet(self.daftar), 140000)

    def test_menu_terlaris(self):
        self.assertEqual(processing.menu_terlaris(self.daftar), ("Latte", 5))

    def test_pesanan_besar_keyword(self):
        hasil = processing.pesanan_besar(self.daftar, minimal=60000)
        self.assertEqual([p.jumlah for p in hasil], [3])

    def test_omzet_per_kategori(self):
        self.assertEqual(processing.omzet_per_kategori(self.daftar),
                         {"Kopi": 125000, "Makanan": 15000})

    def test_urutkan_lambda(self):
        dp = DaftarPesanan()
        for p in self.daftar:
            dp.tambah(p)
        self.assertEqual(dp.urutkan(turun=True)[0].jumlah, 3)


class TestFileIO(unittest.TestCase):
    def setUp(self):
        self.folder = tempfile.mkdtemp()
        self.path = os.path.join(self.folder, "data.txt")

    def test_mode_x_tidak_menimpa(self):
        self.assertTrue(fileio.buat_file_data(self.path, ["A;100;1"]))
        self.assertFalse(fileio.buat_file_data(self.path, ["B;200;2"]))
        self.assertEqual(len(fileio.baca_data(self.path)), 1)

    def test_baris_rusak_dilewati(self):
        fileio.buat_file_data(self.path, ["A;100;1", "B;abc;2", "C;-5;1", "D;50;3"])
        self.assertEqual([p.menu for p in fileio.baca_data(self.path)], ["A", "D"])

    def test_mode_a_menambah(self):
        fileio.buat_file_data(self.path, ["A;100;1"])
        fileio.tambah_pesanan(self.path, Pesanan("E", 300, 4))
        self.assertEqual(len(fileio.baca_data(self.path)), 2)

    def test_file_tidak_ada(self):
        self.assertEqual(fileio.baca_data(os.path.join(self.folder, "x.txt")), [])


if __name__ == "__main__":
    unittest.main()
