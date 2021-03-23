from products.Product import Product


class BKProduct(Product):
	def __init__(self, name, prod, price, stock_amount):
		super().__init__(name, prod, price, stock_amount)
		self.weight = 0

	def set_weight(self, weight):
		self.weight = weight

	def get_rest(self):
		return self.stock_amount

	def get_cost(self):
		return self.price * self.weight
