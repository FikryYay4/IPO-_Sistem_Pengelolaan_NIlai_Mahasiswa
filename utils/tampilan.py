# utils/tampilan.py

def cetak_laporan(daftar_mahasiswa, rata_kelas):
    print("\n========================================")
    print("       DAFTAR NILAI MAHASISWA           ")
    print("========================================")
    print(f"{'NIM':<12} {'Nama':<15} {'Nilai':<8} {'Status'}")
    print("-" * 40)

    for data in daftar_mahasiswa:
        nim, nama, nilai, status = data
        print(f"{nim:<12} {nama:<15} {nilai:<8} {status}")

    print("-" * 40)
    print(f"Rata-rata Kelas : {rata_kelas:.2f}")
    print("========================================")
