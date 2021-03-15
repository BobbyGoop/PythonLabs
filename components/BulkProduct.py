from components.AbstractProduct import *


class BulkProduct(AbstractProduct):
	def __init__(self, name, price_kg, stock_amount_kg):
		super().__init__(name, price_kg, stock_amount_kg)
		self.weight = 0

	def set_weight(self, weight):
		self.weight = weight

	def show_rest(self):
		return self.stock_amount

	def get_cost(self):
		return self.price * self.amount
