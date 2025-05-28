from abc import ABC, abstractmethod

class AnimalError(Exception):
    pass

class Animal(ABC):
    def __init__(self, name, age):
        self._set_name(name)
        self._set_age(age)
    
    def _get_name(self):
        return self._name
    
    def _set_name(self, name):
        if not name or not isinstance(name, str):
            raise AnimalError("Nama hewan harus berupa string dan tidak boleh kosong.")
        self._name = name

    def _get_age(self):
        return self._age
    
    def _set_age(self, age):
        if not isinstance(age, int) or age < 0:
            raise AnimalError("Usia hewan harus berupa bilangan bulat non-negatif.")
        self._age = age

    name = property(_get_name, _set_name)
    age = property(_get_age, _set_age)

    @abstractmethod
    def make_sound(self):
        pass

    def info(self):
        return f"Hewan: {self.name}, Usia: {self.age} tahun"

# Turunan kelas Animal

class Dog(Animal):
    def make_sound(self):
        return "Guk guk!"

class Cat(Animal):
    def make_sound(self):
        return "Meong!"

class Elephant(Animal):
    def make_sound(self):
        return "Trumpet!"

# Sistem manajemen kebun binatang

class Zoo:
    def __init__(self):
        self._animals = []

    def add_animal(self, animal):
        if not isinstance(animal, Animal):
            raise AnimalError("Hanya objek hewan yang dapat ditambahkan ke kebun binatang.")
        self._animals.append(animal)
        print(f"{animal.name} berhasil ditambahkan ke kebun binatang.")

    def show_all_sounds(self):
        if not self._animals:
            print("Kebun binatang kosong.")
            return
        for animal in self._animals:
            print(f"{animal.info()} bersuara: {animal.make_sound()}")

# Contoh penggunaan:

def main():
    zoo = Zoo()
    while True:
        print("\nMenu:")
        print("1. Tambah hewan")
        print("2. Tampilkan suara hewan")
        print("3. Keluar")
        pilihan = input("Pilih aksi (1/2/3): ").strip()

        try:
            if pilihan == '1':
                jenis = input("Masukkan jenis hewan (dog/cat/elephant): ").strip().lower()
                nama = input("Masukkan nama hewan: ").strip()
                usia = input("Masukkan usia hewan (angka): ").strip()

                if not usia.isdigit():
                    raise AnimalError("Usia harus berupa angka bulat non-negatif.")
                usia = int(usia)

                if jenis == 'dog':
                    hewan = Dog(nama, usia)
                elif jenis == 'cat':
                    hewan = Cat(nama, usia)
                elif jenis == 'elephant':
                    hewan = Elephant(nama, usia)
                else:
                    print("Jenis hewan tidak dikenali.")
                    continue

                zoo.add_animal(hewan)

            elif pilihan == '2':
                zoo.show_all_sounds()

            elif pilihan == '3':
                print("Keluar dari program.")
                break
            else:
                print("Pilihan tidak valid.")
        except AnimalError as e:
            print("Error:", e)

if __name__ == "__main__":
    main()