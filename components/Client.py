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
		print(self.name + "\nНаличные: " + self.cash + "\nБонусы: " + self.bonus)

	def show_cart(self):
		print("\nСостав корзины: ")
		counter = 1
		for item in self.products:
			print(str(counter) + item.name + " - " + str(item.price) + r" руб\кг, вес " + str(item.weight) + " кг"
				  if type(item) is BulkProduct else str(counter) + ") "  + item.name + " - " + str(item.price))
			counter += 1

	def full_price(self):
		check = 0
		for item in self.products:
			check += item.price if type(item) is PkgProduct else item.price * item.weight
		return check


	def remove_product(self, amount):
		print("Вот ваш список товаров: ")
		while True:
			self.show_cart()
			print("Выберите товар, который необходимо удалить: ")
			answer = answer_check(len(self.products))
			del self.products[answer - 1]
			if len(self.products) == 0:
				return False
			if self.full_price() > amount:
				print("Товар удален, но вам все равно не хватает средств")
				continue
			else:
				print("Товар удален, на данный момент средств хвататет")
				return True


	def add_products(self, market):
		print("Выберите продукт, который вы хотите добавить в корзину:\n")
		while True:
			market.show_products()
			answer = answer_check(6)
			if answer == 6:
				break
			elif answer == 4 or answer == 5:
				print("Необходимо взвевисить товар, прежде чем положить в корзину.")
				print("Пожалуйста, введите число от 1 до " + str(market.stock[answer - 1].show_rest()) + "(оставшееся количество на складе)")
				weight = answer_check(market.stock[answer - 1].show_rest())
				self.products.append(market.stock[answer - 1])
				self.products[-1].set_weight(weight)
			else:
				self.products.append(market.stock[answer - 1])
			print("Хотите продолжить выбор? \n1.Да \n2.Перейти к оплате")
			final_answer = answer_check(2)
			if final_answer == 1:
				continue
			else:
				break
		return

	def pay_check(self):
		self.show_cart()
		print("Полная сумма: " + str(self.full_price()) + " рублей")
		print("У вас есть " + str(self.cash) + " рублей и " + str(self.bonus) + " баллов")
		if self.cash + self.bonus < self.full_price():
			print("Вам не хватает суммарных средств для оплаты товара. Выложите что либо из корзины")
			if not self.remove_product(self.cash + self.bonus):
				print("Вы выложили все товары из корзины, и, видимо, у Вас совсем нет средств.\n Запустите программу снова, чтобы взять другие продукты. ")
				sys.exit(1)
			else:
				pass
		print("\n Как вы хотите оплатить товары?")
		print("1. Наличные\n2. Баллы по карте\n3. Списать баллы и оплатить остаток суммы наличными")
		answer = answer_check(3)
		check = self.full_price()
		if answer == 1:
			if check <= self.cash:
				print("Вы успешно купили товары. Поздравляем!")
				print("Ваша сдача: " + str(self.cash - self.full_price()))
				sys.exit(1)
			else:
				print("Вам не хватает средств")
				if self.remove_product(self.cash):
					print("Вы успешно купили товары. Поздравляем!")
					print("Итоговая сумма: " + str(self.full_price()) + " Ваша сдача: " + str(self.cash - self.full_price()))
					sys.exit(1)
				else:
					print("Вы выложили все товары из корзины, и, видимо, у Вас совсем нет средств.\n Запустите программу снова, чтобы взять другие продукты. ")
					sys.exit(1)
		elif answer == 2:
			if check <= self.bonus:
				print("Вы успешно купили товары. Поздравляем!")
				print("Оставшиеся бонусы: " + str(self.bonus - check))
				sys.exit(1)
			else:
				print("Вам не хватает средств")
				if self.remove_product(self.bonus):
					print("Вы успешно купили товары. Поздравляем!")
					print("Итоговая сумма: " + str(self.full_price()) + str(self.bonus - check))
					sys.exit(1)
				else:
					print("Вы выложили все товары из корзиныи, и, видимо, у Вас совсем нет средств.\n Запустите программу снова, чтобы взять другие продукты. ")
					sys.exit(1)
		elif answer == 3:
			# Если суммарно не хватает, то товар удаляется до вступления в if-elif
			# Если суммы бонусов и наличных хватате, то дополнительная проверка не нужна.
			if check <= self.bonus:
				print("Чек был оплачен бонусами. Поздравляем!")
				print("Оставшиеся бонусы: " + str(self.cash - check))
			else:
				cash_rest = check - self.bonus
				if cash_rest <= self.cash:
					print("Вы успешно купили товары и списали бонусы. Поздравляем!")
					print("Итоговая сумма: " + str(cash_rest) + ", Ваша сдача: " + str(self.cash - cash_rest))
					sys.exit(1)