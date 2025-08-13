# SOLID 
"""
Single Responsibility
Open/Closed
Liskov Substitution <--
Interface Segregation
Dependency Inversion
"""

# Liskov Substitution means that if you have objects in a program you should be able to replace those objects with instances of their subtypes or subclasses
# without altering the correctness of the program


class Order: 
    items = []
    quantities = []
    prices = []
    status = "open"

    def add_item(self,name,quantity,price):
        self.items.append(name)
        self.quantities.append(quantity)
        self.prices.append(price)

    def total_price(self):
        total = 0
        for i in range(len(self.prices)):
            total += self.quantities[i]*self.prices[i]
        return total
    
    def set_status(self, status):
         self.status = status
        
# we remove the security code in the pay method and add the initializer as the paypalpayment processor does not cantain security code but email instead

from abc import ABC, abstractmethod
class PaymentProcessor(ABC):
    @abstractmethod
    # def pay(self, order, security_code):
    def pay(self, order):
        pass

class DebitPaymentProcessor(PaymentProcessor):
    def __init__(self,security_code):
        self.security_code = security_code

    # def pay(self, order, security_code):
    def pay(self, order):
        print("Processing debit payment type")
        print(f"Verifying security code: {self.security_code}")
        order.set_status(status="paid")

class CreditPaymentProcessor(PaymentProcessor):
    def __init__(self,security_code):
        self.security_code = security_code

    # def pay(self, order, security_code):
    def pay(self, order):
        print("Processing credit payment type")
        print(f"Verifying security code: {self.security_code}")
        order.set_status(status="paid")

#Now, it's easy to extend a new payment type
class PaypalPaymentProcessor(PaymentProcessor):
    def __init__(self,email_address):
        self.email_address = email_address

    # def pay(self, order, security_code):
    def pay(self, order):
        print("Processing paypal payment type")
        print(f"Verifying email adress: {self.email_address}")
        order.set_status(status="paid")

def main():
    order = Order()
    order.add_item("Keyboard",1,50)
    order.add_item("SSD",1,150)
    order.add_item("USB cable",2,5)

    print(order.total_price())

    # payment_processor = PaymentProcessor()
    # payment_processor.pay_debit(order,"0372846")
    # payment_processor = CreditPaymentProcessor()
    payment_processor = PaypalPaymentProcessor("email@email.com")
    payment_processor.pay(order)

# we're properly using the pay method instead of changing what parameters mean in order to fit our specific use case 

if __name__ == "__main__":
    main()