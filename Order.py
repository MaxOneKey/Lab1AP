from customer import Customer
from product import Product

class Order:
    def __init__(self, order_id: int, customer: Customer):
        self.order_id = order_id
        self.customer = customer
        self.products: list[Product] = []  # список продуктів у замовленні
        self.total: float = 0.0
        self.is_paid: bool = False

    def add_product(self, product: Product):
        self.products.append(product)
        self.total += product.price

    def pay(self):
        self.is_paid = True
