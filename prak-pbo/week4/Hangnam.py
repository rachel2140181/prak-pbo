import random

def tampilkan_judul():
    print("=" * 40)
    print("         GAME HANGMAN SEDERHANA")
    print("=" * 40)
    print("Tebak kata dengan menebak huruf satu per satu.")
    print("Jika tebakanmu salah terus, kamu akan kalah.")
    print()

def buat_daftar_kata():
    return ["komputer", "python", "hangman", "terminal", "kucing", "gajah", "program"]

def pilih_kata_acak(daftar):
    return random.choice(daftar)

def tampilkan_gambar_hangman(jumlah_salah):
    gambar = [
        """
           +---+
               |
               |
               |
              ===""",
        """
           +---+
           O   |
               |
               |
              ===""",
        """
           +---+
           O   |
           |   |
               |
              ===""",
        """
           +---+
           O   |
          /|   |
               |
              ===""",
        """
           +---+
           O   |
          /|\\  |
               |
              ===""",
        """
           +---+
           O   |
          /|\\  |
          /    |
              ===""",
        """
           +---+
           O   |
          /|\\  |
          / \\  |
              ==="""
    ]
    print(gambar[jumlah_salah])

def tampilkan_kata(kata_rahasia, huruf_tertebak):
    hasil = ""
    for huruf in kata_rahasia:
        if huruf in huruf_tertebak:
            hasil += huruf + " "
        else:
            hasil += "_ "
    print("Kata: " + hasil.strip())

def cek_menang(kata_rahasia, huruf_tertebak):
    for huruf in kata_rahasia:
        if huruf not in huruf_tertebak:
            return False
    return True

def main():
    tampilkan_judul()
    daftar_kata = buat_daftar_kata()
    kata_rahasia = pilih_kata_acak(daftar_kata)
    huruf_tertebak = []
    jumlah_salah = 0
    max_salah = 6

    while True:
        tampilkan_gambar_hangman(jumlah_salah)
        tampilkan_kata(kata_rahasia, huruf_tertebak)
        print("Huruf yang sudah ditebak:", " ".join(huruf_tertebak))
        print(f"Sisa kesempatan: {max_salah - jumlah_salah}")
        print()

        tebakan = input("Masukkan huruf tebakanmu: ").lower()

        if len(tebakan) != 1 or not tebakan.isalpha():
            print("⚠️ Masukkan hanya satu huruf alfabet.\n")
            continue

        if tebakan in huruf_tertebak:
            print("⚠️ Kamu sudah menebak huruf itu.\n")
            continue

        huruf_tertebak.append(tebakan)

        if tebakan not in kata_rahasia:
            jumlah_salah += 1
            print("❌ Tebakan salah!\n")
        else:
            print("✅ Tebakan benar!\n")

        if cek_menang(kata_rahasia, huruf_tertebak):
            tampilkan_kata(kata_rahasia, huruf_tertebak)
            print("🎉 Selamat! Kamu berhasil menebak kata dengan benar!")
            break

        if jumlah_salah >= max_salah:
            tampilkan_gambar_hangman(jumlah_salah)
            print("💀 Kamu kalah! Kata yang benar adalah:", kata_rahasia)
            break

if __name__ == "__main__":
    main()