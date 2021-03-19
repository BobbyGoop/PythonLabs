from components.Market import *
from components.Client import *


def answer_check(right_border):
	while True:
		try:
			to_check = int(input(">> "))
			if right_border >= to_check >= 1:
				return to_check
			else:
				raise BaseException
		except BaseException or ValueError:
			print("Введите корректные данные")


if __name__ == "__main__":
	# Начало программы
	# Создаем клиентов
	accounts = [Client("Миллионер", 100000, 10000), Client("Средний Покупатель", 500, 1000), Client("Бедный Покупатель", 20, 30)]
	print("Вы зашли в магазин. Что вы хотите сделать? \n1. Выберите аккаунт \n2. Выйти")
	answer = answer_check(2)
	if answer == 1:
		print("Доступные аккаунты: ")
		for item in accounts:
			print(item.name)
		chosen_account = accounts[answer_check(len(accounts)) - 1]
	elif answer == 2:
		sys.exit(1)
	print("\nАккаунт выбран. Выберите дальнейшие действия:")
	while True:
		print("\n1. Выбрать товары \n2. Посмотреть баланс \n3. Выйти")
		answer = answer_check(3)
		if answer == 1:
			market = Market(chosen_account)
			break
		elif answer == 2:
			chosen_account.show_info()
			continue
		elif answer == 2:
			break
	sys.exit(1)
