class Hero:
        # конструктор класса
        def __init__(self, nick, hp, lvl):
            # атрибуты класса(без скобок)
            self.nick = nick
            self.hp = hp
            self.lvl = lvl
        # действия(со скобками)
        def action(self):
            return f"{self.nick} base action activate!!"
    # объект

Kirito = Hero("Kirito", 1000, 1000)
Asuna = Hero("Asuna", 1000, 1000)

print(Kirito.action())
print(Asuna.action())

# my_int = 123
# my_int.
# my_str = "123"
# my_str.

