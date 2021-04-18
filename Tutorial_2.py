print("*****************************Question 1************************************************")


class Flower:
    def __init__(self, name, num_petals, price):
        # Initialize
        self.name = str(name)
        self.num_petals = int(num_petals)
        self.price = float(price)

     # Setters
    def setName(self, name):
     self.name = name

    def setPetals(self, num_petals):
     self.num_petals = num_petals


    def setPrice(self, price):
     self.price = price

    # Getters


    def get_Name(self):
     return self.name


    def getPetals(self):
     return self.num_petals


    def getPrice(self):
     return self.price


flower1 = Flower("One", 2, 200)
print("Flower")
print("Name: " + flower1.get_Name())
print("Number of petals: " + str(flower1.getPetals()))
print("Price: " + str(flower1.getPrice()))
print("\n")

print("*****************************Question 2************************************************")
class CreditCard:
    def __init__(self, customer, bank, acnt,limit):
        self.customer = customer
        self.bank = bank
        self.acnt = acnt
        self.limit = limit
        self.balance = 0

    def get_customer(self):
        return self.customer

    def get_bank(self):
        return self.bank

    def get_account(self):
        return self.acnt

    def get_limit(self):
        return self.limit

    def get_balance(self):
        return self.balance

    def charge(self, price):
        if price + self.balance > self.limit:
            return False
        else:
            self.balance += price
            return True

    def make_payment(self, amount):
        self.balance -= amount

class PredatoryCreditCard(CreditCard):
    def __init__(self, customer, bank, acnt, limit, apr):
        super().__init__(customer, bank, acnt, limit)
        self.apr = apr

    def charge(self, price):
        success = super().charge(price)
        if not success:
            self.balance += 10
        return success

    def process_month(self):
        """Assess monthly interest on outstanding balance."""
        if self.balance > 0:
            # if positive balance, convert APR to monthly multiplicative factor
            monthly_factor = pow(1 + self.apr, 1 / 12)
            self.balance *= monthly_factor
print("*****************************Question 4************************************************")


class Progression:
    def __init__(self, start=0):
        self._current = start

    def _advance(self):
        self._current += 1

    def __next__(self):
        if self._current is None:
            raise StopIteration()
        else:
            answer = self._current
            self._advance()
            return answer

    def __iter__(self):
        return self

    def print_progression(self, n):
        print(' '.join(str(next(self)) for j in range(n)))

class FibonacciProgression(Progression):
    def __init__(self, first=2, second=200):
        super().__init__(first)  # start progression at first
        self._prev = second - first  # fictitious value preceding the first

    def _advance(self):
        self._prev, self._current = self._current, self._prev + self._current

print('Fibonacci progression with default start values:')
FibonacciProgression().print_progression(10)


