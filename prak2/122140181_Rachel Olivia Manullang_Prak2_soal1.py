class IsMahasiswa:
    def __init__(self, nim, nama, angkatan, is_mahasiswa=True):
        self.__nim = nim
        self.__nama = nama
        self.__angkatan = angkatan
        self.__is_mahasiswa = is_mahasiswa

    def get_nim(self):
        return self.__nim

    def get_nama(self):
        return self.__nama

    def set_nama(self, nama):
        self.__nama = nama

    def get_angkatan(self):
        return self.__angkatan

    def is_mahasiswa(self):
        return self.__is_mahasiswa

    def method_satu(self):
        # Contoh method pertama
        return f"Mahasiswa {self.__nama} dengan NIM {self.__nim} berada di angkatan {self.__angkatan}."

    def method_dua(self, tahun_sekarang):
        # Contoh method kedua
        if tahun_sekarang - self.__angkatan >= 4:
            return f"{self.__nama} sudah lulus karena sudah lebih dari 4 tahun berada di universitas."
        else:
            return f"{self.__nama} masih aktif sebagai mahasiswa."

    def method_tiga(self, status_mahasiswa):
        # Contoh method ketiga
        self.__is_mahasiswa = status_mahasiswa
        return f"Status mahasiswa {self.__nama} diubah menjadi {status_mahasiswa}."


# Inisialisasi objek pertama dengan semua parameter
mahasiswa1 = IsMahasiswa(nim="122140097", nama="ujang bedil", angkatan=2020)

# Inisialisasi objek kedua tanpa parameter is_mahasiswa
mahasiswa2 = IsMahasiswa(nim="122140098", nama="juan cargloss", angkatan=2021)

# Penggunaan method dan output
print(mahasiswa1.method_satu())
print(mahasiswa2.method_satu())

print(mahasiswa1.method_dua(2024))
print(mahasiswa2.method_dua(2024))

print(mahasiswa1.method_tiga(False))
print(mahasiswa2.method_tiga(True))