class PaymentStrategy:
    def pay(self, amount):
        pass


class CreditCardPayment(PaymentStrategy):
    def pay(self, amount):
        print("Payment of ₹", amount, "processed using Credit Card.")


class DebitCardPayment(PaymentStrategy):
    def pay(self, amount):
        print("Payment of ₹", amount, "processed using Debit Card.")


class UPIPayment(PaymentStrategy):
    def pay(self, amount):
        print("Payment of ₹", amount, "processed using UPI.")


class PayPalPayment(PaymentStrategy):
    def pay(self, amount):
        print("Payment of ₹", amount, "processed using PayPal.")


class PaymentProcessor:
    def __init__(self, strategy):
        self.strategy = strategy

    def set_strategy(self, strategy):
        self.strategy = strategy

    def process_payment(self, amount):
        self.strategy.pay(amount)


print("__________________________________")
print("   CONFIGURABLE PAYMENT PROCESSING")
print("__________________________________")

amount = float(input("Enter payment amount: ₹"))

print("\nSelect Payment Method:")
print("1. Credit Card")
print("2. Debit Card")
print("3. UPI")
print("4. PayPal")

choice = int(input("Enter your choice: "))

if choice == 1:
    payment_method = CreditCardPayment()
elif choice == 2:
    payment_method = DebitCardPayment()
elif choice == 3:
    payment_method = UPIPayment()
elif choice == 4:
    payment_method = PayPalPayment()
else:
    print("Invalid payment method.")
    exit()

processor = PaymentProcessor(payment_method)
processor.process_payment(amount)

