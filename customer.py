class Customer:
    name: str = ''
    address: str = ''
    enterprise: bool = False
    def __init__(self, name, address, enterprise):
     self.name = name
     self.address = address
     self.enterprise = enterprise

    def notify(cust, msg):
     print(f'Sending {msg} to {cust.name} at {cust.address}')