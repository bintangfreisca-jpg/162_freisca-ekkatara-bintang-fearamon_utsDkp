"""
Kelompok C - Instrumentasi
Monitoring Level Tangki

Aturan status:
    Level < 30%             -> LOW
    30% <= Level <= 80%     -> NORMAL
    Level > 80%             -> HIGH
"""

# 15 data inti (%)
data_inti = [18, 25, 33, 41, 55, 62, 76, 84, 91, 47, 29, 38, 70, 82, 15]

# 5 data tambahan mahasiswa (uji batas kategori dan variasi nilai)
data_tambahan = [30, 80, 29.9, 80.1, 100]

# Total tepat 20 data
data_level = data_inti + data_tambahan


def status_level(level):
    """Mengembalikan status tangki berdasarkan level (%)."""
    if level < 30:
        return "LOW"
    elif level <= 80:
        return "NORMAL"
    else:
        return "HIGH"


def hitung_kategori(data):
    """Menghitung jumlah data pada tiap kategori status."""
    jumlah = {"LOW": 0, "NORMAL": 0, "HIGH": 0}
    for level in data:
        jumlah[status_level(level)] += 1
    return jumlah


def rata_rata(data):
    """Menghitung nilai rata-rata data."""
    if len(data) == 0:
        return 0
    return sum(data) / len(data)


def main():
    assert len(data_inti) == 15, "Data inti harus 15"
    assert len(data_tambahan) == 5, "Data tambahan harus 5"
    assert len(data_level) == 20, "Total data harus tepat 20"

    print("=" * 40)
    print("   MONITORING LEVEL TANGKI")
    print("=" * 40)
    print(f"{'No':<4}{'Level (%)':<12}{'Status':<8}Keterangan")
    print("-" * 40)

    for i, level in enumerate(data_level, start=1):
        ket = "inti" if i <= 15 else "tambahan"
        print(f"{i:<4}{level:<12}{status_level(level):<8}{ket}")

    print("-" * 40)
    kategori = hitung_kategori(data_level)
    print("Jumlah per kategori (20 data):")
    for nama, jumlah in kategori.items():
        print(f"  {nama:<7}: {jumlah}")

    print(f"Total data     : {len(data_level)}")
    print(f"Rata-rata level: {rata_rata(data_level):.2f} %")

    print("\nRingkasan 15 data inti saja:")
    print(f"  Kategori  : {hitung_kategori(data_inti)}")
    print(f"  Rata-rata : {rata_rata(data_inti):.2f} %")


if __name__ == "__main__":
    main()