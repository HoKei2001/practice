# SOLID 
"""
Single Responsibility
Open/Closed
Liskov Substitution 
Interface Segregation <--
Dependency Inversion
"""

# Interface Segregation means that overall it's better if you have several specific interfaces as opposed to one general purpose interface


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

# class PaymentProcessor_SMS(PaymentProcessor):
#     @abstractmethod
#     def auth_sms(self, code): 
#         pass


# instead of doing this with classes and subclasses we can also use composition: 
# create a separate class called sms authorizer that handles the authentication
class SMSAuth:
    authorized = False

    def verify_code(self,code):
        print(f"Verifying code {code}")
        self.authorized = True

    def is_authorized(self) -> bool:
        return self.authorized
    

class DebitPaymentProcessor(PaymentProcessor):
    def __init__(self,security_code, authorizer:SMSAuth):
        self.security_code = security_code
        self.authorizer =authorizer

    def pay(self, order):
        if not self.authorizer.is_authorized():
            raise Exception("Not authorized")
        print("Processing debit payment type")
        print(f"Verifying security code: {self.security_code}")
        order.set_status(status="paid")

class CreditPaymentProcessor(PaymentProcessor):
    def __init__(self,security_code):
        self.security_code = security_code

    def pay(self, order):
        print("Processing credit payment type")
        print(f"Verifying security code: {self.security_code}")
        order.set_status(status="paid")

class PaypalPaymentProcessor(PaymentProcessor):
    def __init__(self,email_address,authorizer:SMSAuth):
        self.email_address = email_address
        self.authorizer =authorizer

    def pay(self, order):
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

    authorizer = SMSAuth()
    authorizer.verify_code("555555")

    payment_processor = PaypalPaymentProcessor("email@email.com",authorizer)
    payment_processor.pay(order)


if __name__ == "__main__":
    main()


