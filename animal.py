class Animal:
  def __init__(self, name, age, specie):

    self.name = name
    self.age = age 
    self.specie = specie
  
  def getInfo(self):
    dict_info =  {"name":self.name, "age":self.age, "specie":self.specie}
    return dict_info
  
class Mammal(Animal):
  def __init__(self, name, age, specie, hasFur):
    super().__init__(name, age, specie)
    self.hasFur = hasFur

  def getInfo(self): 
     origin_dict = super().getInfo()
     origin_dict["hasFur"] = self.hasFur
     return origin_dict
     
class Dog(Mammal):
  def __init__(self, name, age, breed):
    super().__init__(name, age, specie = "dog", hasFur = True)
    self.breed = breed 
    self.hasFur = True 

  def bark(self): 
    return "woof!"
  
  def getInfo(self): 
     mammal_dict = super().getInfo()
     mammal_dict["breed"] = self.breed
     return mammal_dict
  

  
print("\n ------------------------- Clase Padre = Animal \n")
bird = Animal("pepe", 1, "bird")
print(bird.getInfo())
print("\n ------------------------- Clase Hija = Mammal \n")
hippo = Mammal("bartolo", 3, "hippo", False)
print(hippo.getInfo())
print("\n ------------------------- Clase Nieta = Dog \n")
dog = Dog("fido", 4, "pastor aleman");
print(dog.bark())
