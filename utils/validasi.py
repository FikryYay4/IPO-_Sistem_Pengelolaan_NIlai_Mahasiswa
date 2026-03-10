# utils/validasi.py

def input_mahasiswa():
    nim = input("Masukkan NIM   : ")
    nama = input("Masukkan Nama  : ")

    while True:
        try:
            nilai = float(input("Masukkan Nilai : "))
            if 0 <= nilai <= 100:
                break
            else:
                print("Nilai harus antara 0 - 100!")
        except ValueError:
            print("Nilai harus berupa angka!")

    return nim, nama, nilai


def tanya_lanjut():
    lagi = input("\nInput data lagi? (y/n): ")
    return lagi == "y"
