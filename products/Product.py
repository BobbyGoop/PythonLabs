from abc import ABC, abstractmethod


class Product(ABC):

	def __init__(self, name, prod, price, stock_amount):
		self.name = name
		self.price = price
		self.stock_amount = stock_amount
		self.prod = prod

	@abstractmethod
	def get_cost(self):
		pass

	@abstractmethod
	def get_rest(self):
		pass
