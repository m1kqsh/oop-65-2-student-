class Hero:
    def __init__(self, hp, nick, lvl):
        self.hp = hp
        self.nick = nick
        self.lvl = lvl
    def action(self):
        return f"{self.nick} action base!!"
