class BankAcount:
    def __init__(self, login, password, balance):
        self.login = login
        self.password = password
        self._balance = balance

    def get_balance(self, password):
        if password == self.password:
            return self._balance
        else:
            return "неправ пароль"

Mura = BankAcount("Mura", 1212, 9090)
print(Mura.get_balance(1212))
print(Mura.login)
print(Mura._balance)