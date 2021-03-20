import sys
from main import answer_check
from components.BulkProduct import BulkProduct
from components.PkgProduct import PkgProduct


class Client:
    def __init__(self, name, bonus, cash):
        self.name = name
        self.bonus = bonus
        self.cash = cash
        self.products = list()

    def show_info(self):
        print(self.name + "\nНаличные: " + str(self.cash) + "\nБонусы: " + str(self.bonus))

    def show_cart(self):
        print("Состав корзины: ")
        counter = 1
        for item in self.products:
            print(
                str(counter) + ") " + item.name + " - " + str(item.price) + r" руб\кг, вес " + str(item.weight) + " кг"
                if type(item) is BulkProduct else str(counter) + ") " + item.name + " - " + str(item.price))
            counter += 1

    def full_price(self):
        check = 0
        for item in self.products:
            check += item.get_cost()
        return check

    def remove_product(self, amount, flag=False, market=None, weight=0):
        print("\nВот ваш список товаров: ")
        while True:
            self.show_cart()
            print("Выберите товар, который необходимо удалить: ")
            answer = answer_check(len(self.products))
            index = market.stock.index(self.products[answer - 1])
            if type(market.stock[index]) is BulkProduct:
                market.stock[index].stock_amount += weight
            elif type(market.stock[index]) is PkgProduct:
                market.stock[index].stock_amount += 1
            del self.products[answer - 1]
            if flag:
                print(f"Товар удален ")
                return
            if len(self.products) == 0:
                return False
            if self.full_price() > amount:
                print("Товар удален, но вам все равно не хватает средств")
                continue
            else:
                print("Товар удален, на данный момент средств хвататет")
                return True

    def add_products(self, market):
        print("\nВыберите продукт, который вы хотите добавить в корзину:")
        while True:
            market.show_products()
            answer = answer_check(6)
            if market.stock[answer-1].show_rest() != 0:
                if answer == 6:
                    break
                elif answer == 4 or answer == 5:
                    print("Необходимо взвевисить товар, прежде чем положить в корзину.")
                    print(
                        f"Пожалуйста, введите число от 1 до {market.stock[answer - 1].show_rest()} (оставшееся количество "
                        f"на складе)")
                    weight = answer_check(market.stock[answer - 1].show_rest())
                    market.stock[answer - 1].stock_amount -= weight
                    self.products.append(market.stock[answer - 1])
                    self.products[-1].set_weight(weight)
                else:
                    self.products.append(market.stock[answer - 1])
                    market.stock[answer - 1].stock_amount -= 1
                    weight = 1
            else:
                print ("Товара, который вы выбрали, нет в наличии")

            # Костыль для реализации goto
            answer = 0
            while answer != 1 and answer != 3:
                print("\nХотите продолжить выбор? \n1. Да \n2. Выложить товар \n3. Перейти к оплате")
                answer = answer_check(3)
                if answer == 2 and len(self.products) != 0:
                    self.remove_product(0, True, market, weight )
                    continue
                elif answer == 2 and len(self.products) == 0:
                    print("Ваша корзина пустая !")
                    continue
            if answer == 1:
                continue
            if answer == 3:
                return


    def pay_check(self, market):
        self.show_cart()
        print(f"Полная сумма: {self.full_price()} рублей")
        print(f"У вас есть {self.cash} рублей и {self.bonus} баллов")
        if self.cash + self.bonus < self.full_price():
            print("Вам не хватает суммарных средств для оплаты товара. Выложите что либо из корзины")
            if not self.remove_product(self.cash + self.bonus, market=market):
                print(
                    "Вы выложили все товары из корзины, и, видимо, у Вас совсем нет средств.\n Запустите программу "
                    "снова, чтобы взять другие продукты. ")
                sys.exit(1)
            else:
                pass
        print("Полная сумма: " + str(self.full_price()) + " рублей")
        print("\nКак вы хотите оплатить товары?")
        print("1. Наличные\n2. Баллы по карте \n3. Списать баллы и оплатить остаток суммы наличными")
        answer = answer_check(3)
        check = self.full_price()
        if answer == 1:
            if check <= self.cash:
                print("Вы успешно купили товары. Поздравляем!" if check > 0
                      else "Вы успешно ничего не купили. Поздравляем! (нет)")
                print("Ваша сдача: " + str(self.cash - self.full_price()))
                sys.exit(1)
            else:
                print("Вам не хватает средств")
                if self.remove_product(self.cash, market = market):
                    print("Вы успешно купили товары. Поздравляем!")
                    print("Итоговая сумма: " + str(self.full_price()) + " Ваша сдача: " + str(
                        self.cash - self.full_price()))
                    sys.exit(1)
                else:
                    print(
                        "Вы выложили все товары из корзины, и, видимо, у Вас совсем нет средств.\n Запустите программу снова, чтобы взять другие продукты. ")
                    sys.exit(1)
        elif answer == 2:
            if check <= self.bonus:
                print("Вы успешно купили товары. Поздравляем!" if check > 0
                      else "Вы успешно ничего не купили. Поздравляем! (нет)")
                print(f"Оставшиеся бонусы: {self.bonus - check}")
                sys.exit(1)
            else:
                print("Вам не хватает средств")
                if self.remove_product(self.bonus, market = market):
                    print("Вы успешно купили товары. Поздравляем!")
                    print(f"Итоговая сумма: {self.bonus - check}")
                    sys.exit(1)
                else:
                    print(
                        "Вы выложили все товары из корзиныи, и, видимо, у Вас совсем нет средств.\n Запустите программу снова, чтобы взять другие продукты. ")
                    sys.exit(1)
        elif answer == 3:
            # Если суммарно не хватает, то товар удаляется до вступления в if-elif
            # Если суммы бонусов и наличных хватате, то дополнительная проверка не нужна.
            if check == 0:
                print("Вы успешно ничего не купили. Поздравляем! (нет)")
                sys.exit(1)
            if check <= self.bonus:
                print("Чек был оплачен бонусами. Поздравляем!")
                print(f"Оставшиеся бонусы: {self.cash - check}")
            else:
                cash_rest = check - self.bonus
                if cash_rest <= self.cash:
                    print("Вы успешно купили товары и списали бонусы. Поздравляем!")
                    print(f"Итоговая сумма: {cash_rest}, Ваша сдача: {self.cash - cash_rest}")
                    sys.exit(1)
