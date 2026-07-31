from Batalla_N import Jugadores
from Batalla_N import Tablero 

print("\n -------------------------------- Batalla Naval -------------------------------- ")

nombre_1 = input("\nDame el nombre del primer jugador: ")
nombre_2 = input("\nDame el nombre del segundo jugador: ")

Usuario_1 = Jugadores(nombre_1)
Usuario_2 = Jugadores(nombre_2)

Tablero_1 =Tablero()
Tablero_1.Mostrar_m(Usuario_1)
Tablero_1.Posicionamiento(Usuario_1)

print(f"\nAhora por favor ingresa tus valores {Usuario_2.nombre}")

Tablero_2 =Tablero()
Tablero_2.Mostrar_m(Usuario_2)
Tablero_2.Posicionamiento(Usuario_2)

print(f"\nEs momento de atacar, tu deber es elegir las coordenadas en donde crees que esten los barcos de tu oponente. \n")

while len(Tablero_1.vencido) <= 17 and len(Tablero_2.vencido) <= 17: 
   
    if len(Tablero_2.vencido) < 17 and len(Tablero_1.vencido) < 17:
         print(f"Turno de {Usuario_1.nombre}: ")
         Tablero_1.Mostrar_m(Usuario_1)
         Tablero_2.Combate()     
    elif len(Tablero_2.vencido) == 17 and len(Tablero_1.vencido) < 17: 
         print(f"\n¡¡¡Undiste todos los barcos {Usuario_1.nombre} Ganaste!!!\n")
         break
    
    if len(Tablero_1.vencido) < 17 and len(Tablero_2.vencido) < 17:
         print(f"Turno de {Usuario_2.nombre}: ")
         Tablero_2.Mostrar_m(Usuario_2)
         Tablero_1.Combate() 
    elif len(Tablero_1.vencido) == 17 and len(Tablero_2.vencido) < 17:
         print(f"\n¡¡¡Undiste todos los barcos {Usuario_2.nombre}!! Ganaste!!!\n")
         break
        
