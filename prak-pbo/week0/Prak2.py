siswa = {}
jumlah_siswa = int(input('Masukkan jumlah siswa: '))

for i in range(1, jumlah_siswa + 1):
    nama = input(f'Masukkan nama siswa ke-{i}: ')
    nilai = int(input(f'Masukkan nilai untuk {nama}: '))
    siswa[nama] = nilai

print('dictionary =', siswa)