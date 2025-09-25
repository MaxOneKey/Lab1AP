from product import Product

class Menu:
    def __init__(self):
        self.items: list[Product] = []  # список продуктів у меню

    def add_product(self, product: Product):
        self.items.append(product)

    def show_menu(self):
        for p in self.items:
            print(f"{p.name} ({p.category}) – {p.price} грн")
