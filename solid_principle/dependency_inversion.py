# SOLID 
"""
Single Responsibility
Open/Closed
Liskov Substitution
Interface Segregation
Dependency Inversion  <--
"""

# Dependency inversion means I want our classes to depend on abstractions and not on concrete subclasses.


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
        


from abc import ABC, abstractmethod
class PaymentProcessor(ABC):
    @abstractmethod
    def pay(self, order):
        pass

# here, all three payment processors are depending on a concrete class SMSAuth, 
# to follow the dependency inversion principle, we should make it abstract, so we create the abstract class Authorizer

class Authorizer(ABC):
    @abstractmethod
    def is_authorized(self) -> bool:
        pass

class SMSAuth(Authorizer):
    authorized = False

    def verify_code(self,code):
        print(f"Verifying code {code}")
        self.authorized = True

    def is_authorized(self) -> bool:
        return self.authorized
    
class NotARobot(Authorizer):
    authorized = False

    def not_a_robot(self):
        print("Are you a robot? Naaaa...")
        self.authorized = True

    def is_authorized(self) -> bool:
        return self.authorized
    

class DebitPaymentProcessor(PaymentProcessor):
    def __init__(self,security_code, authorizer:Authorizer):
        self.security_code = security_code
        self.authorizer =authorizer

    def pay(self, order:Order):
        if not self.authorizer.is_authorized():
            raise Exception("Not authorized")
        print("Processing debit payment type")
        print(f"Verifying security code: {self.security_code}")
        order.set_status(status="paid")

class CreditPaymentProcessor(PaymentProcessor):
    def __init__(self,security_code):
        self.security_code = security_code

    def pay(self, order:Order):
        print("Processing credit payment type")
        print(f"Verifying security code: {self.security_code}")
        order.set_status(status="paid")

class PaypalPaymentProcessor(PaymentProcessor):
    def __init__(self,email_address,authorizer:Authorizer):
        self.email_address = email_address
        self.authorizer = authorizer

    def pay(self, order:Order):
        if not self.authorizer.is_authorized():
            raise Exception("Not authorized")
        print("Processing paypal payment type")
        print(f"Verifying email adress: {self.email_address}")
        order.set_status(status="paid")


def main():
    order = Order()
    order.add_item("Keyboard",1,50)
    order.add_item("SSD",1,150)
    order.add_item("USB cable",2,5)

    print(order.total_price())

    authorizer = NotARobot()
    payment_processor = PaypalPaymentProcessor("email@email.com",authorizer)
    authorizer.not_a_robot()
    payment_processor.pay(order)


if __name__ == "__main__":
    main()


