import collections

def consume(it):
   collections.deque(it, maxlen=0)

def action_if(f, g, it):
     consume(f(i) for i in it if g(i))

class Order:
    
      order = []

      ordered: int = 0
      shipping_address: str = ''
      expedited: bool = False
      shipped: bool = False
      customer: object = None
      order_items: list

      def __init__(self, orderid, shipping_address, expedited, shipped, customer, order_items):
       self.orderid = orderid
       self.shipping_address = shipping_address
       self.expedited = expedited
       self.shipped = shipped
       self.customer = customer
       self.orde_items = order_items
      
      @staticmethod
      def test_expedited(order):
        return order.expedited
      
      @staticmethod
      def test_not_expedited(order):
          return not order.expedited
      
      @staticmethod
      def get_customer_name(order):
        return order.customer.name
      
      @staticmethod
      def get_shipping_address(order):
        return order.shipping_address
      
      @staticmethod
      def filter(predicate, it):
         return list(filter(predicate, it))
      
      @staticmethod
      def map(func, it):
            return list(map(func, it))
      @staticmethod
      def get_filtered_info(predicate, func, orders):
            return Order.map(func, Order.filter(predicate, orders))
     

      @staticmethod
      def get_expedited_orders_customer_names():
        return Order.get_filtered_orders_customer_(Order.test_expedited)
      
      @staticmethod
      def get_expedited_orders_customer_names(predicate):
          return Order.get_filtered_info(
              Order.test_expedited,
              Order.get_customer_name,
              Order.orders
          )
      
      @staticmethod
      def set_order_expedited(orderid, orders):
            for order in Order.get_order_by_id(orderid, orders):
                order.expedited = True

      @staticmethod
      def get_expedited_orders_customer_addresses():
          return Order.get_filtered_info(
             Order.test_expedited,
             Order.get_customer_name
          )
     
      @staticmethod
      def get_not_expedited_orders_customer_addresses():
          return Order.get_filtered_info(
             Order.test_not_expedited,
             Order.get_customer_name
          )
      
      @staticmethod
      def get_expedited_orders_shipping_addresses():
          return Order.get_filtered_info(
             Order.test_not_expedited,
              Order.get_shipping_address
          )
      
      @staticmethod
      def set_order_expedited(orderid):
         for order in Order.orders:
            if order.orderid == orderid:
               order.expedited = True
      @staticmethod
      def get_order_by_id(orderid):
         return Order.get_filtered_info(
            lambda order: order.orderid == orderid,
            lambda order: order
         )
      @staticmethod
      def set_order_expedited(orderid):
          for order in Order.get_order_by_id(orderid):
             order.expedited = True
      
      @staticmethod
      def notify_backordered(orders, msg):
       action_if(
           lambda o: o.customer.notify(o.customer, msg),
           lambda o: any(i.backordered for i in o.order_items),
           orders
       )