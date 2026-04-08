# class Hero:
#         # --конструктор класса--
#         def __init__(self, nick, hp, lvl):

#             # --атрибуты класса(без скобок)--
#             self.nick = nick
#             self.hp = hp
#             self.lvl = lvl
#         # функции действия(со скобками)
#         def action(self):
#             return f"{self.nick} base action activate!!"
#     # --объект--
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
