"""Modul models: berisi class Pesanan dan DaftarPesanan."""
try:
    # Dijalankan sebagai bagian package (diimpor)
    from .validasi import validasi_pesanan
except ImportError:
    # Dijalankan langsung (tombol Run / python kafe/models.py)
    import os
    import sys
    sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    from kafe.validasi import validasi_pesanan

class Pesanan:
    """Satu baris pesanan. Atribut tambahan diterima lewat **kwargs."""

    def __init__(self, menu, harga, jumlah, **kwargs):
        validasi_pesanan(menu, harga, jumlah)  # tolak data tidak valid
        self.menu = menu.strip()
        self.harga = harga
        self.jumlah = jumlah
        # **kwargs: atribut bervariasi, contoh kategori / topping
        self.kategori = kwargs.get("kategori", "-")
        self.topping = kwargs.get("topping", "-")

    def subtotal(self):
        """Subtotal pesanan = harga x jumlah."""
        return self.harga * self.jumlah

    def ke_baris(self):
        """Mengubah objek menjadi satu baris teks untuk disimpan ke file."""
        return f"{self.menu};{self.harga};{self.jumlah};{self.kategori};{self.topping}"


class DaftarPesanan:
    """Kumpulan pesanan beserta operasi dasarnya."""

    def __init__(self):
        self.data = []

    def tambah(self, pesanan):
        """Menambah pesanan ke daftar."""
        assert isinstance(pesanan, Pesanan), "Yang ditambahkan harus objek Pesanan"
        self.data.append(pesanan)

    def cari(self, menu):
        """Mencari pesanan pertama dengan nama menu tertentu."""
        for p in self.data:
            if p.menu.lower() == menu.lower():
                return p
        return None

    def urutkan(self, turun=False):
        """Mengurutkan pesanan berdasarkan subtotal (lambda sebagai key)."""
        return sorted(self.data, key=lambda p: p.subtotal(), reverse=turun)

    def jumlah_pesanan(self):
        """Banyaknya baris pesanan."""
        return len(self.data)
