from supplier import Supplier
from product import Product
from menu import Menu
from customer import Customer
from order import Order
from barista import Barista

class CoffeeShop:
    def __init__(self, name: str):
        self.name = name
        self.suppliers: list[Supplier] = []
        self.menu = Menu()
        self.orders: list[Order] = []
        self.baristas: list[Barista] = []

    def add_supplier(self, supplier: Supplier):
        self.suppliers.append(supplier)

    def add_barista(self, barista: Barista):
        self.baristas.append(barista)

    def create_order(self, order: Order):
        self.orders.append(order)
        return order
