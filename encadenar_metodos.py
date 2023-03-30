class usuario:
    def __init__(self , name):
        self.name = name
        self.balance_cuenta = 0

    def hacer_deposito(self, amount):
        self.balance_cuenta += amount
        return self

    def hacer_descontar(self , other_user):
        self.balance_cuenta -= other_user
        return self

yiyi = usuario("yiyi")
kako = usuario("kako")
nani = usuario("nani")


yiyi.hacer_deposito(2000).hacer_deposito(2000).hacer_deposito(200).hacer_descontar(200).balance_cuenta()
kako.hacer_deposito(1000).hacer_deposito(3000).hacer_descontar(300).hacer_descontar(100).balance_cuenta()
nani.hacer_deposito(5000)nani.hacer_descontar(600).hacer_descontar(300).hacer_descontar(500).balance_cuenta()


print(f"user: {yiyi.name},balance: {yiyi.balance_cuenta}")
print(f"user: {kako.name},balance: {kako.balance_cuenta}")
print(f"user: {nani.name},balance: {nani.balance_cuenta}")