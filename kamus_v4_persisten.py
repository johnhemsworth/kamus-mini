"""
KAMUS MINI V4 — Persisten JSON
------------------------------
Fitur:
1) Cari arti kata (EN -> ID).
2) Lihat semua kosakata.
3) Tambah kata baru.
4) Keluar (data otomatis tersimpan).

Catatan:
- Data kosakata disimpan di file kamus.json
- Kalau file belum ada, program akan membuat file baru dengan data awal.
"""

import json
from pathlib import Path

DB_FILE = Path("kamus.json")


def load_kamus() -> dict:
    """Baca kamus dari file JSON (atau buat default kalau belum ada)."""
    if DB_FILE.exists():
        try:
            with open(DB_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except json.JSONDecodeError:
            print("File JSON rusak, membuat kamus baru...")
            return {}
    else:
        # Data default awal
        return {
            "cat": "kucing",
            "dog": "anjing",
            "book": "buku",
            "apple": "apel",
            "school": "sekolah",
        }


def save_kamus(kamus: dict) -> None:
    """Simpan kamus ke file JSON dengan format rapi."""
    with open(DB_FILE, "w", encoding="utf-8") as f:
        json.dump(kamus, f, ensure_ascii=False, indent=2)


def tampilkan_semua(kamus: dict) -> None:
    """Cetak semua kosakata."""
    if not kamus:
        print("(Kamus kosong)")
        return
    print("\n=== Daftar Kosakata ===")
    for en in sorted(kamus):
        print(f"- {en} -> {kamus[en]}")


def tambah_entri(kamus: dict) -> None:
    """Tambah kata baru ke kamus."""
    en = input("Masukkan kata English: ").strip().lower()
    if en in kamus:
        print(f"'{en}' sudah ada di kamus dengan arti: {kamus[en]}")
    else:
        idn = input("Masukkan arti Indonesia: ").strip().lower()
        kamus[en] = idn
        save_kamus(kamus)
        print(f"Berhasil menambahkan: {en} -> {idn}")


def main():
    kamus = load_kamus()
    print("=== Kamus Mini V4 ===")
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
            save_kamus(kamus)
            print("Bye! Data tersimpan di kamus.json 😊")
            break
        else:
            print("Pilihan tidak valid.")


if __name__ == "__main__":
    main()
