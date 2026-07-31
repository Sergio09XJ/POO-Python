#Crear concesionaria 
#Compra y venta de vehiculo. 
#Usuario puede preguntar por su precio, disponibles y comprar uno.

class auto: #Creamos la clase Auto, definimos sus caracteristicas y metodos. 
   def __init__(self, precio, modelo, año): 
      self.precio = precio #Precio del Auto. 
      self.modelo = modelo  #Modelos de este. 
      self.año = año  #Año de este 
      self.disponible = True  #Si se encuentra disponible, por defecto si. 

   def comprar(self): #Metodo comprar 
      if  self.disponible == True: #Si el auto esta disponible. 
         self.disponible = False  #Lo cambiamos a false, ya no lo esta. 
         return print(f"Felicidades haz comprado el  {self.modelo} del año {self.año}") #Retornamos el print
      else: 
         print("Lo Lamento pero el auto que buscas no esta disponible por ahora. ") #Retornamos el print en caso de que el auto no este disponible. 

   def vender(self):  #Metodo para vender. 
      self.disponible = True  #Pasamos disponible a true 
      print(f"EL auto {self.modelo} a sido comprado por la concesionaria. ") #Lanzamos el mensaje de que fue comprado. 

class usuario: #Creamos la clase usuario con sus caracteristicas y métodos. 
   def __init__(self, nombre, monto): 
      self.nombre = nombre  #Nombre de la persona. 
      self.monto = monto #El dínero con el que cuenta. 
      self.auto_adqui  = []  #Lista donde se guardaran los autos con los que cuenta  o a comprado el usuario

   def comprar_auto(self, auto,concesionario): #Metodo comprar auto. 
      #Como entrada pedimos el auto y el concesionario ya que el auto lo eliminaremos de la lista de este si es que lo tienen. 
      if  self.monto >= auto.precio and auto.disponible: #Si el usuario tiene el dínero y esta disponible
          auto.comprar() #Llama a la función comprar de la clase auto. 
          self.auto_adqui.append(auto) #Guardamos el auto en la lista del usuario. 
          if auto in concesionario.carros: 
            concesionario.carros.remove(auto) #La eliminamos de la lista del concecionario si es que eta 
          self.monto -= auto.precio #Restamos el precio del auto al monto con el que cuenta el usuario. 
          print(f"La compra fue por un monto de ${auto.precio} y te restan ${self.monto}")
          #Mandamos a imprimir un mensaje con el valor despues de la compra. 
      else: 
         print("Lo Lamento pero el auto que buscas no esta disponible por ahora. ")#En caso de que el auto no este disponible lanza este mensaje. 

   def vender_auto(self, auto, concesionario): #Esta función nos sirve para vender el auto. 
       if  auto in self.auto_adqui: #Si el auto esta en la lista de autos de usuario(Lo tenemos. 
         if concesionario.capital >= auto.precio:  # y si el concesionario tiene el capital para comprarlo 
           concesionario.capital -= auto.precio #Restamos el valor del auto al capita. 
           self.monto += auto.precio #Sumamos ese valor al monto del usuario. 
           self.auto_adqui.remove(auto) #Removemos el auto de la lista de autos del usuario. 
           concesionario.carros.append(auto) #Ponemos el auto en la lista del concesionario. 
           auto.vender() #Llamamos a auto. vender
         else: 
          print("fLo sentimos pero la Concesionaria no tiene capital para comprar el auto.") 
          #Si la concesionaria no cuenta con el dínero mandamos este mensaje. 
       else:
          print("No cuentas con este carro para poder venderlo.")    
          #Si no tenemos el auto, mandamos este. 

   def add_auto_u(self,auto):#Función para agregar el auto a la lista del usuario. 
        self.auto_adqui.append(auto)  #Agregamos el auto con append. 
        print(f"El  {auto.modelo} fue agregado con exito. ")  #y mandamos este mensaje. 

   def autos_disponibles_u(self): #Función para conocer los autos con los que contamos. 
      print("\n Cuentas con los siguientes carros:  ")
      cont = 1 #Usamos a cont como indice númerico. 
      for auto in self.auto_adqui: #Ciclo para iterar por estos. 
            print(f"{cont}. {auto.modelo} año {auto.año}") 
            cont += 1  #Despues de imprimir cada valor sumamos uno. 

      
class concesionario: #Clase concesionario con métodos y valores. 
   def __init__(self): 
      self.carros = [] #Lista donde guardaremos los carros.
      self.usuarios = [] #Lista donde guardaremos a los usuarios. 
      self.capital = 1000000 #Iniciamos el capital con 1,000,000

   def add_carro(self, carro): #Con esta función agregamos los carros a la lista. 
      self.carros.append(carro) #Usamos append
      print(f"El  {carro.modelo} fue agregado con exito. ") #Lanzamos el mensaje de confirmación. 

   def add_usuario(self, usuario):#Con esta función agregamos los usuarios a la lista. 
      self.usuarios.append(usuario) #Usamos append
      print(f"El usuario {usuario.nombre} fue agregado con exito al concecionario. ")#Lanzamos el mensaje de confirmación. 

   def usuarios_disponibles(self): #Mostramos los usuarios con los que contamos. 
      print(" ")
      for usuario in self.usuarios: 
          print(f"{usuario.nombre} esta en nuestra base de datos.(:")#Lanzamos el mensaje de confirmación 

   def autos_disponibles(self): #Mostramos los Carros con los que contamos. 
      print(" ")
      for carro in self.carros: 
            print(f"El {carro.modelo}, año {carro.año} tiene un costo de ${carro.precio}  esta disponible.")  #Lanzamos el mensaje de confirmación        

   def costos(self,auto):#Esta función la usamos para los costos de cada carro. 
      for carro in self.carros: #Por cada carro en lista de carros. 
         if carro.modelo == auto and carro.disponible == True:  #Si el carro esta disponible. 
            print(f"El costo del {auto} es de ${carro.precio}. ") #Mostramos el precio 
         elif carro.modelo == auto and carro.disponible == False: #SI el carro no esta disponible
            print(f"Lo sentimos el {auto} no se encuentra disponible.  ")   #Lanzamos el mensaje para informar que no esta disponible.  
        
# 5 objetos de Carros 
Carro_1 = auto(25000, "Mustang", 1969)
Carro_2 = auto(51900, "Model 3", 2024)
Carro_3 = auto(34500, "Prius", 2024)
Carro_4 = auto(2500000, "La Ferrari", 2013)
Carro_5 = auto(44600, "Volvo XC30", 2025)
 
# 1 Objeto de usuario 
usuario_1 = usuario("Sergio",1000000)

#Creamos un objeto para concesionario
Adv = concesionario()
Adv.add_carro(Carro_1) #Agregamos el carro 1
Adv.add_carro(Carro_2) # y el 2
Adv.add_usuario(usuario_1) #Agregamos el usuario 1
Adv.usuarios_disponibles() #Mostramos los usuarios disponibles. 
Adv.autos_disponibles() #Mostramos los autos disponibles. 

#Compramos el carro 1
usuario_1.comprar_auto(Carro_1, Adv)
Adv.autos_disponibles() #Mostramos ahora los autos con los que cuenta la concesionaria Adv. 
         
Adv.costos("Model 3") #Imprimimos los costos del Model 3

usuario_1.add_auto_u(Carro_5) #Agregamos el carro 5 a la lista del usuario. 
usuario_1.autos_disponibles_u()#Ahora mostramos los carros con los que cuenta Sergio 

usuario_1.vender_auto(Carro_5,Adv) #Vendemos el carro 5 a la concesionario Adv. 

usuario_1.autos_disponibles_u() #Ahora mostramos los carros con los que cuenta el usuario. 
Adv.autos_disponibles()# y la concecionaria 

usuario_1.comprar_auto(Carro_1, Adv)#Compramos el carro 1 a la concecionaria(NO podemos, lo tenemos nosotros.)
usuario_1.vender_auto(Carro_5,Adv)#Vendemos el carro 5(No podemos, ya lo hicimos antes).