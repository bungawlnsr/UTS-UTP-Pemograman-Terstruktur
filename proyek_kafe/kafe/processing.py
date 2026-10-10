"""Modul processing: perhitungan dan analisis data pesanan."""


def hitung_total(*nilai):
    """Menjumlahkan sejumlah nilai (*args)."""
    return sum(nilai)


def total_omzet(daftar):
    """Total omzet seluruh pesanan, memakai hitung_total(*args)."""
    return hitung_total(*[p.subtotal() for p in daftar])


def rata_subtotal(daftar):
    """Rata-rata subtotal per pesanan; 0 jika daftar kosong."""
    if not daftar:
        return 0
    return total_omzet(daftar) / len(daftar)


def jumlah_per_menu(daftar):
    """Menjumlahkan porsi terjual untuk tiap nama menu."""
    hasil = {}
    for p in daftar:
        hasil[p.menu] = hasil.get(p.menu, 0) + p.jumlah
    return hasil


def menu_terlaris(daftar):
    """Menu dengan porsi terjual terbanyak (lambda sebagai key)."""
    terjual = jumlah_per_menu(daftar)
    if not terjual:
        return None
    nama = max(terjual, key=lambda m: terjual[m])
    return nama, terjual[nama]


def pesanan_besar(daftar, minimal=50000):
    """Pesanan dengan subtotal di atas atau sama dengan minimal (filter + lambda)."""
    return list(filter(lambda p: p.subtotal() >= minimal, daftar))


def omzet_per_kategori(daftar):
    """Total omzet untuk tiap kategori."""
    hasil = {}
    for p in daftar:
        hasil[p.kategori] = hasil.get(p.kategori, 0) + p.subtotal()
    return hasil


def buat_laporan(daftar, minimal=50000):
    """Menyusun teks laporan penjualan dari daftar pesanan."""
    baris = ["LAPORAN PENJUALAN KAFE", "=" * 44]
    for p in daftar:
        baris.append(f"{p.menu:<16} Rp{p.harga:>7,} x {p.jumlah:>2} = Rp{p.subtotal():>9,}")
    baris.append("=" * 44)
    baris.append(f"Jumlah pesanan      : {len(daftar)}")
    baris.append(f"Total omzet         : Rp{total_omzet(daftar):,}")
    baris.append(f"Rata-rata pesanan   : Rp{rata_subtotal(daftar):,.0f}")
    terlaris = menu_terlaris(daftar)
    if terlaris:
        baris.append(f"Menu terlaris       : {terlaris[0]} ({terlaris[1]} porsi)")
    besar = [p.menu for p in pesanan_besar(daftar, minimal=minimal)]
    baris.append(f"Pesanan >= Rp{minimal:,}: " + (", ".join(besar) or "tidak ada"))
    for kat, omzet in omzet_per_kategori(daftar).items():
        baris.append(f"Omzet {kat:<12}: Rp{omzet:,}")
    return "\n".join(baris) + "\n"


if __name__ == "__main__":
    # Pengujian lokal modul processing
    assert hitung_total(1, 2, 3) == 6
    print("processing OK")
