"""
Monitoring Level Tangki
Nama  : Freisca Ekkatara Bintang F.
NIM   : 03041382631162
Kampus: B Palembang
Prodi : Teknik Elektro
"""

# 15 data inti sesuai soal
DATA_INTI = [18, 25, 33, 41, 55, 62, 76, 84, 91, 47, 29, 38, 70, 82, 15]

# 5 data tambahan realistis untuk menguji batas kategori dan variasi nilai.
# 0% dan 100% mewakili tangki kosong/penuh; 30% dan 80% menguji
# batas NORMAL; 50% mewakili kondisi isi sedang.
DATA_TAMBAHAN = [0, 30, 50, 80, 100]

def status_level(level):
    """Mengembalikan status level: LOW, NORMAL, atau HIGH."""
    if not isinstance(level, (int, float)) or isinstance(level, bool):
        raise TypeError("Level harus berupa angka.")
    if not 0 <= level <= 100:
        raise ValueError("Level tangki harus berada pada rentang 0 sampai 100%.")
    if level < 30:
        return "LOW"
    elif level <= 80:
        return "NORMAL"
    return "HIGH"


def hitung_kategori(data):
    """Menghitung jumlah data pada setiap kategori status."""
    kategori = {"LOW": 0, "NORMAL": 0, "HIGH": 0}
    for level in data:
        kategori[status_level(level)] += 1
    return kategori


def rata_rata(data):
    """Menghitung rata-rata level; data kosong ditolak."""
    if not data:
        raise ValueError("Data tidak boleh kosong.")
    # Validasi seluruh elemen melalui fungsi status_level.
    for level in data:
        status_level(level)
    return sum(data) / len(data)


def main():
    seluruh_data = DATA_INTI + DATA_TAMBAHAN

    print("MONITORING LEVEL TANGKI")
    print("Nama   : Freisca Ekkatara Bintang F.")
    print("NIM    : 03041382631162")
    print("Kampus : B Palembang")
    print("Prodi  : Teknik Elektro")
    print("-" * 55)
    print(f"Jumlah data inti       : {len(DATA_INTI)}")
    print(f"Jumlah data tambahan   : {len(DATA_TAMBAHAN)}")
    print(f"Total data pengamatan  : {len(seluruh_data)}")
    print("\nRINCIAN STATUS SETIAP DATA")
    for nomor, level in enumerate(seluruh_data, start=1):
        sumber = "Inti" if nomor <= len(DATA_INTI) else "Tambahan"
        print(f"{nomor:02d}. {level:>5}% -> {status_level(level):<6} ({sumber})")

    print("\nREKAPITULASI")
    for status, jumlah in hitung_kategori(seluruh_data).items():
        print(f"{status:<7}: {jumlah} data")
    print(f"Rata-rata level tangki : {rata_rata(seluruh_data):.2f}%")


if __name__ == "__main__":
    main()
