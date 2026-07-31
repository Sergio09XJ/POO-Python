from pay import Pay
import re 

class Card(Pay):
  def __init__(self, card_n):
    self.card_n = card_n 

  def make_pay(self, amount):
    pay_card = super().make_pay(amount)

    if len(str(self.card_n)) == 16:
      digitos = re.findall( r"\d{4,4}",self.card_n)
      num_c = digitos[-1] 
      pay_card["last_card_numbers"] = num_c
      return pay_card
      
    else: 
      raise Exception ("El número de tu tajeta es incorrecto.")  
   
   
