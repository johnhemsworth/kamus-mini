"""
KAMUS MINI V7 = POS Tagging +  Migrasi Skema
--------------------------------------------
Fitur:
1) Cari arti dua arah (EN<>ID) dan tampilkan POS (part of speech).
2) Tambah entri baru: English, terjemahan Indonesia, dan POS (pilih/auto).
3) Lihat semua kosakata (urut abjad) dengan POS.
4) Edit: terjemahan atau POS.
5) Hapus Entri.
6) Persisten ke kamus.json(otomatis migrasi format lama -> baru).
Catatan:
- Struktur data disimpan sebagai:
    {
    "run": {"id": ["lari", "menjalankan"], "pos": "verb"},
    "beatiful": ("id":["indah", "cantik"], "pos": "adjective")
    }
- Jika kamu sudah punya kamus.json lama (format {eng: "indo"} atau {eng: ["indo", ...]}),
  program ini akan ***otomatis migrasi*** saat load.  
"""

import json
from pathlib import Path

DB_FILE = Path("kamus.json")

# ==========================
# POS Utilities & Heuristik
# ==========================
POS_SET = [
    "noun", "verb", "adjective", "adverb", 
    "pronoun", "preposition", "conjuction",
    "determiner","interjection" 
]

# Daftar kata fungsi umum untuk deteksi cepat
PRONOUNS = {"i","you","he","she","it","we","they","me","him","her","us","them","my","your","his","her","its","our","their","mine","yours","ours","theirs"}
PREPOSITIONS = {"in","on","at","by","for","with","from","to","of","about","over","under","between","into","through","during","before","after","above","below","without","within","across","behind","beyond"}
CONJUNCTIONS = {"and","or","but","so","yet","for","nor","although","because","since","unless","while","whereas","though"}
DETERMINERS = {"a","an","the","this","that","these","those","some","any","each","every","no","few","many","much","several","all","both","either","neither","my","your","his","her","its","our","their"}
INTERJECTIONS = {"oh","ah","wow","oops","hey","ouch","bravo","alas","yay","hurray","hmm","uh","um","er"}

AUXILIARY_VERBS = {"be","am","is","are","was","were","been","being","do","does","did","done","doing","have","has","had","having","will","would","shall","should","can","could","may","might","must"}

def bersihkan(s: str) -> str:
    "Normalisasi string: lowercase + strip spasi berlebihan."
    return " ".join(s.strip().lower().split())

def guess_pos(word: str) -> str:
    """
    Heuristik sederhana untuk menebak POS sebuah kata English.
    Aturan ringkas:
    - Kata fungsi (pronoun/preposition/conjunction/determiner/interjection) → sesuai daftar.
    - Sufiks -ly → adverb
    - Sufiks adj: -able,-ible,-al,-ful,-less,-ous,-ive,-ic → adjective
    - Sufiks noun: -ness,-ment,-tion,-sion,-ity,-ship,-er,-or → noun
    - Sufiks verb: -ize,-ise,-en → verb
    - Bentuk -ing,-ed → sering verb (atau adj), tebak "verb"
    - Auxiliary verbs → verb
    - Default → "noun"
    """
    w = bersihkan(word)

    w = bersihkan(word)

    if w in PRONOUNS: return "pronoun"
    if w in PREPOSITIONS: return "preposition"
    if w in CONJUNCTIONS: return "conjunction"
    if w in DETERMINERS: return "determiner"
    if w in INTERJECTIONS: return "interjection"

    if w in AUXILIARY_VERBS: return "verb"

    if w.endswith("ly"): return "adverb"
    if w.endswith(("able","ible","al","ful","less","ous","ive","ic")): return "adjective"
    if w.endswith(("ness","ment","tion","sion","ity","ship","er","or")): return "noun"
    if w.endswith(("ize","ise","en")): return "verb"
    if w.endswith(("ing","ed")): return "verb"

    return "noun"

# ========================
# Load/Save & Migrasi Data
# ========================
def load_kamus():
    """
    Baca kamus dari kamus.json
    - Jika file format lama: {eng: "indo"} atau {eng: [indo,...]} → MIGRASI ke format baru:
      {eng: {"id":[...], "pos":"<guess>"}}.
    - Jika file tidak ada → buat kamus default kecil.
    """

    if DB_FILE.exists():
        try:
            data = json.loads(DB_FILE.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            print("File JSON rusak. Membuat kamus baru.")
            data = {}

        #Deteksi format lama (value bukan dict), migrasi penuh
        migrated = {}
        if data and all(not isinstance(v, dict) for v in data.value()):
            for en, indo in data.items():
                # Pastikan list
                if isinstance(indo, list):
                    indo_list = [bersihkan(x) for x in indo]
                else:
                    indo_list = [bersihkan(indo)]
                migrated[bersihkan(en)] = {"id": indo_list, "pos" : guess_pos(en)}
            save_kamus(migrated)
            return migrated
        #Format baru atau campur
        result = {}
        for en, payload in data.items():
            if isinstance(payload, dict):
                id_list = payload.get("id", [])
                pos = payload.get("pos") or guess_pos(en)
                if not isinstance(id_list, list):
                    id_list = [id_list]
                result[bersihkan(en)] = {"id": [bersihkan(x) for x in id_list], "pos": bersihkan(pos)}
            else:
                # jika ada sisa format lama
                id_list = payload if isinstance(payload, list) else [payload]
                result[bersihkan(en)] = {"id": [bersihkan(x) for x in id_list], "pos": guess_pos(en)}

        return result
    # Kamus default jika file belum ada
    return {
        "cat": {"id": ["kucing"], "pos": "noun"},
        "dog": {"id": ["anjing"], "pos": "noun"},
        "run": {"id": ["lari", "menjalankan"], "pos": "verb"},
        "beautiful": {"id": ["indah", "cantik"], "pos": "adjective"},
        "quickly": {"id": ["dengan cepat"], "pos": "adverb"},
        "book": {"id": ["buku", "memesan"], "pos": "noun"},  # catatan: bisa verb juga
        "the": {"id": ["(artikel tertentu)"], "pos": "determiner"},
    }    
def save_kamus(kamus: dict):
    """Simpan ke kamus.json (rapi)"""
    DB_FILE.write_text(json.dumps(kamus, ensure_ascii=False, indent=2), encoding="utf-8")


#=======================
# Core Logic Kamus + POS
#=======================
def cari_dua_arah(kamus: dict, query: str):
   """
    Cari arti dua arah:
    - EN→ID: jika query ditemukan sebagai key English → tampilkan terjemahan & POS.
    - ID→EN: jika ditemukan di daftar Indonesia → tampilkan English yang cocok.
    """
   q = bersihkan(query)

   # English -Indonesia
   if q in kamus:
       payload = kamus[q] # {"id":[...], "pos":"..."}
       return ("EN→ID", q, payload["id"], payload["pos"])
   
   # Indonesia -> English (scan values)
   found_en = []
   for en, payload in kamus.items():
       if q in (bersihkan(x) for x in payload["id"]):
           found_en.append((en, payload["pos"]))
           
    if found_en:
        return ("ID→EN", q, found_en, None)

    return (None, q, None, None)

def tambah_entri(kamus: dict, eng: str, indo: str, pos_choice: str):
    """
    Tambahkan entri baru:
    - eng: kata/kalimat English 
    - indo: terjemahan Indonesia (tunggal; bisa ditambah lagi lewat edit)\
    - pos_choice: "auto: -> tebak; atau input manual (mis. "noun")
    """
    e = bersihkan(eng)
    i = bersihkan(indo)
    if not e or not i:
        print("Input tidak boleh kosong.")
        return False
    # Tentukan POS
    if pos_choice == "auto":
        pos = guess_pos(e)
    else:
        pos = bersihkan(pos_choice)
        if pos not in POS_SET:
            print(f"POS tidak valid. Pilih salah satuu: {','.join(POS_SET)}")
            return False
        
    # Tambah/mutakhirkan entri
    if e not in kamus:
        kamus[e] = {"id": [i], "pos": pos}
    else:
        # Tambah terjemahan jika belum ada
        if i not in (bersihkan(x) for x in kamus[e]["id"]):
            kamus[e]["id"].append(i)
        # Jangan timpa POS kalau sudah ada-kecuali user memilih non-auto
        if pos_choice != "auto":
            kamus[e]["pos"] = pos

    save_kamus(kamus)
    return True

def edit_entri(kamus: dict, eng: str):
    """
    Edit entri berdasarkan English:
    - Ganti seluruh terjemahan (list)
    - Tambah satu terjemahan
    - Hapus satu terjemahan
    - Ubah POS
    """
    e = bersihkan(eng)
    if e not in kamus:
        print("Entri English tidak ditemukan.")
        return
    
    print(f"\nEntri: {e}")
    print(f"Terjemahan sekarang: {kamus[e]['id']}")
    print(f"POS sekarang       : {kamus[e]['pos']}")
    print("1) Ganti seluruh daftar terjemahan")
    print("2) Tambah satu terjemahan")
    print("3) Hapus satu terjemahan")
    print("4) Ubah POS")
    pilih = input("Pilih (1/2/3/4): ").strip()

    if pilih == "1":
        baru = input("Masukan terjemahan (pisahkan koma): ")
        daftar = [bersihkan(x) for x in baru.split(",") if bersihkan(x)]
        if daftar:
            kamus[e]["id"] = daftar
            save_kamus(kamus)
            print("Terjemahan berhasil diganti.")
    elif pilih == "2":
        i = bersihkan(input("Masukan terjemahan baru: "))
        if i and i not in (bersihkan(x) for x in kamus[e]["id"]):
            kamus[e]["id"].append(i)
            save_kamus(kamus)
            print("Terjemahan berhasil ditambah.")
    elif pilih == "3":
        i = bersihkan(input("Masukkan terjemahan yang akan dihapus: "))
        baru = [x for x in kamus[e]["id"] if bersihkan(x) !=i]
        if len(baru) != len (kamus[e]["id"]):
            kamus[e]["id"] = baru
            save_kamus(kamus)
            print("Terjemahan berhasi dihapus.")
        else:
            print("Terjemahan tidak ditemukan.")
    elif pilih == "4":
        print(f"Pilihan POS: {', '}.join(POS_SET) atau 'auto'")
        pos_choice = bersihkan(input("Masukan POS baru: "))
        if pos_choice == "auto":
            kamus[e]["pos"] = guess_pos(e)
        elif pos_choice in POS_SET:
            kamus[e]["pos"] = guess_pos(e)
        elif pos_choice in POS_SET:
            kamus[e]["pos"] = pos_choice
        else:
            print("POS tidak valid.")
            return
        save_kamus(kamus)
        print("POS berhasil diubah.")
    else:
        print("Pilihan tidak valid.")

def hapus_entri(kamus: dict, eng: str):
    """Hapus entri english dari kamus."""
    e = bersihkan(eng)
    if e in kamus:
        konfirm = bersihkan(input(f"Yakin hapus '{e}'? (y/n): "))
        if konfirm == "y":
            kamus.pop(e)
            save_kamus(kamus)
            print("Berhasil dihapus.")
    else:
        print("Tidak ditemukan")

def tampilkan_semua(kamus: dict):
    """Cetak semua entri (EN -> ID) beserta POS."""
    if not kamus:
        print(f"(kamus kosong)")
        return
    print("\=== Daftar kosakata (English -> Indonesia)===")
    for en in sorted(kamus.keys()):
        pos = kamus[en]["pos"]
        indo = ", ".join(kamus[en]["id"])
        print(f"- {en} [{pos}] -> {indo}")

# ===============
# Program Utama UI
# ===============
def main():
    """ Loop menu interaktif."""
    kamus = load_kamus()
    print("=== Kamus mini V7 (EN->ID + POS) ===")

    while True:
        print("\nMenu:")
        print("1. Cari arti (auto EN-ID, tampilkan POS)")
        print("2. Tambah entri baru (pilih/auto POS)")
        print("3. Lihat semua kosakata")
        print("4. Edit entri (terjemahan/POS)")
        print("5. Hapus entri")
        print("6. Keluar.")
        pilihan = input("Pilih menu (1-6): ").strip()

        if pilihan == "1":
            q = input("Masukan kata/kalimat (English atau Indonesia): ")
            arah, kata, hasil, pos = cari_dua_arah(kamus, q)
            if arah == "EN→ID":
                print(f"{kata} [{pos}] → {', '.join(hasil)} ")
            elif arah == "ID→EN":
                # hasil: list of (en, pos)
                list

        


       