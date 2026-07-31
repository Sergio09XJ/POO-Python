from pay import Pay

class PayPal(Pay):
  def __init__(self,email):
   self.email = email 
   
  def make_pay(self,amount):
    pay = super().make_pay(amount)
    pay["platform"] = "PayPal"
    pay["email"] = self.email
    return pay

