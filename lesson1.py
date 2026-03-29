# class Hero:
#         # конструктор класса
#         def __init__(self, nick, hp, lvl):
#             # атрибуты класса(без скобок)
#             self.nick = nick
#             self.hp = hp
#             self.lvl = lvl
#         # действия(со скобками)
#         def action(self):
#             return f"{self.nick} base action activate!!"
#     # объект
#
# Kirito = Hero("Kirito", 1000, 1000)
# Asuna = Hero("Asuna", 1000, 1000)
#
# print(Kirito.action())
# print(Asuna.action())

# my_int = 123
# my_int.
# my_str = "123"
# my_str.

# ДЗ
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

# тут уже можно приписать своего перса и его статы
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
        return f"{self.name} отдыхает…"

print("----------------------------------")

name1 = input("Имя героя 1: ")
level1 = int(input("Уровень: "))
health1 = int(input("Здоровье: "))
strength1 = int(input("Сила: "))

name2 = input("Имя героя 2: ")
level2 = int(input("Уровень: "))
health2 = int(input("Здоровье: "))
strength2 = int(input("Сила: "))

hero1 = Hero(name1, level1, health1, strength1)
hero2 = Hero(name2, level2, health2, strength2)

print(hero1.greet())
print(hero1.attack())
print(hero1.rest())
print(f"После: здоровье = {hero1.health}, сила = {hero1.strength}")

print("-----")

print(hero2.greet())
print(hero2.attack())
print(hero2.rest())
print(f"После: здоровье = {hero2.health}, сила = {hero2.strength}")