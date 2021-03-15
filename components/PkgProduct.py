from components.AbstractProduct import AbstractProduct


class PkgProduct(AbstractProduct):
	def __init__(self, name, price, stock_amount, pkg_weight):
		super().__init__(name, price, stock_amount)
		self.pkg_weight = pkg_weight

	def show_rest(self):
		return self.stock_amount

	def get_cost(self):
		return self.price
