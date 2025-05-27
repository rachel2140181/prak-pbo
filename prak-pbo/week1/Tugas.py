import random

class Robot:
    def __init__(self, name, serang, hp, akurasi=0.8):
        self.name = name
        self.serang = serang
        self.hp = hp
        self.akurasi = akurasi

    def serang_musuh(self, musuh):
        if random.random() < self.akurasi:  # Attack only hits if within akurasi
            dmg = random.randint(1, self.serang)
            musuh.hp = max(0, musuh.hp - dmg)
            print(f"{self.name} hits {musuh.name} for {dmg} dmg. {musuh.name} HP: {musuh.hp}")
        else:
            print(f"{self.name} missed the serang on {musuh.name}!")

    def regen(self, amount=5):
        self.hp += amount
        print(f"{self.name} regenerates {amount} HP. Current HP: {self.hp}")

    def msh_hidup(self):
        return self.hp > 0


class Game:
    def __init__(self, robot1, robot2, batas_ronde=10):
        self.robot1 = robot1
        self.robot2 = robot2
        self.batas_ronde = batas_ronde

    def start(self):
        ronde = 1
        while ronde <= self.batas_ronde and self.robot1.msh_hidup() and self.robot2.msh_hidup():
            print(f"\n--- Round {ronde} ---")
            if random.choice([True, False]):
                self.robot1.serang_musuh(self.robot2)
            else:
                self.robot2.serang_musuh(self.robot1)
            ronde += 1
        self.show_result()

    def show_result(self):
        if self.robot1.msh_hidup() and not self.robot2.msh_hidup():
            print(f"{self.robot1.name} wins!")
        elif self.robot2.msh_hidup() and not self.robot1.msh_hidup():
            print(f"{self.robot2.name} wins!")
        else:
            print("The battle ended in a draw!")


# Input manual untuk robot
def create_robot(num):
    name = input(f"Masukkan nama Robot {num}: ")
    serang = int(input("Masukkan nilai serangan (serang): "))
    hp = int(input("Masukkan nilai HP: "))
    akurasi = float(input("Masukkan akurasi serangan (0.0 - 1.0): "))
    return Robot(name, serang, hp, akurasi)

robot1 = create_robot(1)
robot2 = create_robot(2)
batas_ronde = int(input("Masukkan jumlah maksimal ronde: "))

game = Game(robot1, robot2, batas_ronde)
game.start()