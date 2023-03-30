class CuentaBancaria:
    cuentas = []
    def __init__(self, tasa_interes, balance): 
        self.tasa_interes = tasa_interes
        self.balance= balance
        CuentaBancaria.cuentas.append(self)

    def deposito(self, amount):
        self.balance += amount
        return self

    def retiro(self, amount):
        if self.balance > amount:
            self.balance -= amount
        else:
            print("No se puede, saldo insuficiente")

    def mostrar_info_cuenta(self):
        return 'balance: $%d'%(self.balance)

    def generar_interes(self):
        if self.balance > 0:
            self.balance += (self.balance * self.tasa_interes)
        return self
    @classmethod
    def imprimir_todas_cuentas(cls):
        for cuenta in cls.cuentas:
            cuenta.mostrar_info_cuenta()

class Usuario:

    def  __init__ ( self , name, email):
        self.name = name
        self.email = email
        self.cuenta  = {
            "checking" : CuentaBancaria(tasa_interes = 0.02 , balance = 0 ),
            "savings" : CuentaBancaria(tasa_interes = 0.06 , balance = 0 )
        }
    
    def hacer_deposito(self, amount , cuenta_key):
        self.cuenta[cuenta_key].deposito(amount)
        return self
    
    def hacer_retiro(self,amount,cuenta_key):
        self.cuenta[cuenta_key].retiro(amount)
        return self
    
    def mostrar_balance_usuario(self):
        print(f"Usuario: {self.name}, Checking Balance: {self.cuenta['checking'].mostrar_info_cuenta()}")
        print(f"Usuario: {self.name}, Savings Balance: {self.cuenta['savings'].mostrar_info_cuenta()}")
        return self
    

yiyi = Usuario("yiyi","yiyi@gmail.com")
yiyi.hacer_deposito(2000,'savings')
yiyi.hacer_retiro(-100,'checking')
yiyi.mostrar_balance_usuario()
