class Hero:
    def __init__(self, name, level, health, strength):
        self.name = name
        self.level = level
        self.health = health
        self.strength = strength

    def greet(self):
        return f"Привет, я {self.name}, мой уровень {self.level}"

    def attack(self):
        self.strength -= 1
        return f"{self.name} наносит удар!"

    def rest(self):
       self.health += 1
       return f"{self.name} отдыхает"

Artas = Hero("Artas", 10, 3000, 90)
lllidan = Hero("llidan", 10, 2600, 50)

print(Artas.greet())
print(Artas.attack())
print(Artas.rest())
print(f"После: здоровье = {Artas.health}, сила = {Artas.strength}")
print("----------------------------------")
print(lllidan.greet())
print(lllidan.attack())
print(lllidan.rest())
print(f"После: здоровье = {lllidan.health}, сила = {lllidan.strength}")
