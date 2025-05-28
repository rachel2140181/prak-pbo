import random
import time

def print_separator():
    print("=" * 30)

def print_title():
    print_separator()
    print("     GAME MINESWEEPER 3x3")
    print_separator()
    print("Petunjuk:")
    print("Buka semua kotak kecuali yang berisi bom.")
    print("Simbol:")
    print("?  = Kotak belum dibuka")
    print("O  = Kotak kosong dan aman")
    print("X  = Kotak berisi BOM 💣")
    print_separator()

def init_game():
    board = [['?' for _ in range(3)] for _ in range(3)]
    bomb_position = (random.randint(0, 2), random.randint(0, 2))
    opened = set()
    return board, bomb_position, opened

def print_board(board):
    print("\nPapan saat ini:")
    for row in board:
        print(' '.join(row))
    print()

def check_win(opened):
    return len(opened) == 8 

def play_game():
    board, bomb_position, opened = init_game()
    bomb_row, bomb_col = bomb_position

    print_title()
    print_board(board)

    while True:
        try:
            row = int(input("Masukkan baris (0-2): "))
            col = int(input("Masukkan kolom (0-2): "))

            if not (0 <= row <= 2 and 0 <= col <= 2):
                print("Koordinat tidak valid. Masukkan angka antara 0 hingga 2.")
                continue

            if (row, col) in opened:
                print("Kotak ini sudah dibuka sebelumnya. Pilih kotak lain.")
                continue

            if (row, col) == bomb_position:
                board[row][col] = 'X'
                print_board(board)
                print("💥 Boom! Kamu membuka bom! Kamu kalah!")
                break
            else:
                board[row][col] = 'O'
                opened.add((row, col))
                print_board(board)

            if check_win(opened):
                print("🎉 Selamat! Kamu membuka semua kotak tanpa terkena bom!")
                break

        except ValueError:
            print("Masukkan angka yang valid (0, 1, atau 2).")

if __name__ == "__main__":
    play_game()