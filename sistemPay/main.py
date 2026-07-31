 
from paypal import PayPal
from card import Card 
from cash import Cash

def process_pay(payment_method, amount):
   return payment_method.make_pay(amount)

cash = Cash()

print(process_pay(cash, 400))