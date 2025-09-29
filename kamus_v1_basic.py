"""
KAMUS MINI V1 — Basic Lookup
Cara jalan: python kamus_v1_basic.py
"""


def main():
    kamus = {
        "cat": "kucing",
        "dog": "anjing",
        "book": "buku",
        "apple": "apel",
        "school": "sekolah",
        "Like": "suka",
    }
    kata = input("Masukkan kata (English): ").strip().lower()
    if kata in kamus:
        print(f"{kata} -> {kamus[kata]}")
    else:
        print("Kata tidak ada di kamus.")


if __name__ == "__main__":
    main()
