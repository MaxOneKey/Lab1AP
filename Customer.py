class Customer:
    def __init__(self, customer_id: int, name: str, phone: str, money:float):
        self.customer_id = customer_id  # int – ID клієнта
        self.name = name                # str – ім’я
        self.phone = phone              # str – телефон
        self.money_amount = money       # float - кількість грошей
