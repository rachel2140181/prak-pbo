import math

while True:
    try:
        angka = input("Masukkan angka: ")
        nilai = float(angka)

        if nilai < 0:
            print("Input tidak valid. Harap masukkan angka positif.")
            continue
        elif nilai == 0:
            raise ValueError("Error: Akar kuadrat dari nol tidak diperbolehkan.")
        
        akar = math.sqrt(nilai)
        print(f"Akar kuadrat dari {nilai} adalah {akar}")
        break 

    except ValueError as e:
        pesan = str(e)
        if pesan == "could not convert string to float: '{}'".format(angka):
            print("Input tidak valid. Harap masukkan angka yang valid.")
        else:
            print(pesan)