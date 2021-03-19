from components.BulkProduct import *
from components.PkgProduct import *


class Market:
    def __init__(self, client):
        self.client = client
        self.stock = list()
        self.stock.append(PkgProduct("Молоко", 100, 1000, 200))
        self.stock.append(PkgProduct("Творог", 100, 1000, 200))
        self.stock.append(PkgProduct("Мясо", 230, 100, 100))
        self.stock.append(BulkProduct("Фрукты", 20, 150))
        self.stock.append(BulkProduct("Овощи", 20, 150))
        self.client.add_products(self)
        self.client.pay_check()

    def show_products(self):
        counter = 1
        for item in self.stock:
            print(
                f"{counter}) {item.name} - {item.price} {'руб' if type(item) is PkgProduct else 'руб/кг'} "
                + f"(осталось: {item.stock_amount} {'упаковок' if type(item) is PkgProduct else 'кг'})")
            counter += 1
