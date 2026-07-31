class bank_account:
    def __init__(self, propietario, cantidad): 
        self.propietario = propietario
        self.cantidad = cantidad
        self.estatus = True 

    def  Ingresar_D(self, monto): 
        if self.estatus == True:
           self.cantidad += monto
           print(f"La cantidad de {monto}, fueron ingresados a tu cuenta, tienes {self.cantidad}")
        else: 
            print("No se puede hacer la transacción. Cuenta desactivada.")

    def Retirar_D(self,monto): 
        if self.estatus == True and monto <= self.cantidad: 
          self.cantidad -= monto
          print("El Dínero fue exitosamente retirado. ")  
        elif monto > self.cantidad :
            print("El monto que deseas retirar supera tus fondos. ")
        elif self.estatus == False: 
             print("No se puede hacer la transacción. Cuenta desactivada.")  


    def deactivate(self): 
        self.estatus = False if self.estatus == True else print("Tu cuenta ya a sido desactivada. ")

    def activate(self): 
        self.estatus = True if self.estatus == False else print("Tu cuenta ya esta activa. ")

Account_1 = bank_account("Julian", 10000)
Account_2 = bank_account("Antonieta", 30000)

Account_1.Ingresar_D(7000)
Account_2.activate()
Account_2.deactivate()
Account_2.Retirar_D(40000)
Account_2.activate()
Account_2.Retirar_D(40000)
Account_1.Retirar_D(500)
