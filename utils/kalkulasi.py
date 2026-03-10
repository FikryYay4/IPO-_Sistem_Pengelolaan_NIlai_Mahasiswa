# utils/kalkulasi.py

def cek_status(nilai):
    if nilai >= 60:
        return "Lulus"
    else:
        return "Tidak Lulus"


def hitung_rata(total_nilai, jumlah_mhs):
    rata = total_nilai / jumlah_mhs
    return rata
