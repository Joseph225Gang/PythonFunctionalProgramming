import collections
from dataclasses import dataclass, field
from order_item import OrderItem
from customer import Customer

def consume(it):
   collections.deque(it, maxlen=0)

def action_if(f, g, it):
     consume(f(i) for i in it if g(i))

def get_updated_tuple(p, f, it):
    return tuple(f(i) if p(i) else i for i in it)


@dataclass(frozen=True)
class Order:
    orders: tuple = field(init=False)

    orderid: int
    shipping_address: str
    expedited: bool
    shipped: bool
    customer: Customer
    order_items: tuple[OrderItem, ...]

    @staticmethod
    def mark_backordered(orders, orderid, itemnumber):
        return Order.map(lambda o:
                         o if o.orderid != orderid
                         else (Order(o.orderid, o.shipping, o.customer,
                           Order.map(lambda i:
                              i if i.itemnumber != itemnumber
                              else OrderItem(i.name, i.itemnumber, i.quantity, i.price, True 
				),
                              o.order_items)
                         )),
                        orders
    )