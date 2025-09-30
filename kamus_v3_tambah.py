"""
KAMUS MINI V3 — Tambah Kata Baru
--------------------------------
Fitur:
1) Cari arti kata (EN -> ID).
2) Lihat semua kosakata.
3) Tambah kata baru.
4) Keluar.

Catatan:
- Kosakata disimpan hanya di memory (belum ke file).
- Jadi kalau program ditutup, data tambahan hilang.
"""


def tampilkan_semua(kamus: dict) -> None:
    """Cetak semua pasangan English -> Indonesia."""
    if not kamus:
        print("(Kamus kosong)")
        return
    print("\n=== Daftar Kosakata ===")
    for en in sorted(kamus):
        print(f"- {en} -> {kamus[en]}")


def tambah_entri(kamus: dict) -> None:
    """Tambah kata baru ke kamus (cek duplikat)."""
    en = input("Masukkan kata English: ").strip().lower()
    if en in kamus:
        print(f"'{en}' sudah ada di kamus dengan arti: {kamus[en]}")
    else:
        idn = input("Masukkan arti Indonesia: ").strip().lower()
        kamus[en] = idn
        print(f"Berhasil menambahkan: {en} -> {idn}")


def main():
    # Data awal sederhana
    kamus = {
        "cat": "kucing",
        "dog": "anjing",
        "book": "buku",
        "apple": "apel",
        "school": "sekolah",
    }

    print("=== Kamus Mini V3 ===")
    while True:
        print("\nMenu:")
        print("1. Cari arti (EN->ID)")
        print("2. Lihat semua kosakata")
        print("3. Tambah kata baru")
        print("4. Keluar")
        pilih = input("Pilih (1-4): ").strip()

        if pilih == "1":
            kata = input("Masukkan kata (English): ").strip().lower()
            arti = kamus.get(kata)
            if arti:
                print(f"{kata} -> {arti}")
            else:
                print("Kata tidak ada di kamus.")
        elif pilih == "2":
            tampilkan_semua(kamus)
        elif pilih == "3":
            tambah_entri(kamus)
        elif pilih == "4":
            print("Bye! Program selesai 😊")
            break
        else:
            print("Pilihan tidak valid.")


if __name__ == "__main__":
    main()
