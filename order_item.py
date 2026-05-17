from dataclasses import dataclass

class OrderItem:
    name: str
    itemnumber: int
    quantity: int
    price: float
    backordered: bool

    @property
    def total_price(self):
        return self.quantity * self.price