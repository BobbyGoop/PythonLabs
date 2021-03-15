from abc import ABC, abstractmethod
from random import random


class AbstractProduct(ABC):

	def __init__(self, name, price, stock_amount):
		self.name = name
		self.price = price
		self.stock_amount = stock_amount
		self.barcode = str(range(1000, 9999, 1))

	@abstractmethod
	def get_cost(self):
		pass
