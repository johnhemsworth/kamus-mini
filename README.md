---
# 🐍 Mini Kamus EN ↔ ID

Proyek belajar Python dasar dengan membuat **kamus mini English ↔ Indonesia**.  
Dibangun **bertahap** dari level entry sampai fitur lebih lengkap.

![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python)
![Status](https://img.shields.io/badge/Status-Learning-green)
![Version](https://img.shields.io/badge/Version-v5%20Ready-orange)
![License](https://img.shields.io/badge/License-MIT-lightgrey)
![Made with Love](https://img.shields.io/badge/Made%20with-%E2%9D%A4-red)
![By Uncle John](https://img.shields.io/badge/By-Uncle%20John-blue)
---
## 🎯 Tujuan

- Latihan dasar Python: variabel, dictionary, loop, fungsi, file JSON, OOP.
- Belajar Git & GitHub workflow: commit, push, versioning.
- Membuat aplikasi nyata walau sederhana.

---

## 🚀 Versi & Progress

- ✅ **v1**: Basic lookup (EN → ID, sekali jalan)
- ✅ **v2**: Menu & loop (search/list/exit)
- ✅ **v3**: Tambah entri (in-memory)
- ✅ **v4**: Persistence JSON (save/load data)
- ✅ **v5**: Bilingual search (EN ↔ ID)
- 🔜 **v6**: Edit & hapus entri
- 🔜 **v7**: POS tagging (noun, verb, adj, adv)
- 🔜 **v8**: Migrasi schema + fitur lanjutan

---

## 🛠️ Cara Menjalankan

Clone repo & masuk ke folder:

```bash
git clone https://github.com/johnhemsworth/kamus-mini.git
cd kamus-mini


---
```

Jalankan program:

```
# versi 1
python kamus_v1_basic.py

# versi 2
python kamus_v2_menu.py

# versi 3
python kamus_v3_tambah.py

# versi 4 (persisten JSON)
python kamus_v4_persisten.py

# versi 5 (bilingual EN <-> ID)
python kamus_v5_bilingual.py


```

📖 Contoh Output (v5)

```
=== Kamus Mini V5 ===

Menu:
1. Cari arti (EN->ID)
2. Cari arti (ID->EN)
3. Lihat semua kosakata
4. Tambah kata baru
5. Keluar
Pilih (1-5): 2
Masukkan kata (Indonesia): rumah
rumah -> house

```

🗂️ Struktur Project

```
kamus-mini/
├── kamus_v1_basic.py       # versi 1, basic lookup
├── kamus_v2_menu.py        # versi 2, menu & loop
├── kamus_v3_tambah.py      # versi 3, tambah entri
├── kamus_v4_persisten.py   # versi 4, save/load JSON
├── kamus_v5_bilingual.py   # versi 5, bilingual EN<->ID
├── kamus.json              # file data kosakata
├── README.md               # dokumentasi project
└── .gitignore

```


## 🤝 Cara Fork & Kontribusi

1. Klik tombol **Fork** di kanan atas repo ini.
2. Repo akan tersalin ke akun GitHub kamu.
3. Clone repo hasil fork ke PC/laptop untuk belajar/modifikasi.
4. Kalau ingin kontribusi balik, buat **Pull Request (PR)** ke repo ini.


## 📌 Catatan

Project ini dibuat untuk **pembelajaran pribadi** (entry → intermediate).

Silakan **fork** / modifikasi sesuai kebutuhan 🚀

```

---

## 🔹 Cara Update di GitHub
```powershell
git add README.md
git commit -m "docs: update README with v5 bilingual feature"
git push

```
