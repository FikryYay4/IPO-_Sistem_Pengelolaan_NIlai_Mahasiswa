# main.py

from utils import input_mahasiswa, tanya_lanjut, cek_status, hitung_rata, cetak_laporan

# Deklarasi variabel
daftar_mahasiswa = []
total_nilai = 0
jumlah_mahasiswa = 0

# Looping input data
while True:
    nim, nama, nilai = input_mahasiswa()
    status = cek_status(nilai)

    daftar_mahasiswa.append((nim, nama, nilai, status))
    total_nilai = total_nilai + nilai
    jumlah_mahasiswa = jumlah_mahasiswa + 1

    if not tanya_lanjut():
        break

# Hitung rata-rata
rata_kelas = hitung_rata(total_nilai, jumlah_mahasiswa)

# Tampilkan laporan
cetak_laporan(daftar_mahasiswa, rata_kelas)
