# --Тема: Наследование--

# --Родительский класс--
class Hero:
    def __init__(self, nick, hp, lvl,):
        self.nick = nick
        self.hp = hp
        self.lvl = lvl
    def action(self):
        return f"{self.nick} base action!!"
Kirito = Hero("Kirito", 100, 100)

# print(Kirito.action())

# --Дочерний класс--
class MageHero(Hero):
    def __init__(self, nick, hp, lvl, mp):
        super().__init__(nick, hp, lvl)
        self.mp = mp
    def action(self):
        print(f"i'm {self.nick}  this my base and my MP:{self.mp}")
Asuna = MageHero("Asuna", 100, 100, 9999)
# Asuna.action()

# вертикальное наследование
class Fly:
    def action(self):
        print("Fly")

class Swim:
    def action(self):
        print("Swim")

class Animal(Fly, Swim):
    pass
# Duck = Animal()
# Duck.action()


# Ромбавидное наследование и его проблемы
class A:
    def action(self):
        print("A")

class B(A):
    def action(self):
        super().action()
        print("B")

class C(A):
    def action(self):
        print("C")

class D(B , C):
    def action(self):
        super().action()
        print("D")
test_obj = D()
test_obj.action()