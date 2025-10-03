# 🧠 Kamus Mini (Python Project)

> 📚 *Project pembelajaran Python dari level entry → intermediate.*

Kamus Mini ini adalah latihan nyata untuk belajar **Python dasar** hingga pengelolaan data menggunakan **file JSON**.
Setiap versi memperkenalkan fitur baru — dari yang sederhana hingga yang semakin canggih.

---

## 🚀 Versi & Fitur

|     Versi     | Fitur Utama    | Deskripsi                                                                            |
| :------------: | -------------- | ------------------------------------------------------------------------------------ |
|  **v1**  | Basic Lookup   | Pencarian arti kata sederhana (EN → ID).                                            |
|  **v2**  | Menu & Loop    | Program interaktif dengan menu pilihan.                                              |
|  **v3**  | Dua Arah       | Pencarian EN → ID dan ID → EN.                                                     |
|  **v4**  | Persisten JSON | Data disimpan otomatis ke file `kamus.json`.                                       |
|  **v5**  | Bilingual      | Terjemahan dua arah dengan update ke file JSON.                                      |
| 🆕**v6** | Edit & Delete  | Menambah, mengedit, dan menghapus entri dari kamus dengan data yang tetap tersimpan. |

---

## ⚙️ Cara Menjalankan

Pastikan sudah berada di folder project:

```
D:\Python\Project\2. Mini Kamus
```

Jalankan sesuai versi yang ingin digunakan:

```bash
# versi 1 - lookup sederhana
python kamus_v1_basic.py

# versi 2 - menu & loop
python kamus_v2_menu.py

# versi 3 - dua arah
python kamus_v3_bilingual.py

# versi 4 - simpan otomatis (JSON)
python kamus_v4_persisten.py

# versi 5 - kamus bilingual lengkap
python kamus_v5_bilingual.py

# versi 6 - edit & hapus entri
python kamus_v6_edit_delete.py
```

---

## 🧩 Struktur Data (contoh isi `kamus.json`)

```json
{
  "cat": "kucing",
  "dog": "anjing",
  "run": "lari",
  "book": "buku",
  "beautiful": "indah"
}
```

---

## 🧱 Contoh Output (V6)

```bash
=== Kamus Mini V6 ===

Menu:
1. Cari arti (EN->ID)
2. Lihat semua kosakata
3. Tambah kata baru
4. Edit entri
5. Hapus entri
6. Keluar
Pilih (1-6): 2

=== Daftar Kosakata ===
- cat -> kucing
- dog -> anjing
- book -> buku
```

---

## 🧠 Pembelajaran dari Project Ini

- ✅ Mengerti struktur `dict`, `list`, dan `loop` di Python
- ✅ Belajar **input/output interaktif**
- ✅ Menggunakan **file JSON** untuk penyimpanan data permanen
- ✅ Belajar konsep **CRUD (Create, Read, Update, Delete)**
- ✅ Latihan commit & version control menggunakan **Git + GitHub**

---

## 📌 Catatan

Project ini dibuat untuk **pembelajaran pribadi (entry → intermediate)**.
Silakan **fork / modifikasi / tambahkan fitur baru** sesuai kebutuhan 🚀

---

## 🧑‍💻 Author

**John Hemsworth**
📍 _“Belajar, Bangun, dan Berkarya — satu baris kode setiap hari.”_

---

## 🧾 Lisensi

Lisensi bebas digunakan untuk tujuan pembelajaran dan pengembangan pribadi.
Kredit tetap diberikan kepada pembuat asli bila digunakan secara publik 🙏
