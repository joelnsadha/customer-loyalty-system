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

    def retieve_points(self):
        pass


class VipCustomer(Customer, LoyaltyPoints):
    def __init__(self, customer_id, name):
        Customer.__init__(self, customer_id, name)
