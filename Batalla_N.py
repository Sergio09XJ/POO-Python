
class Jugadores: 
   def __init__(self, nombre):
       self.nombre = nombre 
       self.Naval = ["Portaaviones", "Acorazado", "Submarino", "Crucero", "Destructor", "P", "A", "S", "C", "D"]
 
class Tablero: 
    def __init__(self): 
        self. posicion = None 
        self.comparador = None
        self.vencido = []
        self.matriz = [[" ","1","2","3","4","5","6","7","8","9","10"],
                       ["A","*","*","*","*","*","*","*","*","*","*"],
                       ["B","*","*","*","*","*","*","*","*","*","*"],
                       ["C","*","*","*","*","*","*","*","*","*","*"],
                       ["D","*","*","*","*","*","*","*","*","*","*"],
                       ["E","*","*","*","*","*","*","*","*","*","*"],
                       ["F","*","*","*","*","*","*","*","*","*","*"],
                       ["G","*","*","*","*","*","*","*","*","*","*"],
                       ["H","*","*","*","*","*","*","*","*","*","*"],
                       ["I","*","*","*","*","*","*","*","*","*","*"],
                       ["J","*","*","*","*","*","*","*","*","*","*"]]
    def Mostrar_m(self,Jugadores): 
        print(f"\n------ Tablero de {Jugadores.nombre} ------------------------------ ")
        for i in range(len(self.matriz)): 
         print(self.matriz[i])

    def Posicionamiento(self, Jugador):
       Simbolo = 5
       long = 4
       letras = ["A","B","C","D","E","F","G","H","I","J"]
       comp = False
       cont = 0
       for i in range(5):
         while not comp:
          
          if cont == 0:
             print(f"\nUsando las letras y números de tu tablero, dime en que coordenada quíeres poner tu {Jugador.Naval[i]}")
          elif cont == 1:
             print(f"\nLas coordenadas que usaste para tu {Jugador.Naval[i]} ya estan siendo ocupadas por otro barco, dame unas nuevas. ") 
          else:
             print(f"\nLas coordenadas que usaste para tu {Jugador.Naval[i]} salen del tablero, por favor dame unas nuevas. ")   
          self.posicion = input("Comenzando con la letra(Mayuscula) seguido del Número:  ")
          particion = list(self.posicion)

          if len(particion)  == 3: 
              particion[1] = particion[1] + particion[2]
              particion.pop(2)
          particion[1] = int(particion[1])
          particion[0] = particion[0].upper()

          for k in range(len(letras)): 
             if particion[0] == letras[k]:
                particion[0] = k+1
                break 

          direccion = input("Vertical u Horizontal(V/H): ") 
          direccion =direccion.upper()

          if (direccion == "V" and particion[0] - long < 1) or (direccion == "H" and particion[1] - long < 1):
             cont = 2  
             print("Entro al if de los limites") 
          elif self.matriz[particion[0]][particion[1]] != "*":
             cont = 1
             print("Entro al if del asterisco * ")
          else:  
             for j in range(long):
               if direccion == "V": 
                if self.matriz[particion[0]-(j)][particion[1]] != "*":
                   print("imporstor!!!!")
                   cont = 1 
                   comp = False
                   break 
                elif self.matriz[particion[0]-(j)][particion[1]] == "*":
                   comp = True 
                   particion[0]-(j+1)
               elif direccion == "H":
                  if self.matriz[particion[0]][particion[1]-(j+1)] != "*": 
                    print("imporstor!!!!")
                    cont = 1
                    comp = False
                    break
                  elif self.matriz[particion[0]][particion[1]-(j+1)] == "*": 
                    comp = True
                    particion[1]-(j+1) 
                           
             
         for j in range(long):
          self.matriz[particion[0]][particion[1]] = Jugador.Naval[Simbolo]
          if direccion == "V":
            self.matriz[particion[0]-(j+1)][particion[1]] = Jugador.Naval[Simbolo]
            self.matriz[particion[0]-(j+1)]     
          elif direccion == "H":
            self.matriz[particion[0]][particion[1]-(j+1)] = Jugador.Naval[Simbolo]
            self.matriz[particion[1]-(j+1)]
          
         if Jugador.Naval[i] != "Submarino":
            long -= 1
         Simbolo += 1  
         cont = 0
         comp = False
         print(self.Mostrar_m(Jugador))
         
       
         
                     
    def Combate(self): 
       print("\nDame los valores para atacar a tu oponente: ")
       letras = ["A","B","C","D","E","F","G","H","I","J"]

       self.comparador = input("Comenzando con la letra(Mayuscula) seguido del Número:  ")
       particion_c = list(self.comparador)
       if len(particion_c)  == 3: 
          particion_c[1] = particion_c[1] + particion_c[2]
          particion_c.pop(2)
       particion_c[0] = particion_c[0].upper()
       particion_c[1] = int(particion_c[1])
       
       for i in range(len(letras)): 
          if particion_c[0] == letras[i]:
             particion_c[0] = i+1
             break

       if self.matriz[particion_c[0]][particion_c[1]] == "P":  
          self.matriz[particion_c[0]][particion_c[1]] = "Tp"
          self.vencido.append("P")
          print("!Tocado!")
       elif self.matriz[particion_c[0]][particion_c[1]] == "A":  
          self.matriz[particion_c[0]][particion_c[1]] = "Ta"
          self.vencido.append("A")
          print("!Tocado!")
       elif self.matriz[particion_c[0]][particion_c[1]] == "S":  
          self.matriz[particion_c[0]][particion_c[1]] = "Ts"
          self.vencido.append("S")
          print("!Tocado!")
       elif self.matriz[particion_c[0]][particion_c[1]] == "C":  
          self.matriz[particion_c[0]][particion_c[1]] = "Tc"
          self.vencido.append("C")
          print("!Tocado!")
       elif self.matriz[particion_c[0]][particion_c[1]] == "D":  
          self.matriz[particion_c[0]][particion_c[1]] = "Td"
          self.vencido.append("D")
          print("!Tocado!")
       else: 
          print("¡Agua!") 
       particion_c = [None, None]
       self.comparador = None
       

          
          

if __name__ == "__main__": 
 pass


