print("*****************************Question 1************************************************")
class Flower:
    def __init__(self,name,num_petals,price):
        #Initialize
        self.name = name
        self.num_petals = num_petals
        self.price = price

    # Setters
    def get_name(self, name):
        return self.name == name

    def get_num_petals(self, num_petals):
        return self.num_petals == num_petals

    def get_price(self, price):
        return self.price == price
        #Getters
    def get_name(self):
        return self.name
    def get_num_petals(self):
        return  self.num_petals
    def get_price(self):
        return self.price

    def hello(self):
       print("Hello " + self.name + "\nThe price is: R"+str(self.price) + "\nPetals "+str(self.num_petals))
flower1 = Flower("Onke",2,20.7)
flower1.hello()


print("*****************************Question 2************************************************")
class Goat(object):
    def __init__(self, variable_tail):
        self.variable_tail = variable_tail

    def milk(self):
        print("Milk")

    def jump(self):
        print("Jump")

goat = Goat("tail")
print(goat.milk())
print(goat.jump())



print("*****************************Question 3************************************************")
class CreditCard:
    def __init__(self, customer, bank, acnt, limit):
        self.customer = customer
        self.bank = bank
        self.acnt = acnt
        self.limit = limit

class PredatoryCreditCard(CreditCard):

     #”””An extension to CreditCard that compounds interest and fees.”””
      def init (self, customer, bank, acnt, limit, apr):
          # ”””Create a new predatory credit card instance.

          # The initial balance is zero.

          # customer the name of the customer (e.g., John Bowman )

          # bank the name of the bank (e.g., California Savings )

          # acnt the acount identifier (e.g., 5391 0375 9387 5309 )

          # limit credit limit (measured in dollars)

          # apr annual percentage rate (e.g., 0.0825 for 8.25% APR)
          super().init(customer, bank, acnt, limit)  # call super constructor
          self.apr = apr
      def charge(self, price):
# ”””Charge given price to the card, assuming sufficient credit limit.
# Return True if charge was processed.
# Return False and assess 5 fee if charge is denied.”””
         success = super( ).charge(price) # call inherited method
# if not success:
         self. balance += 5 # assess penalty
         return success # caller expects return value
      def process_month(self):
# ”””Assess monthly interest on outstanding balance.”””
          if self. balance > 0:
             monthly_factor = pow(1 + self. apr, 1/12)
             self. balance = monthly_factor

print("*****************************Question 4************************************************")


class Progression:

# 2 ”””Iterator producing a generic progression.


# 4 Default iterator produces the whole numbers 0, 1, 2, ... 5 ”””
      def init (self, start=0):

# 8 ”””Initialize current to the first value of the progression.”””
        self. current = start
      def advance(self):

# 12 ”””Update self. current to a new value.

# This should be overridden by a subclass to customize progression.
# By convention, if current is set to None, this designates the
# end of a finite progression.
       self. current += 1
      def next (self):

# 22 ”””Return the next element, or else raise StopIteration error.”””
       if self. current is None: # our convention to end a progression
        raise StopIteration( )
       else:
        answer = self. current # record current value to return
        self. advance( ) # advance to prepare for next time
       return answer # return the answer
      def iter (self):

# ”””By convention, an iterator must return itself as an iterator.”””
       return self
      def progression(self, n):

# ”””Print next n values of the progression.”””
         print(n.join(str(next(self)) for j in range(n)))
