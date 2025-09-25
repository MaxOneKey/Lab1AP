class Warehouse:
    def __init__(self, location):
        self.location = location
        self.products = []  # список товарів на складі

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, product):
        if product in self.products:
            self.products.remove(product)

    def list_products(self):
        return [p.name for p in self.products]
