import random

class Father:
    def __init__(self, blood_types):
        self.blood_types = blood_types

class Mother:
    def __init__(self, blood_types):
        self.blood_types = blood_types

class Child:
    def __init__(self, father, mother):
        self.father_allel = random.choice(father.blood_types)
        self.mother_allel = random.choice(mother.blood_types)
        self.blood_type = self.determine_blood_type()

    def determine_blood_type(self):
        allels = sorted([self.father_allel, self.mother_allel])

        if allels == ['A', 'B']:
            return 'AB'
        elif allels == ['A', 'O']:
            return 'A'
        elif allels == ['B', 'O']:
            return 'B'
        elif allels == ['A', 'A']:
            return 'A'
        elif allels == ['B', 'B']:
            return 'B'
        elif allels == ['O', 'O']:
            return 'O'
        else:
            return 'Unknown'

father_allels = tuple(input("Masukkan 2 alel golongan darah ayah (misal A O): ").split())
mother_allels = tuple(input("Masukkan 2 alel golongan darah ibu (misal B O): ").split())

father = Father(father_allels)
mother = Mother(mother_allels)

child = Child(father, mother)

print(f"Golongan darah anak: {child.blood_type}")
print(f"Alel anak: {child.father_allel} dari ayah, {child.mother_allel} dari ibu")