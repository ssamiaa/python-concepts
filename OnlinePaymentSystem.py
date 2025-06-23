# Objective: Simulate different payment methods (Credit Card, UPI, Net Banking) using inheritance and polymorphism.
class PaymentMethod:
    def pay(self, amount):
        print("Processing generic payment")

    def payment_type(self):
        print("Generic payment method")

class CreditCard(PaymentMethod):
    def __init__(self, card_number, cvv):
        self.card_number = card_number
        self.cvv = cvv

    def pay(self, amount):
        print(f"Paid ₹{amount} via Credit Card ending with {self.card_number[-4:]}.")

    def payment_type(self):
        print("Credit card payment method")

class UPI(PaymentMethod):
    def __init__(self, upi_id):
        self.upi_id = upi_id

    def pay(self, amount):
        print(f"Paid ₹{amount} via UPI ID {self.upi_id}.")

    def payment_type(self):
        print("UPI payment method")

class NetBanking(PaymentMethod):
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def pay(self, amount):
        print(f"Paid ₹{amount} via Net Banking (User: {self.username}).")

    def payment_type(self):
        print("Net banking payment method")

def process_payment(payment_method, amount):
    payment_method.payment_type()
    payment_method.pay(amount)

# Example usage
credit_card = CreditCard("1234567890123456", "123")
process_payment(credit_card, 500)

upi = UPI("user@bank")
process_payment(upi, 200)

net_banking = NetBanking("aasha", "1234")
process_payment(net_banking, 1000)
