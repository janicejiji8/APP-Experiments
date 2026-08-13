from abc import ABC, abstractmethod


# Step 1: Define PaymentStrategy interface
class PaymentStrategy(ABC):

    @abstractmethod
    def pay(self, amount):
        pass


# Step 2: Implement different payment strategies

class CreditCardPayment(PaymentStrategy):

    def pay(self, amount):
        print(f"Paid ₹{amount} using Credit Card.")


class PayPalPayment(PaymentStrategy):

    def pay(self, amount):
        print(f"Paid ₹{amount} using PayPal.")


class BitcoinPayment(PaymentStrategy):

    def pay(self, amount):
        print(f"Paid ₹{amount} using Bitcoin.")


# Step 3: Create PaymentProcessor class
class PaymentProcessor:

    def __init__(self, strategy):
        self.strategy = strategy

    # Step 4: Switch strategy at runtime
    def set_strategy(self, strategy):
        self.strategy = strategy

    def process_payment(self, amount):
        self.strategy.pay(amount)


# Main Program
if __name__ == "__main__":

    # Create payment processor with Credit Card strategy
    processor = PaymentProcessor(CreditCardPayment())
    processor.process_payment(1000)

    # Switch to PayPal at runtime
    processor.set_strategy(PayPalPayment())
    processor.process_payment(2000)

    # Switch to Bitcoin at runtime
    processor.set_strategy(BitcoinPayment())
    processor.process_payment(3000)
