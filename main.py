import sys

from components.Market import *
from components.Client import *


def answer_check(right_border):
	while True:
		try:
			to_check = input(">> ")
			if right_border >= int(to_check) >= 1:
				return int(to_check)
			else:
				raise BaseException
		except BaseException or ValueError:
			print("Введите корректные данные")


if __name__ == "__main__":
	# Начало программы
	# Создаем случайного клиента
	rich_client = Client("Богатый Покупатель", 100000, 100000)
	poor_client = Client("Бедный Покупатель", 100, 30)
	print("Вы зашли в магазин.Что вы хотите сделать?\n1.Выбрать товары\n2.Выйти")
	answer = answer_check(2)
	if answer == 1:
		market = Market(poor_client)
	elif answer == 2:
		sys.exit(1)
