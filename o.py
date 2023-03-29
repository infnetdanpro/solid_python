from decimal import Decimal


# The Open–closed principle: "Software entities ... should be open for extension, but closed for modification."
class Discount:
    def __init__(self, customer: str, price: Decimal):
        self.customer = customer
        self.price = price

    def give_discount(self) -> Decimal:
        return self.price * Decimal('0.2')


# GOOD!
class VipDiscount(Discount):
    def give_discount(self) -> Decimal:
        return super().give_discount() * 2


# Now we have a new business requirement, and we rewrite Discount class
# BAD!!!
class Discount:
    def __init__(self, customer: str, price: Decimal):
        self.customer = customer
        self.price = price

    def give_discount(self) -> Decimal:
        if self.customer == 'vip':
            return self.price * Decimal('0.4')


