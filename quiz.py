import random

# Daftar operasi yang tersedia (dipakai untuk mode Campuran)
DAFTAR_OPERASI = ["Penjumlahan", "Pengurangan", "Perkalian", "Pembagian"]

# Rentang angka per tingkat kesulitan: (minimum, maksimum)
RENTANG = {
    "Mudah": {
        "tambah_kurang": (1, 20),
        "kali_a": (1, 5),
        "kali_b": (1, 10),
        "bagi_hasil": (1, 10),
        "bagi_pembagi": (2, 5),
    },
    "Sedang": {
        "tambah_kurang": (10, 100),
        "kali_a": (2, 9),
        "kali_b": (2, 12),
        "bagi_hasil": (2, 12),
        "bagi_pembagi": (2, 9),
    },
    "Sulit": {
        "tambah_kurang": (100, 999),
        "kali_a": (11, 25),
        "kali_b": (3, 15),
        "bagi_hasil": (5, 25),
        "bagi_pembagi": (6, 15),
    },
}

def buat_pilihan(jawaban):
    """Membuat 4 pilihan: 1 benar + 3 salah, urutannya diacak."""
    selisih_maks = max(5, jawaban // 5)   # semakin besar jawaban, semakin lebar variasi
    pilihan_salah = set()                 # set = kumpulan tanpa duplikat

    while len(pilihan_salah) < 3:
        arah = random.choice([-1, 1])     # -1 = lebih kecil, 1 = lebih besar
        kandidat = jawaban + arah * random.randint(1, selisih_maks)
        if kandidat >= 0 and kandidat != jawaban:
            pilihan_salah.add(kandidat)

    pilihan = list(pilihan_salah) + [jawaban]
    random.shuffle(pilihan)
    return pilihan


def buat_soal(operasi, kesulitan):
    """Membuat 1 soal. Mengembalikan dictionary: teks, jawaban, pilihan."""
    if operasi == "Campuran":
        operasi = random.choice(DAFTAR_OPERASI)

    r = RENTANG[kesulitan]

    if operasi == "Penjumlahan":
        a = random.randint(*r["tambah_kurang"])
        b = random.randint(*r["tambah_kurang"])
        simbol = "+"
        jawaban = a + b
    elif operasi == "Pengurangan":
        a = random.randint(*r["tambah_kurang"])
        b = random.randint(*r["tambah_kurang"])
        if a < b:
            a, b = b, a                   # tukar agar hasil tidak negatif
        simbol = "-"
        jawaban = a - b
    elif operasi == "Perkalian":
        a = random.randint(*r["kali_a"])
        b = random.randint(*r["kali_b"])
        simbol = "×"
        jawaban = a * b
    elif operasi == "Pembagian":
        b = random.randint(*r["bagi_pembagi"])
        jawaban = random.randint(*r["bagi_hasil"])
        a = b * jawaban                   # dibangun dari belakang → pasti habis dibagi
        simbol = "÷"
    else:
        raise ValueError(f"Operasi tidak dikenal: {operasi}")

    return {
        "teks": f"{a} {simbol} {b} = ?",
        "jawaban": jawaban,
        "pilihan": buat_pilihan(jawaban),
    }


def buat_daftar_soal(operasi, kesulitan, jumlah):
    """Membuat sejumlah soal tanpa soal yang sama persis."""
    daftar_soal = []
    teks_terpakai = []
    percobaan = 0

    while len(daftar_soal) < jumlah and percobaan < jumlah * 20:
        soal = buat_soal(operasi, kesulitan)
        if soal["teks"] not in teks_terpakai:
            daftar_soal.append(soal)
            teks_terpakai.append(soal["teks"])
        percobaan += 1

    return daftar_soal


# Blok ini hanya jalan jika file dijalankan langsung (python quiz.py)
if __name__ == "__main__":
    for soal in buat_daftar_soal("Campuran", "Mudah", 5):
        print(soal["teks"], soal["pilihan"], "→ jawaban:", soal["jawaban"])

    try:
        buat_soal("Akar", "Mudah")
    except ValueError as error:
        print("Error tertangkap:", error)