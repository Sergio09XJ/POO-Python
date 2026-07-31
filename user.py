class User:
  def __init__(self, name, age):
    self._name = name
    self._age = age
    self._friends = []
    self._messages = []

  @property
  def name(self): 
    return self._name 
  
  @name.setter
  def name(self, nuevo):
    self._name = nuevo
    return self._name

  @property
  def age(self): 
    return self._age  
  
  @age.setter
  def age(self, nuevo):
    self._age = nuevo
    return self._age


  def addFriend(self, friend): 
    self._friends.append(friend)
  
  def sendMessage(self, message, friend):
     self._messages.append(message)  
     friend._messages.append(message)
  
  def showMessages(self):
    return self._messages
  
usuario1 = User("Juan", 20)
usuario2 = User("Maria", 25)
usuario1.addFriend(usuario2)
usuario1.sendMessage("Hola Maria!", usuario2)
usuario2.sendMessage("Hola Juan!", usuario1)

usuario1.showMessages()