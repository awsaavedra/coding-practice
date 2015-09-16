class CreditCard: # Make sure classes start with upper case
  
  def __init__(self, customer, bank, acnt, limit):
    self._customer = customer
    self._bank = bank
    self._acnt = acnt
    self._limit = limit
    self._balance = 0

  def get_customer(self): #accessor method
    return self._customer

  def get_bank(self):
    return self._bank

  def get_limit(self):
    return self._limit

  def get_balance(self):
    return self._balance 

  def charge(self, price):
    # if charge would exceed limit,
    if price + self. balance > self. limit:
      return False
    # cannot accept charge
    else:
      self. balance += price
      return True
  
  def make_payment(self, amount):
    self._balance -= amount
    

cc = CreditCard( 'John Doe', '1st Bank' , '5391 0375 9387 5309' , 1000)

class PredatoryCreditCard(CreditCard):
  """An extension of the original CC class"""
  def __init__(self, customer, bank, acnt, limit, apr):
    super( ).__init__(customer, bank, acnt, limit) #calls super class credit card
    self._apr = apr

  def charge(self, price):
    #return true if charge was processed
    #otherwise, false
    success = super( ).charge(price)
    if not success:
      self._balance += 5
    return success

  def process_month(self):
    if self._balance > 0:
      monthly._factor = pow(1 + self._apr, 1/12)
      self._balance *= monthly_factor

