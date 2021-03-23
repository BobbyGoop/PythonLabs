from main import answer_check
from products.BKProduct import *
from products.PKProduct import *


class Cart:
	def __init__(self):
		self.products = list()

	def show_chosen_products(self):
		print("Состав корзины: ")
		count = 1
		for item in self.products:
			print(f"{count} {item.name} - {item.price} {f'руб/кг, всего {item.weight} кг' if type(item) is BKProduct else 'руб'}")
			count += 1

	def total_cost(self):
		check = 0
		for item in self.products:
			check += item.get_cost()
		return check

	def add_products(self, market):
		print("\nВыберите продукт, который вы хотите добавить в корзину:")
		while True:
			market.show_products()
			answer = answer_check(len(market.stock)+1)
			if market.stock[answer-1].get_rest() != 0:
				if type(market.stock[answer-1]) is BKProduct:
					print("Необходимо взвевисить товар, прежде чем положить в корзину.")
					print(f"Пожалуйста, введите число от 1 до {market.stock[answer - 1].get_rest()} (оставшееся количество на складе)")
					weight = answer_check(market.stock[answer - 1].get_rest())
					market.stock[answer - 1].stock_amount -= weight
					self.products.append(market.stock[answer - 1])
					self.products[-1].set_weight(weight)
				else:
					self.products.append(market.stock[answer - 1])
					market.stock[answer - 1].stock_amount -= 1
					weight = 1
			else:
				print ("Извините, товар, который вы выбрали, закончился")
			# Костыль для реализации goto
			answer = 0
			while answer != 1 and answer != 3:
				print("\nХотите продолжить выбор? \n1. Да \n2. Выложить товар \n3. Перейти к оплате")
				answer = answer_check(3)
				if answer == 2 and len(self.products) != 0:
					self.remove_product(0, True, market, weight)
					continue
				elif answer == 2 and len(self.products) == 0:
					print("Ваша корзина пустая !")
					continue
			if answer == 1:
				continue
			if answer == 3:
				return

	def remove_product(self, amount, flag=False, market=None, weight=0):
		print("\nВот ваш список товаров: ")
		while True:
			self.show_chosen_products()
			print("Выберите товар, который необходимо удалить: ")
			answer = answer_check(len(self.products))
			index = market.stock.index(self.products[answer - 1])
			if type(market.stock[index]) is BKProduct:
				market.stock[index].stock_amount += weight
			elif type(market.stock[index]) is PKProduct:
				market.stock[index].stock_amount += 1
			del self.products[answer - 1]
			if flag:
				print(f"Товар удален ")
				return
			if len(self.products) == 0:
				return False
			if self.total_cost() > amount:
				print("Товар удален, но вам все равно не хватает средств")
				continue
			else:
				print("Товар удален, на данный момент средств хвататет")
				return True
