from mail import Mail

class Queue:
  def __init__(self):
   self.first = None
   self.last = None
   self.length = 0
  
  def enqueue(self, from_email, to, body, subject):
    nuevo_nodo = Mail(from_email, to, body, subject)
    correo_e = None
    if self.length == 0: 
      self.first = nuevo_nodo
      self.last = nuevo_nodo
    else: 
      self.last.next = nuevo_nodo
      self.last = nuevo_nodo
    self.length += 1
      

  def dequeue(self):
    if self.length == 0:
      raise Exception("No hay ningun correo que eliminar")
    eliminado = self.first
    if self.first == self.last: 
      self.last = None 
      self.first = None   
    else: 
      self.first = self.first.next 
    self.length -= 1 
    print("\n El correo fue eliminado con exito.\n")
    return eliminado
  
  def peek(self):
     if self.length == 0: 
       raise Exception ("NO tienes correos para mostrar")
     else: 
      print("\n El correo que buscas es: ")
      return self.first

  def is_empty(self):
    return  self.length  == 0
      
  
     
  def size(self):
   print("\n La longitud de tu cadena es de: ")
   return self.length


emailQueue = Queue()

emailQueue.enqueue(
    'jane@ejemplo.com',
    'support@ejemplo.com',
    'No puedo iniciar sesión en mi cuenta',
    'Problema de inicio de sesión'
)

emailQueue.enqueue(
    'joe@ejemplo.com',
    'support@ejemplo.com',
    'Mi pedido no ha llegado todavía',
    'Estado del pedido'
)

email = emailQueue.dequeue()
print(email)

print(emailQueue.is_empty())
print(emailQueue.size())