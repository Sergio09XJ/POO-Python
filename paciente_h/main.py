from Node import PatientNode

class PatientList:
  def __init__(self, max_beds):
    
    self.head = None
    self.tail = None
    self.max_beds = max_beds
    self.cont = 0
   

  def addPatient(self, name, age):
      if self.cont < self.max_beds: 
        self.cont = self.cont + 1 
        bed_number = self.cont
        new_node = PatientNode(name, age, bed_number) 
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node 
      else: 
        raise Exception ("No hay camas disponibles")        
        

  def removePatient(self, name):
    if self.cont == 0:
     raise Exception ("No hay pacientes que liberar")
    else: 
     current = self.head 
     for i in range(self.cont-1): 
       if current.name == name: 
        self.head = current.next 
        self.cont = self.cont - 1 
        return (f"Se elimino a {name}")
       elif current.next.name == name:
         deleted_N = current.next 
         current.next = deleted_N.next
         self.cont = self.cont - 1
         return (f"Se elimino a {name}")
       elif i == self.cont-2:
         raise Exception ("Paciente no encontrado")
       else:  
         current = current.next

          
  def getPatient(self, name):
    current = self.head 
    while current is  not None: 
       if current.name == name: 
          return  {"name":current.name ,"age":current.age , "bedNumber": current.bed_number}
       current = current.next 
    raise Exception ("Paciente no encontrado")   


  def getPatientList(self):
   lista_paciente = []
   current = self.head
   while current is not None:  
      lista_paciente.append({"name":current.name ,"age":current.age , "bedNumber": current.bed_number})
      current = current.next 
   return lista_paciente  

  def getAvailableBeds(self):
    return self.max_beds - self.cont




list = PatientList(10)
list.addPatient("Paciente 1", 20)
list.addPatient("Paciente 2", 30)
list.addPatient("Juanito Cabrera", 26)
list.addPatient("Ernesto de la Roma", 67)
list.addPatient("Atraides", 25)


print("\n Lista de Pacientes: ")
print(f"{list.getPatientList()}\n")

list.removePatient("Paciente 1")

print("\n Lista de Pacientes, pero con uno eliminado:")
print(f"{list.getPatientList()}\n")

print("\n Paciente en especifico: ")
print(f"{list.getPatient("Atraides")}\n")

print("\n Camas disponibles: ")
print(f"{list.getAvailableBeds()}\n")
