# SOLID 
"""
Single Responsibility
Open/Closed <--
Liskov Substitution
Interface Segregation
Dependency Inversion
"""
# A sale system for example

# write code that's open for extension so we should be able to extend the existing code with new functionality
# but closed for modification, we shouldn't need to modify the original code

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
        
# class PaymentProcessor:
#     def pay_debit(self,order:Order, security_code):
#             print("Processing debit payment type")
#             print(f"Verifying security code: {security_code}")
#             order.set_status(status="paid")
#     def pay_credit(self,order:Order,security_code):
#             print("Processing credit payment type")
#             print(f"Verifying security code: {security_code}")
#             order.set_status(status="paid")

# In order to extend the payment type, we can create classes and subclasses,and for each new payment type, we just creat the new subclass

from abc import ABC, abstractmethod
class PaymentProcessor(ABC):
    @abstractmethod
    def pay(self, order, security_code):
        pass

class DebitPaymentProcessor(PaymentProcessor):
    def pay(self, order, security_code):
        print("Processing debit payment type")
        print(f"Verifying security code: {security_code}")
        order.set_status(status="paid")

class CreditPaymentProcessor(PaymentProcessor):
    def pay(self, order, security_code):
        print("Processing credit payment type")
        print(f"Verifying security code: {security_code}")
        order.set_status(status="paid")

#Now, it's easy to extend a new payment type
class PaypalPaymentProcessor(PaymentProcessor):
    def pay(self, order, security_code):
        print("Processing paypal payment type")
        print(f"Verifying security code: {security_code}")
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
    payment_processor = PaypalPaymentProcessor()
    payment_processor.pay(order,"0372846")
    

if __name__ == "__main__":
    main()