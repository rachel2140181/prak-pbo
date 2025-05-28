class TaskError(Exception):
    pass

def tambah_tugas(daftar_tugas):
    tugas = input("Masukkan tugas yang ingin ditambahkan: ").strip()
    if not tugas:
        raise TaskError("Input tugas tidak boleh kosong.")
    daftar_tugas.append(tugas)
    print("Tugas berhasil ditambahkan!")

def hapus_tugas(daftar_tugas):
    if not daftar_tugas:
        raise TaskError("Daftar tugas kosong, tidak ada yang bisa dihapus.")
    try:
        nomor = int(input("Masukkan nomor tugas yang ingin dihapus: "))
    except ValueError:
        raise TaskError("Input nomor tugas harus berupa angka.")
    if nomor < 1 or nomor > len(daftar_tugas):
        raise TaskError(f"Tugas dengan nomor {nomor} tidak ditemukan.")
    tugas_dihapus = daftar_tugas.pop(nomor - 1)
    print(f"Tugas '{tugas_dihapus}' berhasil dihapus.")

def tampilkan_tugas(daftar_tugas):
    if not daftar_tugas:
        print("Daftar tugas kosong.")
    else:
        print("Daftar Tugas:")
        for i, tugas in enumerate(daftar_tugas, start=1):
            print(f"- {i}. {tugas}")

def main():
    daftar_tugas = []
    while True:
        print("\nPilih aksi:")
        print("1. Tambah tugas")
        print("2. Hapus tugas")
        print("3. Tampilkan daftar tugas")
        print("4. Keluar")
        pilihan = input("Masukkan pilihan (1/2/3/4): ").strip()

        try:
            if pilihan == '1':
                tambah_tugas(daftar_tugas)
            elif pilihan == '2':
                hapus_tugas(daftar_tugas)
            elif pilihan == '3':
                tampilkan_tugas(daftar_tugas)
            elif pilihan == '4':
                print("Keluar dari program.")
                break
            else:
                print("Pilihan tidak valid. Masukkan 1, 2, 3, atau 4.")
        except TaskError as e:
            print("Error:", e)

if __name__ == "__main__":
    main()