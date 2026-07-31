from pay import Pay

class Cash(Pay):

    def make_pay(self,amount):
     cash_dict = super().make_pay(amount)
     return cash_dict