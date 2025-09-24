from order import Order

class Barista:
    def __init__(self, barista_id: int, name: str):
        self.barista_id = barista_id
        self.name = name

    def prepare_order(self, order: Order):
        if order.is_paid:
            print(f"Бариста {self.name} готує замовлення #{order.order_id} для {order.customer.name}")
        else:
            print(f"Замовлення #{order.order_id} ще не оплачено!")
