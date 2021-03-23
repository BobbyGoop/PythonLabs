from products.BKProduct import *
from Client import Client
from products.PKProduct import *
from main import answer_check


class Market:
    def __init__(self):
        self.accounts = [Client("Миллионер", 100000, 100000),
                         Client("Человек среднего достатка", 500, 1000),
                         Client("Бедняк", 100, 30)]
        self.stock = [PKProduct("Молоко", "Тема", 100, 1000, 200),
                      PKProduct("Творог", "Простоквашино", 100, 1000, 200),
                      PKProduct("Мясо", "Мираторг", 230, 100, 100),
                      BKProduct("Фрукты", "Турция", 20, 150),
                      BKProduct("Овощи", "Краснодарский Край", 20, 150)]
        self.enter()

    def show_products(self):
        count = 1
        for item in self.stock:
            print(
                f"{count} {item.name} {item.prod} - {item.price} {'руб' if type(item) is PKProduct else 'руб/кг'}"
                + f"{', ' + str(item.pkg_weight) + 'гр' if type(item) is PKProduct else ''}"
                + f" (осталось: {item.stock_amount} {'шт' if type(item) is PKProduct else 'кг'})")
            count += 1

    def enter(self):
        print("Вас приветствует ПРОДУКТЫ 24 ONLINE! Что вы хотите сделать? ")
        while True:
            print("\n1. Выбрать аккаунт \n2. Зарегестрировать новый\n3. Выйти")
            answer = answer_check(3)
            if answer == 1:
                print("Доступные аккаунты: ")
                for item in self.accounts:
                    print(item.name)
                chosen_account = self.accounts[answer_check(len(self.accounts)) - 1]
                print("\nАккаунт выбран. Выберите дальнейшие действия:")
                while answer != 3:
                    print("\n1. Посмотреть товары \n2. Посмотреть баланс \n3. Выйти")
                    answer = answer_check(3)
                    if answer == 1:
                        chosen_account.choose_and_pay(self)
                        break
                    elif answer == 2:
                        chosen_account.show_info()
                        continue
                    elif answer == 3:
                        return
            elif answer == 2:
                self.register_account()
            elif answer == 3:
                return

    def register_account(self):
        print("Введите ФИО: ")
        name = input(">> ")
        print("Введите сумму наличных: ")
        cash = int(input(">> "))
        print("Введите сумму бонусных баллов: ")
        bonus = int(input(">> "))
        self.accounts.append(Client(name, cash, bonus))