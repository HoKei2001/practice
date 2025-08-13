# SOLID 
"""
Single Responsibility <--
Open/Closed
Liskov Substitution
Interface Segregation
Dependency Inversion
"""
# A sale system for example
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
    
    # def pay(self, payment_type, security_code):
    #     if payment_type == "debit":
    #         print("Processing debit payment type")
    #         print(f"Verifying security code: {security_code}")
    #         self.status = "paid"
    #     elif payment_type == "credit":
    #         print("Processing credit payment type")
    #         print(f"Verifying security code: {security_code}")
    #     else:
    #         raise Exception(f"Unknown payment type: {payment_type}")

    #For better separation, add a set_status method to Order instead of changing it directly via the attribute
    def set_status(self, status):
         self.status = status
        

# we want a single class and method have single responsibility, but the class order here takes some extra tasks like payment
# here we create a new class called payment
class PaymentProcessor:
    def pay_debit(self,order:Order, security_code):
            print("Processing debit payment type")
            print(f"Verifying security code: {security_code}")
            order.set_status(status="paid")
    def pay_credit(self,order:Order,security_code):
            print("Processing credit payment type")
            print(f"Verifying security code: {security_code}")
            order.set_status(status="paid")

def main():
    order = Order()
    order.add_item("Keyboard",1,50)
    order.add_item("SSD",1,150)
    order.add_item("USB cable",2,5)

    print(order.total_price())
    # order.pay("debit","0372846")

    payment_processor = PaymentProcessor()
    payment_processor.pay_debit(order,"0372846")


if __name__ == "__main__":
    main()