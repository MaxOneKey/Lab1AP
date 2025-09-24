class Supplier:
    def __init__(self, supplier_id: int, name: str, product_type: str, contact: str):
        self.supplier_id = supplier_id  # int – ID постачальника
        self.name = name                # str – назва постачальника
        self.product_type = product_type # str – що постачає (кава, молоко, цукор)
        self.contact = contact          # str – контактна інформація
