"""Modul validasi: pengecekan input dan data pesanan."""


class DataTidakValidError(Exception):
    """Exception buatan sendiri untuk data pesanan yang tidak valid."""


def validasi_pesanan(menu, harga, jumlah):
    """Memastikan data pesanan valid; memunculkan error jika tidak."""
    # Field nama menu tidak boleh kosong
    if not str(menu).strip():
        raise DataTidakValidError("Nama menu tidak boleh kosong")
    # Harga tidak boleh negatif
    if harga < 0:
        raise DataTidakValidError(f"Harga negatif untuk '{menu}': {harga}")
    # Jumlah pesanan minimal 1
    if jumlah < 1:
        raise DataTidakValidError(f"Jumlah pesanan '{menu}' minimal 1, bukan {jumlah}")


if __name__ == "__main__":
    # Pengujian lokal modul validasi
    validasi_pesanan("Latte", 25000, 2)
    try:
        validasi_pesanan("Latte", -1, 2)
    except DataTidakValidError as e:
        print("Error tertangkap:", e)
