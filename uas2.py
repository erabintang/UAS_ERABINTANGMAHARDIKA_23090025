nilai_mahasiswa = [
    [90, 80],
    [50, 60],
    [65, 70]
]

rata_rata_mata_kuliah = []
for i in range(len(nilai_mahasiswa[0])):
    total_nilai = sum(nilai_mahasiswa[j][i] for j in range(len(nilai_mahasiswa)))
    rata_rata = total_nilai / len(nilai_mahasiswa)
    rata_rata_mata_kuliah.append(rata_rata)

total_nilai_semua_mahasiswa = sum(sum(nilai) for nilai in nilai_mahasiswa)
jumlah_mahasiswa = len(nilai_mahasiswa)
rata_rata_semua_mahasiswa = total_nilai_semua_mahasiswa / (len(nilai_mahasiswa) * len(nilai_mahasiswa[0]))

print("Rata-rata nilai untuk setiap mata kuliah:")
for i, rata_rata in enumerate(rata_rata_mata_kuliah):
    print(f"Mata Kuliah {i+1}: {rata_rata:.2f}")

print(f"\nRata-rata nilai untuk semua mahasiswa: {rata_rata_semua_mahasiswa:.2f}")
