data = []
def input_data():
    nim = input("Masukkan NIM: ")
    nama = input("Masukkan Nama: ")
    data.append((nim, nama))

def tampilkan_data():
    print("\nData Mahasiswa:")
    for nim, nama in data:
        print(f"NIM: {nim}, Nama: {nama}")

while True:
    input_data()
    tambah_lagi = input("Ingin tambah lagi? (ya/tidak): ")
    if tambah_lagi.lower() != "ya":
        break

tampilkan_data()
