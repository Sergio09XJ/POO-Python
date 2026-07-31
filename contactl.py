class ContactList:
  
  def __init__(self, size):
    self.size = size 
    self.contact_l = [[] for _ in range(size)]

  def hash(self, key):
    return hash(key) % self.size

  def insert(self, name, phone):
    indice = self.hash(name) 
    self.contact_l[indice].append([name, phone])

  def get(self, name):
    indice = self.hash(name) 
    for nam, phone in self.contact_l[indice]:
      if nam == name:
        return phone
    return None

  def retrieveAll(self):
    lista = [] 
    for bucket in self.contact_l:
      for name, phone in bucket: 
       lista.append([name,phone])
    return lista   
    

  def delete(self, name):
    indice = self.hash(name) 
    for i, (nam, phone) in enumerate(self.contact_l[indice]):
       if nam == name:
         del self.contact_l[indice][i]
         break
     
contactList = ContactList(10)
contactList.insert("Mr michi", "123-456-7890")
contactList.insert("Mario", "55-3433-6947")
contactList.insert("Alberto", "56-2735-2573")

print(contactList.retrieveAll())

