import sys
from products.Cart import Cart
from main import answer_check


class Client:
    def __init__(self, name, bonus, cash):
        self.name = name
        self.bonus = bonus
        self.cash = cash
        self.cart = Cart()

    def choose_and_pay(self, market):
        self.cart.add_products(market)
        self.pay_check(market)

    def show_info(self):
        print(self.name + "\nНаличные: " + str(self.cash) + "\nБонусы: " + str(self.bonus))

    def pay_check(self, market):
        self.cart.show_chosen_products()
        receipt = self.cart.total_cost()
        print(f"Полная сумма: {self.cart.total_cost()} рублей")
        print(f"У вас есть {self.cash} рублей и {self.bonus} баллов")
        if self.cash + self.bonus < receipt:
            print("Вам не хватает суммарных средств для оплаты товара. Выложите что либо из корзины")
            if not self.cart.remove_product(self.cash + self.bonus, market=market):
                print(
                    "Вы выложили все товары из корзины.\n Запустите программу "
                    "снова, чтобы взять другие продукты. ")
                sys.exit(1)
            else:
                pass
        receipt = self.cart.total_cost()
        print(f"ИТОГО: {receipt} рублей")
        print("\nКак вы хотите оплатить товары?")
        print("1. Наличными \n2. Бонусами\n3. Списать баллы и наличными")
        answer = answer_check(3)
        if answer == 1:
            if receipt <= self.cash:
                print("Вы успешно купили товары. Поздравляем!" if receipt > 0
                      else "Вы успешно ничего не купили. Поздравляем! (нет)")
                print("Ваша сдача: " + str(self.cash - self.cart.total_cost()))
                sys.exit(1)
            else:
                print("Вам не хватает средств")
                if self.cart.remove_product(self.cash, market=market):
                    print("Вы успешно купили товары. Поздравляем!")
                    print(f"Итоговая сумма: { self.cart.total_cost()}\n "
                          f"Ваша сдача: { self.cash - self.cart.total_cost()}")
                    sys.exit(1)
                else:
                    print(
                        "Вы выложили все товары из корзины, и, видимо, у Вас совсем нет средств.\n Запустите программу снова, чтобы взять другие продукты. ")
                    sys.exit(1)
        elif answer == 2:
            if receipt <= self.bonus:
                print("Вы успешно купили товары. Поздравляем!" if receipt > 0
                      else "Вы успешно ничего не купили. Поздравляем! (нет)")
                print(f"Оставшиеся бонусы: {self.bonus - receipt}")
                sys.exit(1)
            else:
                print("Вам не хватает средств")
                if self.cart.remove_product(self.bonus, market=market):
                    print("Вы успешно купили товары. Поздравляем!")
                    print(f"Итоговая сумма: {self.bonus - self.cart.total_cost()}")
                    sys.exit(1)
                else:
                    print(
                        "Вы выложили все товары из корзины, и, видимо, у Вас совсем нет средств.\n Запустите программу снова, чтобы взять другие продукты. ")
                    sys.exit(1)
        elif answer == 3:
            # Если суммарно не хватает, то товар удаляется до вступления в if-elif
            # Если суммы бонусов и наличных хватате, то дополнительная проверка не нужна.
            if receipt == 0:
                print("Вы успешно ничего не купили. Поздравляем! (нет)")
                sys.exit(1)
            if receipt <= self.bonus:
                print("Чек был оплачен бонусами. Поздравляем!")
                print(f"Оставшиеся бонусы: {self.bonus - receipt}")
            else:
                cash_rest = receipt - self.bonus
                if cash_rest <= self.cash:
                    print("Вы успешно купили товары и списали бонусы. Поздравляем!")
                    print(f"Итоговая сумма: {cash_rest}, Ваша сдача: {self.cash - cash_rest}")
                    sys.exit(1)
