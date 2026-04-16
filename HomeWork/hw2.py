import random

class Hero:
    def __init__(self, name, level, health, strength):
        self.name = name
        self.level = level
        self.health = health
        self.strength = strength

    def greet(self):
        print(f"Привет! Я {self.name}, уровень {self.level}")

    def attack(self):
        print(f"{self.name} атакует!")

    def rest(self):
        self.health += 10
        print(f"{self.name} отдыхает и восстанавливает здоровье. Текущее здоровье: {self.health}")


class Warrior(Hero):
    def __init__(self, name, level, health, strength, stamina):
        super().__init__(name, level, health, strength)
        self.stamina = stamina

    def attack(self):
        print(f"{self.name}: Воин атакует мечом!")


class Mage(Hero):
    def __init__(self, name, level, health, strength, mana):
        super().__init__(name, level, health, strength)
        self.mana = mana

    def attack(self):
        print(f"{self.name}: Маг кастует заклинание!")


class Assassin(Hero):
    def __init__(self, name, level, health, strength, stealth):
        super().__init__(name, level, health, strength)
        self.stealth = stealth

    def attack(self):
        print(f"{self.name}: Ассасин атакует из-под тишка!")


warrior = Warrior("Тор", 5, 100, 20, 50)
mage = Mage("Мерлин", 5, 80, 25, 100)
assassin = Assassin("Шэдоу", 5, 70, 30, 90)

heroes = {
    "warrior": warrior,
    "mage": mage,
    "assassin": assassin
}

print("Выберите героя: Warrior / Mage / Assassin")
choice = input("Ваш выбор: ").lower()

if choice not in heroes:
    print("Неверный выбор!")
else:
    player = heroes[choice]
    enemy = random.choice(list(heroes.values()))

    print(f"\nВы выбрали: {player.__class__.__name__}")
    print(f"Противник: {enemy.__class__.__name__}\n")

    player.attack()
    enemy.attack()

    if type(player) == type(enemy):
        print("Ничья!")
    elif (
        (isinstance(player, Warrior) and isinstance(enemy, Assassin)) or
        (isinstance(player, Assassin) and isinstance(enemy, Mage)) or
        (isinstance(player, Mage) and isinstance(enemy, Warrior))
    ):
        print(f"{player.__class__.__name__} победил!")
    else:
        print(f"{enemy.__class__.__name__} победил!")