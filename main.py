from Market import *


def answer_check(right_border):
	while True:
		try:
			to_check = int(input("=> "))
			if right_border >= to_check >= 1:
				return to_check
			else:
				raise BaseException
		except BaseException or ValueError:
			print("Введите корректные данные")


if __name__ == "__main__":
	market = Market()


