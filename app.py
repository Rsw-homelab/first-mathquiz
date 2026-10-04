from pathlib import Path

import streamlit as st
import quiz   # ← file quiz.py buatan kita sendiri

st.set_page_config(
    page_title="MathQuiz",
    page_icon="🧮",
    layout="centered",
)


def muat_css(nama_file):
    """Membaca file CSS lalu memasangnya ke halaman."""
    lokasi = Path(__file__).parent / nama_file
    try:
        css = lokasi.read_text(encoding="utf-8")
        st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)
    except FileNotFoundError:
        st.warning(f"File {nama_file} tidak ditemukan, memakai tampilan bawaan.")


muat_css("style.css")

# Halaman awal saat aplikasi pertama dibuka
if "halaman" not in st.session_state:
    st.session_state.halaman = "home"


def mulai_quiz(operasi, kesulitan, jumlah):
    """Membuat soal baru dan mereset semua data quiz."""
    st.session_state.daftar_soal = quiz.buat_daftar_soal(operasi, kesulitan, jumlah)
    st.session_state.nomor = 0
    st.session_state.skor = 0
    st.session_state.sudah_jawab = False
    st.session_state.jawaban_user = None
    st.session_state.halaman = "quiz"

def tampilkan_home():
    st.title("🧮 MathQuiz")
    st.write("Latihan matematika seru! Pilih pengaturanmu dulu ya 👇")

    operasi = st.selectbox(
        "Jenis operasi",
        ["Penjumlahan", "Pengurangan", "Perkalian", "Pembagian", "Campuran"],
    )
    kesulitan = st.radio("Kesulitan", ["Mudah", "Sedang", "Sulit"], horizontal=True)
    jumlah = st.radio("Jumlah soal", [5, 10, 20], horizontal=True)

    if st.button("🚀 Mulai Quiz", type="primary", use_container_width=True):
        mulai_quiz(operasi, kesulitan, jumlah)
        st.rerun()

def tampilkan_quiz():
    s = st.session_state                      # nama pendek supaya kode ringkas
    total = len(s.daftar_soal)
    soal = s.daftar_soal[s.nomor]             # soal yang sedang aktif

    # Progress bar: terisi saat soal dijawab
    selesai = s.nomor + (1 if s.sudah_jawab else 0)
    st.progress(selesai / total)
    st.caption(f"Soal {s.nomor + 1} dari {total}  |  ⭐ Skor: {s.skor}")

    st.header(soal["teks"])

    # Tombol pilihan jawaban A-D
    huruf = ["A", "B", "C", "D"]
    for i, pilihan in enumerate(soal["pilihan"]):
        if st.button(
            f"{huruf[i]}.  {pilihan}",
            key=f"pilihan_{s.nomor}_{i}",
            disabled=s.sudah_jawab,
            use_container_width=True,
        ):
            s.jawaban_user = pilihan
            s.sudah_jawab = True
            if pilihan == soal["jawaban"]:
                s.skor += 1
            st.rerun()

    # Feedback + tombol lanjut (hanya muncul setelah menjawab)
    if s.sudah_jawab:
        if s.jawaban_user == soal["jawaban"]:
            st.success("🎉 Benar!")
        else:
            st.error(f"❌ Salah. Jawaban yang benar adalah {soal['jawaban']}")

        if s.nomor + 1 < total:
            label = "Lanjut ➡️"
        else:
            label = "Lihat Hasil 🏁"

        if st.button(label, key="lanjut", type="primary", use_container_width=True):
            s.nomor += 1
            s.sudah_jawab = False
            s.jawaban_user = None
            if s.nomor >= total:
                s.halaman = "hasil"
            st.rerun()

def tampilkan_hasil():
    s = st.session_state
    total = len(s.daftar_soal)
    benar = s.skor
    salah = total - benar
    persen = round(benar / total * 100)

    st.title("Quiz Selesai! 🎉")

    kolom1, kolom2, kolom3 = st.columns(3)
    kolom1.metric("Total", total)
    kolom2.metric("✅ Benar", benar)
    kolom3.metric("❌ Salah", salah)

    st.subheader(f"Nilai: {persen}/100")

    if persen >= 80:
        st.success("Hebat! Terus berlatih! 🌟")
        st.balloons()
    elif persen >= 60:
        st.info("Bagus! Sedikit lagi sempurna 💪")
    else:
        st.warning("Jangan menyerah, ayo coba lagi! 📚")

    if st.button("🔄 Main Lagi", type="primary", use_container_width=True):
        s.halaman = "home"
        st.rerun()


# ---------- PENGATUR HALAMAN (paling bawah) ----------
if st.session_state.halaman == "home":
    tampilkan_home()
elif st.session_state.halaman == "quiz":
    tampilkan_quiz()
else:
    tampilkan_hasil()

