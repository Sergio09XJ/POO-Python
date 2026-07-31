from product import Product

class Article(Product):

   def __init__(self, name, price, quantity):
       super().__init__(name, price, quantity)
       self.name = name
       self.price = price
       self.quantity = quantity

   def addToCart(self):
     print(f"Agregando {self.quantity} unidades del artículo {self.name} al carrito")
   def __repr__(self):
     return f"Article(name={self.name}, price={self.price}, quantity={self.quantity})"
  
class Service(Product):

   def __init__(self, name, price, quantity):
       super().__init__(name, price, quantity)
       self.name = name
       self.price = price
       self.quantity = quantity

   def addToCart(self):
     print(f"Agregando el servicio {self.name} al carrito")
   def __repr__(self):
     return f"Article(name={self.name}, price={self.price}, quantity={self.quantity})"

class Cart:
  def __init__(self):
   self.productos =  []    
  
  def addProduct(self, product):
      self.productos.append(product)
      product.addToCart()
      
      return self.productos
  
  def deleteProduct(self, product):
      self.productos.remove(product)
      return self.productos
  
  def calculateTotal(self):
     total = 0
     for producto in self.productos: 
         total += (producto.price * producto.quantity)
     print(total) 
     print(" ")   
         

  def getProducts(self):
    for producto in self.productos:
       print(f"Producto : {producto}")
    print(" ")   
        

book = Article("Libro", 100, 2);
Pants = Article("Pantalon", 500,3);
course = Service("Curso", 120, 1);


cart = Cart();
cart.addProduct(book);
cart.addProduct(course);
cart.addProduct(Pants);
cart.deleteProduct(book);
cart.calculateTotal();
cart.getProducts();

  