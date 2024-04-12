class Customer:
    def __init__(self, customer_id, name):
        self.customer_id = customer_id
        self.name = name


class LoyaltyPoints:
    def __init__(self):
        points = 0

    def earn_points(self, amount):
        self.points += amount

    def redeem_points(self, amount):
        if self.points >= amount:
            self.points -= amount
        else:
            print("Not enough points!")

    def show_points(self):
        return self.points


class VipCustomer(Customer, LoyaltyPoints):
    def __init__(self, customer_id, name):
        Customer.__init__(self, customer_id, name)
        LoyaltyPoints.__init__(self)


class Transaction:
    def __init__(self, transaction_id, customer, amount):
        self.transaction_id = transaction_id
        self.customer = customer
        self.amount = amount


class TransactionHistory:
    def __init__(self):
        self.transactions = []

    def add_transaction(self, transaction):
        self.transactions.append(transaction)

    def show_transactions(self):
        for transaction in self.transactions:
            print(transaction.transaction_id, transaction.customer, transaction.amount)


vipcustomer = VipCustomer("VIP001", "Benga")
vipcustomer.earn_points(40000)
vipcustomer.redeem_points(12500)

transaction1 = Transaction("T001", vipcustomer, 40000)
transaction2 = Transaction("T002", vipcustomer, 12500)

transatcion_history = TransactionHistory()
transatcion_history.add_transaction(transaction1)
transatcion_history.add_transaction(transaction2)

transatcion_history.show_transactions()
balance = vipcustomer.show_points()

print(f"Customer ID: {vipcustomer.customer_id}")
