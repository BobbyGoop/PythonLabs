from products.Product import Product


class PKProduct(Product):
	def __init__(self, name, prod, price, stock_amount, pkg_weight):
		super().__init__(name, prod, price, stock_amount)
		self.pkg_weight = pkg_weight

	def get_rest(self):
		return self.stock_amount

	def get_cost(self):
		return self.price
