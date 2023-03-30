class CuentaBancaria:

    todascuentas = []

    def __init__(self, tasa_interes, balance): 
        self.tasa_interes = tasa_interes
        self.balance = balance
        CuentaBancaria.todascuentas.append(self)

    def deposito(self, amount):
        self.balance +=amount
        return self

    def retiro(self, amount):
        self.balance -= amount
        return self

    def mostrar_info_cuenta(self):
        print("balance: $%d"%(self.balance))

    def generar_interés(self):
        self.balance = self.balance*(1 +self.tasa_interes/100)
        return self       

    @classmethod
    def imprimir_cuentas(cls):
        for cuenta in cls.todascuentas:
            cuenta.mostrar_info_cuenta()

cuenta1 = CuentaBancaria(3,1000)
cuenta2 = CuentaBancaria(5,2000)

cuenta1.deposito(200).deposito(200).deposito(200).retiro(100).generar_interés()
cuenta1.mostrar_info_cuenta()

# cuenta2.deposito(300).deposito(300).retiro(200).retiro(200).retiro(500).retiro(500).generar_interés()
# cuenta2.mostrar_info_cuenta()
    
# print("imprimir_cuentas")
# CuentaBancaria.imprimir_cuentas()
     





   

    

        
