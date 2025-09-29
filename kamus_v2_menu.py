"""
KAMUS MINI V2 — Menu & Loop
Tujuan:
- Program bisa dipakai berkali-kali (loop).
- Tambahkan menu sederhana: cari arti, lihat semua, keluar.
"""


def tampilkan_semua(kamus: dict) -> None:
    """Cetak semua pasangan English -> Indonesia."""
    if not kamus:
        print("(Kamus kosong)")
        return
    print("\n=== Daftar Kosakata ===")
    for en in sorted(kamus):
        print(f"- {en} -> {kamus[en]}")


def main():
    # Data awal sederhana
    kamus = {
        "cat": "kucing",
        "dog": "anjing",
        "like": "suka",
        "book": "buku",
        "run": "lari",
        "eat": "makan",
        "drink": "minum",
        "beautiful": "indah",
        "fast": "cepat",
        "happy": "bahagia",
    }

    print("=== Kamus Mini V2 ===")
    while True:
        print("\nMenu:")
        print("1. Cari arti (EN->ID)")
        print("2. Lihat semua kosakata")
        print("3. Keluar")
        pilih = input("Pilih (1-3): ").strip()

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
            print("Bye!")
            break
        else:
            print("Pilihan tidak valid.")


if __name__ == "__main__":
    main()
