class Product:
    def __init__(self, product_id: int, name: str, category: str, price: float, available: bool):
        self.product_id = product_id  # int – ID продукту
        self.name = name              # str – назва (Еспресо, Лате, Круасан)
        self.category = category      # str – категорія (кава, чай, десерт)
        self.price = price            # float – ціна
        self.available = available    # bool – чи є в наявності
