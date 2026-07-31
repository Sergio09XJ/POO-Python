class MyList:
  def __init__(self):
    self._data = {}
    self._length = 0

  @property
  def data(self): 
     return self._data
    
  @data.setter 
  def data(self, value):
    self._data = value  
    self._length = len(value)
    
     
  @property 
  def length(self): 
    return self._length 

  def append(self, item):
    self._data[len(self._data)] = item
    self._length += 1
    return self._data
   
  def pop(self):
    aux_dict = {}
    item_F = self._data[self.length-1]
    aux_dict = {clave: valor for clave, valor in self._data.items() if clave != self.length-1}
    self._data = aux_dict
    self._length -=1
    return item_F 

  def shift(self):
    item_P = self._data[0]
    aux_dict = {clave-1: valor for clave, valor in self._data.items() if clave !=0}
    self._data = aux_dict
    self._length -=1
    return item_P

  def unshift(self, item):
    list_aux = []
    list_1 = list(self._data.values())
    list_aux[0:] = [item]
    for i in range(len(list_1)): 
      list_aux[len(list_aux)+1:]  = [list_1[i]]
    self._data = {i: list_aux[i] for i in range(len(list_aux))} 
    self._length += 1
    return self._data  
      

  def map(self, func):
    dict_map = MyList() 
    dict_map._data = {key: func(value) for key, value in self._data.items()} 
    dict_map._length = self.length
    return  dict_map
  

  def filter(self, func):
    dict_filtra = MyList()
    valores = [value for value in self._data.values() if func(value)]
    dict_filtra._data = {i: value for i, value in enumerate(valores)}
    dict_filtra._length = len(valores)
    return dict_filtra
  
        
   

     
   
  def join(self, character = ","):
    stringG = ""
    for indice in range(self._length): 
      if indice == self._length-1: 
        stringG +=  str(self._data[indice])
      else:  
        stringG += (str(self._data[indice]) + character)
    return stringG    
        

myList = MyList()
myList.append("Hola")
myList.append("Como")
myList.append("Estas")
myList.append("Platzinauta")

print(" ")
print( myList.data)
print("\n ------------ \n")

myList = MyList()
myList.append("Platzinauta")
myList.unshift("Hola!")

print(myList.data)
print("\n ------------ \n")

myList = MyList()
myList.append("Hola")
myList.append("Como")
myList.append("Estas")
myList.append("Platzinauta")

print(myList.data)
print(myList.shift())
print(myList.data)
print("\n ------------ \n")

myList = MyList()

myList.append("Hola")
myList.append("Como")
myList.append("Estas")
myList.append("Platzinauta")

print(myList.data)
print(myList.map(lambda x:x.upper()))
print("\n ------------ \n")

myList = MyList()

myList.append(1)
myList.append(2)
myList.append(3)
myList.append(5)
myList.append(6)


print(myList.data)
print(myList.filter(lambda x: x % 2 == 0))
print("\n ------------ \n")
